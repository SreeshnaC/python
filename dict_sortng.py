my_dict={'apple':4,'banana':3,'orange':7,'grape':2}
ascending_dict=dict(sorted(my_dict.items()))
print("ascending is:",ascending_dict)
descending_dict=dict(sorted(my_dict.items(),reverse=True))
print("descending is:",descending_dict)