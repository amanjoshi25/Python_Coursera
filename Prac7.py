#sets
set_a ={1, 2, 3, 4, 5, 5}
set_b ={2,3, 8, 9, 10, 5}
#union and or (|) function  used to join both set
print(set_a|set_b)
print(set_a.union(set_b))
#difference and (-) function used to remove that present in set a
print(set_a.difference(set_b))
print(set_a-set_b)
#symettric difference and (^)= intersection
print(set_a.symmetric_difference(set_b))
print(set_a^set_b)
set_a.add(0)
set_a.remove(5)
set_a.discard(2)
print(set_a)
