def remove (string):
  a=set()
  list=[]
  for ch in string:
    if ch not in a:
      a.add(ch)
      list.append(ch)
      
  return ''.join(list)


string=input()
print(remove(string))