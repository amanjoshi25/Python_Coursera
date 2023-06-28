'''1.read()
   2.readline()
   3.readlines()'''
with open('sample.txt', 'r') as file:
 print(file. read (44))

with open('sample.txt', 'r') as file:
 print(file. readline())

with open('sample.txt', 'r') as file:
 data=file. readlines()
 for x in data:
  print(x)
