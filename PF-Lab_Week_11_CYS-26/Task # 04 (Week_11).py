# 01
s1 = {1,2,3}
s2 = {4,5,6}
s1.update(s2)
print(s1)
print(s2)

# 02
s1 = {1,2,3}
s2 = {4,5,6}
s3 = {7,8,9}
print(set.intersection(s1,s2,s3))

# 03
s1 = {1,2,3}
s2 = {4,3,6}
(s1.intersection_update(s2))
print(s1)
s2.discard(s1)
print(s2)
