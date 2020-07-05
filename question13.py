import csv

def create_csv(file_name, values):
    with open(file_name, 'w') as per:
        writer = csv.writer(per)
        writer.writerow(['name', 'adderss', 'age'])
        writer.writerows(values)
        

info = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
create_csv('info.csv', info)