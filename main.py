import csv

files = open('proj 7.csv','r')
reader =csv.DictReader(files)
for list in reader:
        print(dict(list))