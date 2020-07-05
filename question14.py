import csv

def read_csv():
    with open('info.csv', 'r') as per:
        reader = csv.DictReader(per)
        for info in reader:
            return info

z = read_csv()
print(z)