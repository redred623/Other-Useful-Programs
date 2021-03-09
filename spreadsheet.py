#!/usr/bin/env python3
import gspread
import csv
import re 
import os

def CSV_Download_url(url, new_file): 
    # use creds to create a client to interact with the Google Drive API
    gc = gspread.service_account(filename='D:/code library/onboarding/Service_account_cred.json')
    sh = gc.open_by_url(url)

    # Find a workbook by name or position and open the first sheet
    worksheet = sh.sheet1

    #the fields will help to sort the csv and take irrelavent data 
    fields = input('Put your fields here or leave blank for email and name\n' )
    fields = fields.split()
    if fields == '': 
        fields = ['email','accounts:first_name','accounts:last_name']

    #create new csv file and create header line with fields
    with open(new_file,'w') as file: 
        data = worksheet.get_all_records()
        writer = csv.DictWriter(file,fields,extrasaction='ignore')
    #create header
        writer.writeheader()
    #add rows until data stops
        writer.writerows(data)

def function_a(URL): 
    gc = gspread.service_account(filename='D:/code library/onboarding/Service_account_cred.json')
    sh = gc.open_by_url(URL)
    worksheet = sh.sheet1
    fields = input('Put your fields here or leave blank for email and name\n' )
    if fields == '': 
        fields = ['email','accounts:first_name','accounts:last_name']


    with open('data_test.csv','w') as file: 
        data = worksheet.get_all_records()
        #the extrascaction field stops it from erroring out from the other fields it does not see
        writer = csv.DictWriter(file,fields,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)



# Greet the user and have them select what they want to do



print('Welcome to gsuite util by Noah Padgett\nThis program was designed for use at Raleigh Oak Charter to assist with the duties of the IT personnel\nYou will need to make a gsuite project for this application to work correctly\nFollow these instructions https://gspread.readthedocs.io/en/latest/oauth2.html#oauth-client-id ')
print('make sure you add the service account email as an editor to the document in my case: onboarding@onboarding-project-297914.iam.gserviceaccount.com')
input_main = input('what would you like to do?\n a - open a spreadsheet and export it to a local file\n b - transfer a local csv to your google drive\n> ' )
#this section validates respones put in by the user to see what actions they would like to proceed with


#main user interaction panel with treed responses to find the correct place to put them using while true loops to validate if the user put the information in the correct range
while True:
    if input_main.lower() == 'a':
        input_a = input('Would you rather use the NAME or URL to link your document?\n')
        while True:
            #if they decide url it makes sure what they enter is a valid google share link and that is has editing permission
            if input_a.lower() == 'url':
                while True:
                    gdoc=input('Put link to document here\n')
                    match = re.findall(r'https://docs\.google\.com.*/edit\?usp=sharing$',gdoc)
                    if match[0] == gdoc:
                        #once matched it will then create the parameters for the file it creates and make sure the user is okay with the path the file will go
                        name = input('what would you like to name the file?\n>')
                        if name == "":
                            #default name if none is choosen
                            name = "Google_data"
                        new_file_location = os.path.expanduser(r'~\documents\\' + name + r'.csv')
                        override_file = input('if you want a different path than ' + os.path.expanduser(r'~\documents\\') + " enter it now.\n> ")
                        if override_file != "":
                            new_file_location = override_file + name + '.csv'
                        CSV_Download_url(gdoc,new_file_location)
                        input('Task Completed Succesfully!')
                        exit()
                    else: gdoc = input('your link either is not valid or does not have edit permissions. If you want to try your link anyway press enter if you would like to try again type \'retry\'\n>')
                        
            elif input_a.lower() == 'name':
                gdoc=input('Put the name of the document here\n')
                function_a(gdoc)
            else:
                print('you have made an invalid choice. Type either \"NAME\" or \"URL\"')
    elif input_main.lower() == 'b':
        input_b = input('please specify a path to your local file. EX. D:/code/onboarding/data.csv')
    else: input_main = input('Invalid input please select either a or b\n> ')
