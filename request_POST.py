import csv
import requests 

import string
printable = set(string.printable)

URL = 'https://melp-silverio.herokuapp.com/restaurants'

with open('restaurantes.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    header = reader.next()
    for row in reader:
        x = ""
        DATA = dict(zip(header, row))
        r = requests.post(url = URL, data = DATA) 
        #print r.text
        #break
        