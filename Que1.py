
list = []

# Taking input
n = int(input("Enter size of list: "))
for i in range(n):
    item = int(input())
    list.append(item)

# selection_sort function
def selection_sort(list):
    for i in range(n-1):
        minIdx = i
        # searching for minimum value in rest part of list
        for j in range(i+1,n):
            if list[j]<list[minIdx]:
                minIdx = j
        if minIdx != i:
            list[i],list[minIdx] = list[minIdx],list[i]

# calling function
selection_sort(list)

# printing list elements
print(list)

