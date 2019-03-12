'''
q :Create 3 csv files with arithmetic data
Imput files
input_file1.csv -->2,3
input_file2.csv -->5,6
input_file3.csv -->8,9

Output fil
output_file.csv

Read data from csv files using threads


'''


import csv
import threading
import time
INIT_PATH = 'C:/Users/gajaya/Desktop/'

#Function to read from csv file
def read_from_csv(filepath):
    file = open(filepath, 'r')
    csv_reader = csv.reader(file, delimiter=',')
    data = None
    for row in csv_reader:
        data = row
        break
    file.close()
    return data

#Function to write to csv file
def write_to_csv(filepath, *args, **kwargs):
    file = open(filepath, kwargs['mode'])
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(args)
    file.close()

#Task to be executed by the threads
def task_function(id):
    print("Starting thread ",id)
    time.sleep(3)
    data=read_from_csv(INIT_PATH+"input_file"+str(id)+".csv")
    a,b=int(data[0]),int(data[1])
    print("Data in input file",id," is ",a,b)
    write_to_csv(INIT_PATH+'output_file.csv',a,b,a+b,a-b,a*b,a/b,a**3,b**3,mode='a')
    print("Exiting thread ",id)

    
if __name__=='__main__':
    time.sleep(4)
    
    write_to_csv(INIT_PATH+'output_file.csv','A','B','Sum','Sub','Mul','Div','CubeA','CubeB',mode='w')
    
    for i in range(1,4):
        time.sleep(1)
        t = threading.Thread(target=task_function, args=(i,))
        t.start()
 

    
