#! /usr/bin/python

import csv 

print("Welcome to Student lookup tool" )
first_name= (input("First Name: ").lower()).strip()
last_name= (input('Last Name: ').lower()).strip()


with open('d:/code library/google data sheet/users.csv') as d: 
    csv_reader = csv.DictReader(d)
    line_count = 0 
    s = ""
    for row in csv_reader: 
        if row["First Name [Required]"].lower() == first_name:
            if row['Last Name [Required]'].lower() == last_name: 
                s ='success!'
    
    if s == 'success!': 
        print ('{} {} is here!'.format(first_name.capitalize(), last_name.capitalize()))
    else: 
        print('{} {} is not here!'.format(first_name.capitalize(), last_name.capitalize()))
input('press enter to exit')
