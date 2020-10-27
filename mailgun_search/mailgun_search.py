## Author: Giselle Northy
## Date: 9/2/2019
##
## This program was written with Mailgun csv suppressions in mind
## However, it just checks for a string given by the user in the given CSV file_name
## And prints out the rows the string was found in, into a new CSV file
## This is good for searching very large CSV files efficiently without needing to open them


import csv
import sys

## VARIABLES

search_string = "@email.com"
file_name = "search.csv"
new_file = "emails.csv"

print('Welcome to the Mailgun Suppression Email Scraper!\nEnter the domain to search. Example @someemail.com.\n')
search_string = raw_input()

got_name = False
while(got_name == False):
    file_name = raw_input('Enter the Mailgun CSV to check. Example mailgun_list.csv\n')

    try:     #read csv, and check for file name exists
        csv_file = csv.reader(open(file_name, "r"), delimiter=",")
        got_name = True
    except FileNotFoundError as err:  #Not working yet - Supposed to loop back if file not found
        print("Could not find file " + file_name + "error: ") #Likely because this version of Python handles this differently
        print(err)

row_index = 0;

# variable to write to - writing to csv file
write_file = open(new_file, 'w')
write_file.write('created_at,code,error,MessageHash,address\r\n')

for row in csv_file:
    match_found = False; #creating the variable match_found
    for column in row:
        if search_string in column:
            match_found = True;
    if match_found:
        for column in row:
            #if "," in column:
            write_file.write('"'+str(column) + '",')
            #else:
            # write_file.write(str(column) + ",")
        write_file.write("\r\n")
print('Searching ' + file_name + ' for the domain ' + search_string + '...')
print('Read your results in the new file ' + new_file)

write_file.close()
