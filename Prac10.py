#solution of error in prac11.py
# index error
items = [1,2,3,4,5]
item = items[6]
print(item)

#divide by zero error
def divide_by(a, b):
    return a / b


ans = divide_by(40, 0)
print(ans)

#file not found error
with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())

