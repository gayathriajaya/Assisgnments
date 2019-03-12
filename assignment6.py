'''
# Assignment - 6
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

 	

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Ques
a. Read the sample.log file given in the attachments. 
b. Parse each line of the log and split into individual components.
c. Write each record after splitting into a CSV file.

Fields to display from the log file:
CLIENT_IP_Address, Date, GET/POST Protocol, PATH_OF_FILE, HTTP_PROTOCOL_VERSION, STATUS_CODE, SIZE_OF_FILE_REQUESTED

#-----------------------------------------------------------------
'''

import csv
         
def read_write_file(filepath1,filepath2):
    obj1=open(filepath1,'r')
    data=obj1.readlines()
    obj1.close()
    obj2=open(filepath2,'w')
    csv_writer=csv.writer(obj2,delimiter=',')
    csv_writer.writerow(['CLIENT_IP_Address','Date','GET/POST Protocol','PATH_OF_FILE','HTTP_PROTOCOL_VERSION','STATUS_CODE','SIZE_OF_FILE_REQUESTED'])
    for line in data:
        d=[x for x in line.split() if x!='-']
        csv_writer.writerow(d)
    obj2.close()

filepath1="D:\\Python\\Assignments\\sample.log"
filepath2 ="D:\\Python\\Assignments\\asigmnt6.csv"
read_write_file(filepath1,filepath2)
