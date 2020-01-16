import random
list = []
f = open("output.txt","w")
def big(count,list):
  if count == 0:
    return 0
  #print(count)
  list.append(count)
  list.append(count + random.randint(0,5000))
  return big(count-1,list)
def big2(count):
  list = []
  if count == 0:
    return 0
  big(500, list)
  print(count)
  f.write(str(list))
  return big2(count-1)
for x in range(25000):
  big2(10)
print("done")