def main(): 
  for i in range(no_stu):
    marks = int(input(f"Enter the marks of Student{i + 1} : "))
    ls.append(marks)

  print("\n_________MARKS____________")
  print(f"********{ls}********")


def sum_avg():
  sum = 0
  for i in range(no_stu):
    if ls[i] == -1 :
      continue
    else:
      sum = sum + ls[i]
  print("The Sum is =",sum)
  print("The Average is =", sum/len(ls))

def maxim():
  mx = 0
  for i in range(len(ls)):
    if mx < ls[i]:
      mx = ls[i]
  print("The Maximum marks : ",mx)

def minim():
  mn = ls[0] 
  for i in range(len(ls)):
    if ls[i] < 0:
      continue
    elif ls[i] < mn:
      mn = ls[i]
  print("The Minimun marks : ",mn)

def abcnt():
  count = 0
  for i in range(len(ls)):
    if ls[i]==-1:
      count += 1
  print(count)
  return count


def frequency():
  num= {}
  for i in ls:
    if i not in num:
      num[i] = 0
    num[i] += 1
  print(num)
  max_key = max(num, key=num.get)
  print(f"The number with max frequency is {max_key} : {num[max_key]} times")

if __name__ == "__main__":
  no_stu = int(input("Enter the number of Students : "))
  ls = []
  main()
  while True:
    
    print("\n\n---------------Main Menu-------------\n")
    pk = int(input("Press 1 to see the Average and Sum : \nPress 2 to see the Maximun marks : \nPress 3 to see the Minimum marks : \nPress 4 to get the abscent no : \nPress 5 to see the marks with highest frequency : \n"))

    if pk == 1:
      sum_avg()

    elif pk == 2:
      maxim()

    elif pk == 3:
      minim()

    elif pk == 4:
      abcnt()

    elif pk == 5:
      frequency()

    else : 
      break
