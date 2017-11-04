import csv
import datetime

fieldnames = ["ID", "PRICE", "DATE", "NAME", "LOCATION", "URL", "PARSE_DATE"]
path = "data.csv"
my_dict = []
delimiterCsv = '~'
currentDate = 0

#Read as a dict so it is easier to search for columns.
def csv_dict_reader(file_obj):
    try:
        with open(file_obj) as f_obj:
            reader = csv.DictReader(f_obj, delimiter='~')
    except Exception as e:
        print e

    return reader

#Writes as a dict so it is easier to search for columns.
def csv_dict_writer(path, fieldnames, data):
    with open(path, "a") as out_file:

        writer = csv.DictWriter(out_file, delimiter = delimiterCsv, fieldnames=fieldnames)
        try:
            for row in data:
                writer.writerow(row)
        except Exception as e:
            print e

#User API. Creates the dict and appends to it.
def csv_write(data):
    data.append(currentDate)
    inner_dict = dict(zip(fieldnames, data))
    my_dict.append(inner_dict)

#User API. Writes the header.
def init_csv():
    currentDate = datetime.datetime.now()
    currentDate = (currentDate.strftime("%d-%m-%Y")).encode()

    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter = delimiterCsv, fieldnames=fieldnames)
        writer.writeheader()

#User API. The function that actually writes in the csv file.
def write_to_csv():
    csv_dict_writer(path,fieldnames, my_dict)

#User API. It reads the dict saved in an cvs file.
def read_csv():
    reader = csv_dict_reader(path)
    return reader

#
# if __name__ == "__main__":
#
#     data = ["first_name,last_name,city".split(","),
#
#             "Tyrese,Hirthe,Strackeport".split(","),
#
#             "Jules,Dicki,Lake Nickolasville".split(","),
#
#             "Dedric,Medhurst,Stiedemannberg".split(",")
#
#             ]
#
#     my_list = []
#
#     fieldnames = data[0]
#
#     for values in data[1:]:
#
#         inner_dict = dict(zip(fieldnames, values))
#
#         my_list.append(inner_dict)
#
#     path = "data.csv"
#
#     csv_dict_writer(path, fieldnames, my_list)
#
#     with open("data.csv") as f_obj:
#
#         csv_dict_reader(f_obj)