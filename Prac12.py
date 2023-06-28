''' #file handling in python
  Two types of file handling in python 
 1.Open()-> they used for (Reading,writing and creating):
         1.1 Open fun accept two argument->
             open(<fileName><file_Location>,<mode>):
         1.2 Mode sets->
             'r'->open and read(Text Mode/.txtfile),
             'rb'->open and read(binary Mode)
             'a'->open for editing or appending data->open(<fileNAme>,a)

 2.Close()->they used to close the open file connection
          no argument
 3.with open()->with open('testing .txt' ,'r') as file:(No close funtion needed)

  '''


#access the file
file = open('test.txt',mode='r')
data=file. readline()
print(data)
file.close()

#use of with open function
with open('test2.txt',mode='r') as file:
 dat=file. readline()
 print(dat)

