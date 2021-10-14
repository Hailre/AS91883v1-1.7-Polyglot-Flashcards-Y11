MyList = [0, 1, 2, 3, 4, 5]
print(MyList[1])
MyList.append(6)
print(MyList)
MyList.remove(2)
print(MyList)


print(MyList)

MyNewList = []
for value in MyList:
    MyNewList.append(value)
print(MyNewList)
MyNewList.insert(0, 2)
print(MyNewList)
