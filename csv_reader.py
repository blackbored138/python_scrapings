import csv 
import re

fields = ['Email', 'Status'] 
values = []
filename = "eby_csv_sent.csv"

f = open("test.txt", "r")

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(fields)

    with open('test.txt', 'r') as file:
        data = file.read().replace('\n', '')
    counter = 0

    for x in f:
        x = x.lower()
        splitted_text = x.split("@")
        splitted_text[1] = '@gmail.com' if (splitted_text[1].startswith('g')) else '@'+splitted_text[1];

        x = splitted_text[0] + splitted_text[1]
        values = [x,"Not Sent"]  
        print(values) 
        csvwriter.writerow(values) 
#exit()  
