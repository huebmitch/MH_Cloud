testlist = {"a", "b", "c"}
testlist2 = {"a", "d", "f"}
testlist3 = {"a", "e", "g"}
testlist4 = {"a", "h", "i"}

data = set(testlist)
data2 = set(testlist2)
data3 = set(testlist3)
data4 = set(testlist4)

print(data)
print(data & data2 & data3 & data4)
