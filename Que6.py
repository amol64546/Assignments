def f(lst, start, end):
    print(lst[start:end:2])
  
list = []  
print("Enter item of list or press enter to end: ")
while True:
    item = input()
    if item=="":
        break
    list.append(int(item))

first_idx = int(input("Enter first_idx of range: "))
second_idx = int(input("Enter second_idx of range: "))

f(list, first_idx,second_idx)
