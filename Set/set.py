
# we can't store list and dictioonary in set because they are mutable

# we can store tuple in set bcz tuple is immutable

#? set is  mutable but elements in sets are immutable. i.e we can add and remove values in set but can't change the value which is present in set

collection = {1,2,3,"Hello"}
print(collection)
print(type(collection))

#* empty set
collection2 =  set()

#! collection2 = {} this is not correct way to make empty set . This is dictionary

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)

#! if we add 9 and 9.0 or 8 or 8.0 or any other numbrs like that then python treats both num as same . 
set3={9,9.0,7,7.45}
print(set3)