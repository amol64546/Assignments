

def input_of_list():
    n = int(input("Enter size of list: "))
    list_of_dicts = []
    
    print("Enter fruit and color pair as fruit,color: ")
    for i in range(n):
        str = input("pair1: ")
        
        # split at (,) to get fruit and color
        items = str.split(",")
        
        # making dictionary
        dict_obj = {"fruit": items[0],"color":items[1]}
        
        # making list of dict
        list_of_dicts.append(dict_obj)
    return list_of_dicts
    


# insertion sort
def insertion_sort(list_of_dicts, key):
    for i in range(1, len(list_of_dicts)):
        j = i
        while j > 0 and list_of_dicts[j][key] < list_of_dicts[j-1][key]:
            list_of_dicts[j], list_of_dicts[j-1] = list_of_dicts[j-1], list_of_dicts[j]
            j -= 1
    return list_of_dicts

# input

list_of_dicts = input_of_list()
key = input("Enter key for sorting: ")

# sorting
sorted_list = insertion_sort(list_of_dicts, key)

# output
for item in sorted_list:
    print(item)