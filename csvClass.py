import csv
import datetime

class csvClass:
    fieldnames = ["ID", "PRICE", "DATE", "NAME", "LOCATION", "URL", "PARSE_DATE"]
    path = "data.csv"
    write_dict = []
    read_dict = []
    delimiterCsv = '~'
    currentDate = ""

    def __init__(self):
        currentDate_raw = datetime.datetime.now()
        currentDateLocal = (currentDate_raw.strftime("%d-%m-%Y")).encode()
        self.currentDate = currentDateLocal

    def csv_write(self, data):
        data.append(self.currentDate)
        inner_dict = dict(zip(self.fieldnames, data))
        self.write_dict.append(inner_dict)

    def write_to_csv(self):
        with open(self.path, "wb") as out_file:
            writer = csv.DictWriter(out_file, delimiter=self.delimiterCsv, fieldnames=self.fieldnames)
            writer.writeheader()
            try:
                for row in self.write_dict:
                    writer.writerow(row)
            except Exception as e:
                print e

    def print_csv(self):
        try:
            with open(self.path) as in_file:
                self.read_dict = csv.DictReader(in_file, delimiter=self.delimiterCsv, fieldnames=self.fieldnames)
                for row in self.read_dict:
                   print row
        except Exception as e:
            print e








