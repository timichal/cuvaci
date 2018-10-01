import csv
with open('cuvaci_res.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    maxpotomci = 0
    for row in reader:
        if int(row[5]) > maxpotomci and row[2] == "pes":
            maxpotomci = int(row[5])
            print(row)