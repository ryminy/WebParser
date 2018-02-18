import csv
import datetime

class csvClass:
    fieldnames = ["ID", "PRICE", "DATE", "NAME", "LOCATION", "URL", "PARSE_DATE"]
    path = "data.csv"
    delimiterCsv = '~'
    currentDate = ""

    def __init__(self, path):
        currentDate_raw = datetime.datetime.now()
        currentDateLocal = (currentDate_raw.strftime("%d-%m-%Y")).encode()
        self.currentDate = currentDateLocal

        if len(path) > 0:
            self.path = path
        #clear the file each time
        open(self.path, 'w').close()

    def csv_write(self, data):
        data.append(self.currentDate)
        inner_dict = dict(zip(self.fieldnames, data))

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








