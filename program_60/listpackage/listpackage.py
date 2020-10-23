#listpackage


def sortNumbers(num):
  for i in range(len(num)-1):
    for j in range(len(num)-1):
      if num[j] > num[j+1]:
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp
  print("Sorted numbers:", num)



def reverselist(list2):
    print(list2.reverse())
    print("reversed list :", list2)