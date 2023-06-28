#overiding the existing file as we initiate editing
'''#a->use for append in file
   #r->use for read from file
   #w->use for wring in file
   '''
with open('newfile.txt',mode='w') as file:
    file.write("This is new file creating and editing in cmd of python")
    file.writelines(["line one","\nline two","\nline three"])