_list=[6,3,2,1,7,9,1,4,6,8]

for i in range(len(_list)-1):
  _min=i
  for j in range(i+1,len(_list)):
    if _list[_min] > _list[j]:
      _min=j
  _list[i],_list[_min]=_list[_min],_list[i]

print(_list)
