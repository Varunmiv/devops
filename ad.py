l=[1,2,3,[1,2],4]
l[3][1]='varjgftyugiugun'
l1=l.copy()
print(id(l))
print(id(l1))
print(l[0],id(l[0]))
print(l[0],id(l1[0]))
print(l[1],id(l[1]))
print(l[1],id(l1[1]))
print(        )
print(id(l[2]))
print(id(l[3][0]))
print(id(l[3][1]))
print(id(l[4]))