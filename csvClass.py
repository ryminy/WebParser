import csv
import datetime

class csvClass:
    fieldnames = ["ID", "PRICE", "DATE", "NAME", "LOCATION", "URL", "PARSE_DATE"]
    path = "data.csv"
    delimiterCsv = '~'
    currentDate = ""
    noDuplicateEntries = []

    def __init__(self, path):
        currentDate_raw = datetime.datetime.now()
        currentDateLocal = (currentDate_raw.strftime("%d-%m-%Y")).encode()
        self.currentDate = currentDateLocal

        if len(path) > 0:
            self.path = path
        #clear the file each time
        open(self.path, 'w').close()

    def saveNoDuplicates(self):
        #clear the file each time
        open(self.path, 'w').close()

        #I am going to signal that the input is already a dict
        dictFlag = 1
        for row in self.noDuplicateEntries:
            self.csv_write(row, dictFlag);

    def csv_write(self, data, dictFlag = 0):

        if dictFlag == 0:
            data.append(self.currentDate)
            inner_dict = dict(zip(self.fieldnames, data))
        else:
            inner_dict = data

        with open(self.path, "ab") as out_file:
            writer = csv.DictWriter(out_file, delimiter=self.delimiterCsv, fieldnames=self.fieldnames)
            try:
                writer.writerow(inner_dict)
            except Exception as e:
                print e

    def print_csv(self):
        read_dict = []

        try:
            with open(self.path) as in_file:
                read_dict = csv.DictReader(in_file, delimiter=self.delimiterCsv, fieldnames=self.fieldnames)
                for row in read_dict:
                    print row
        except Exception as e:
            print e

    def clearDuplicates(self):
        read_dict = []
        copyDict = []

        try:
            with open(self.path) as in_file:
                read_dict = csv.DictReader(in_file, delimiter=self.delimiterCsv, fieldnames=self.fieldnames)
                for row in read_dict:
                    copyDict.append(row)
        except Exception as e:
            print e

        for row in copyDict:
            duplicateFlag = 0

            for line in self.noDuplicateEntries:
                if row['ID'] == line['ID']:
                    duplicateFlag = 1
                    break
            if duplicateFlag == 1:
                continue
            else:
                self.noDuplicateEntries.append(row)

        self.saveNoDuplicates()








