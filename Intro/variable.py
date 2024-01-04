#INITIALIZE VARIABLE
variable = "Hello word"
variable = 123
variable: int = 123

variable = True
variable = False

text = "Hello word"
result = text.split(" ") # ["Hello", "word"]
result = text[0:5] # "Hello"
result = text[0:-6] # "Hell"

result=f'{text}!'# "Hello word"
result='{}!'.format(text)# "Hello word"

#LIST
l1 = [10,"Hello Word",True]
l2 = [10,20,30,40,504]
l2[1:2] # [20,30]

len(l1) # 3
l2.append(50) # [10,20,30,40,504,50]
result =l2[3]# 40
l2.sort() # [10,20,30,40,50,504]
del l2[0] # [20,30,40,50,504]
l1[2] = 8

#TUPLE
t=(10,"Hello Word",True)
t[1] # "Hello"
t[1:2] # ("Hello",True)
#t[1] = 8 # ERROR: TUPLE IS IMMUTABLE

#DICTIONARY
d = {"kew0":20,"key1":30,"key2":10}
d["key1"] # 30
d["key3"] = 40 # {"kew0":20,"key1":30,"key2":10,"key3":40}
d.items() # [("kew0",20),("key1",30),("key2",10),("key3",40)]
list(d.items()) # [("kew0",20),("key1",30),("key2",10),("key3",40)] 

d.keys() # ["kew0","key1","key2","key3"]
list(d.keys()) # ["kew0","key1","key2","key3"]

d.values() # [20,30,10,40]  
list(d.values()) # [20,30,10,40]   

#SETS
s = {1,2,3}
s = {1,2,3,2} #the item 2 is repeated => it is not added to the set {1,2,3}

s.add(4) #4 not repeated => it is added to the set {1,2,3,4}
s.add(2) #2 is repeated => it is not added to the set {1,2,3,4} 

#CONTROL FLOW
variable = 10

if variable == 10:
  print("Variable is equal to 10")
elif variable > 10:
  print("Variable is greater than 10")
else:
  print("Variable is less than 10")

#LOOP
list_var = [10,20,30,40,50]

for l in list_var:
  print(f"Element: {l}")

for i in range(5):
  print(i)
  
count = 0
while count < 5:
  print(count)
  count += 1  
  
l = [i for i in range(100)] # create a list [0,1]
print(l)
