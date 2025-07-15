dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict1 = dict1.copy()
merged_dict1.update(dict2)
print("Merged using update():", merged_dict1)

merged_dict2 = {**dict1, **dict2}
print("Merged using ** unpacking:", merged_dict2)
