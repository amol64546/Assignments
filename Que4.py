
# input
def input_of_dict():
    n = int(input("Enter size of dict: "))
    dicts = {}
    
    print("Enter as key:value")
    for i in range(n):
        input_str = input("pair1: ")
        dict_items = input_str.split(":")
        dicts[dict_items[0]] = dict_items[1]
    return dicts
    
def switch_key_value(dict_obj):
    dicts = {}
    for key, value in dict_obj.items():
        dicts[value] = key
    
    return dicts


# input
dicts_obj = input_of_dict()

switched_dicts = switch_key_value(dicts_obj)

# output
print(switched_dicts)