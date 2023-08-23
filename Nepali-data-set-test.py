import csv

with open('EverestNER-test-bio.txt', 'r', encoding='utf-8-sig') as in_file:
    lines = (line.strip().split(" ") for line in in_file if line.strip())
    with open('Nepali-data-set-train.csv', 'w', newline='', encoding='utf-8-sig') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Token', 'Label'))
        writer.writerows(lines)
