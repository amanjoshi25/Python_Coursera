'''#recursion->repetitive problem,complex stucture
     1.The funtion call itself(repiting itself
     2.Always consider base case(funtion kha tk jyega))'''
'''def find_factorial_bylooping(n) :
  if n<0:
    return 0
  else :
    factorial = 1   
    for i in range(1,n+1):
     factorial*=i
   
    return factorial
print(find_factorial_bylooping(5) )'''
def fictorial_Recursive(n):
    if n==1:
        return 1
    else:
         return n*fictorial_Recursive(n-1)
    
print(fictorial_Recursive(6))