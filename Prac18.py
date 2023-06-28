#map function->it takes all object in a list
menu=["espresso","mocha","latte","cappuccino","cortado","americano"]

def findCoffe(coff):
    if coff[0]=='c':
        return coff
mapCoffee=map(findCoffe,menu)
print(mapCoffee)
for x in mapCoffee:
    print(x)  
#filter function->same is map funtion but create new list with on true value
filterCoffee=filter(findCoffe,menu)
print(filterCoffee)
for x in filterCoffee:
  print(x)     
