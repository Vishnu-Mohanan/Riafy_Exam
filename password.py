
def func():
  pwd = input("Enter your Password")

  l = len(pwd)

  special = ['!','@','#','$','%','^','&','*','(',')','=']
  upCaseCount = 0
  specialCount = 0
  numCount = 0

  for j in pwd:
    if j in special:
      specialCount+=1

  for k in pwd:
    if k.isnumeric():
      numCount+=1  

  for i in pwd:
    if i.isupper():
      upCaseCount+=1

  if pwd.find("123") != -1 or pwd.find("qwerty") != -1 or pwd.find("abc") != -1:
    return False

  elif l >= 8 and upCaseCount > 0 and  numCount > 0:
    return True
  

if func():
    print("True")
else:
    print("False")