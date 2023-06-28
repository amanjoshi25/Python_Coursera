my_d={1:'aman','name':'joshi',}
print(type(my_d))
my_d[2]='test 2'
print(my_d[1])
print(my_d)
for key,value in my_d.items():
    print(str(key)+":"+value)
