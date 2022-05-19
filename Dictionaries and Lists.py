
# prob1

l=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in l:
    new_dict, new_list = {}, {}

    for j in i:
        if not j in new_dict:
            new_dict[j] = 1
        else:
            new_dict[j] += 1
    for key, values in new_dict.items():
        if values > 1:
            new_list[key]=values
    print(new_list)

# qyestion 1

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)


# question 2
list1 =["Hello ", "take "]
list2 = ["Dear", "Sir"]
unique_combinations = []
len1=len(list1)
len2=len(list2)
res = [x + y for x in list1 for y in list2]
print(res)

# Prob 3
keys = ["Ten","Twenty","Thirty"]
value = [10,20,30]
map={}
lenth=len(keys)
if (len(keys)==len(value)):
    for i in range(lenth):
        map[keys[i]] = value[i]
    print(map)

# prob 4
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

# Prob 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# prob 6
varss = {"HuEx":[1, 3, 4], "is": [7, 6], "best": [4, 5]}
res=[]
for key, val in varss.items():
    res.append([key] + val)
print(res)
