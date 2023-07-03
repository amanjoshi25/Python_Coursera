#about pure funtion->doen't manupulate the original list outside the function
my_list=[1,2,3] #global scope
def add_to_list(lst,item):
   nl=lst.copy()
   nl.append(item)
   #lst.append( item)
   return nl
new_list= add_to_list(my_list,4)
print(my_list)
print(new_list)
