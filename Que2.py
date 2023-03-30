n = int(input("Enter size of list: "))
filename_list = []

#input
for i in range(n):
    item = input()
    filename_list.append(item)

# mapping extensions with file type name
extension_dict = {
                    "jpg": "image",
                    "png": "image",
                    "xls": "spreadsheet"
                  }

output_dict = {}

for filename in filename_list:
    # getting file name and extension
    ext = filename.split(".")
    if ext[-1] in extension_dict:
        output_dict[ext[0]] = extension_dict.get(ext[-1])
    else:
        output_dict[ext[0]] = "unknown"

print(output_dict)
        
    