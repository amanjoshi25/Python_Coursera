f = open("file1.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(f_content_list)

import random
f = open("file1.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))

#at run time open any file
import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))