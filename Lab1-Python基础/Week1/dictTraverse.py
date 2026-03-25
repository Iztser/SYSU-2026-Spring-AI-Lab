def reverseKeyValue(dict):
    rdict = {}
    for key,value in dict.items():
        rdict[value] = key
    return rdict

dict = {}
n = int(input("请输入键值对数目："))
for i in range(n):
    line = input().split()
    if(len(line) == 2):
        dict[line[0]] = line[1]
rdict = reverseKeyValue(dict)
print(dict)
print(rdict)