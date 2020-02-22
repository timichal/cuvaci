import csv
with open('cuvacizkraceni.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    rows = []

    for row in reader:
        rows.append(row)

    i = 0
    for row in rows:
        if i == 0:
            row.append("potomci")
            row.append("vrhy")
        else:
            desc = 0
            dob = []
            for cmp_row in rows[i:len(rows)]:
                if (row[2] == "fena" and row[0] == cmp_row[3]) or (row[2] == "pes" and row[0] == cmp_row[4]):
                    desc += 1
                    dob.append(cmp_row[1])
            row.append(desc)
            row.append(len(set(dob)))
        i += 1

with open('cuvaci_res.csv', 'w', newline='') as csvout:
    writer = csv.writer(csvout, delimiter=';')
    for row in rows:
        writer.writerow(row)