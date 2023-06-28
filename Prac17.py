#str reverse by recursion
def str_R(str):
    if len(str)==0:
        return str
    else:
        return str_R(str[1:])+str[0]
str="aman"
reverse =str_R(str)
print(reverse)