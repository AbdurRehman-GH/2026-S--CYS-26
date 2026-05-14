s = {1,2,3,3}
print(s)


s = {"CE", "CS", "ISB", "CE"}
for i in s:
    print(i)


s = {"CE", "CS", "ISB", "CE"}    # doesn't give error 
s.add("AE")
s.discard("CS")
for i in s:
    print(i)


s = {"CE", "CS", "ISB", "CE"}     # gives error
s.remove("AE")
for i in s:
    print(i)


s = {"CE", "CS", "ISB", "CE"}
s.pop
print(s)


s1 = {1,2,3,}
s2 = {"A,B,C"}
s3 = {7, "Abid", "4,5,6"}
a = set.union(s1,s2,s3)
print(a)

s1 = {1,2,3}
s2 = {3,4,5}
print(set.union(s1,s2))

s1 = {1,2,3}
s2 = {4,5,6}
s1.update(s2)
print(s1)
print(s2)

s1 = {1,2,3}
s2 = {4,5,6}
s3 = {7,8,9}
print(set.intersection(s1,s2,s3))

s1 = {1,2,3}
s2 = {4,3,6}
(s1.intersection_update(s2))
print(s1)
s2.discard(s1)
print(s2)


s1 = {1,2,3}
s2 = {4,3,6}
s = s1.difference(s2)
print(s)
print(s1)
print(s2)

s1 = {1,2,3}
s2 = {4,3,6}
s = s1.symmetric(s2)
print(s)
print(s1)
print(s2)

s1 = {1,2,3}
s2 = {4,5,6}
s = s1.isdisjoint(s2)
print(s)


s1 = {1,2,3,4}
s2 = {1,2,3,4}
print(s1.issubset(s2))