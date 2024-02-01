myDict = {'ravi': 10, 'raj': 8, 'shyam': 4,'amar': 51}
mykeys = list(myDict.keys())
mykeys.sort()
sorted_dict = {i: myDict[i] for i in mykeys}
print(sorted_dict)
