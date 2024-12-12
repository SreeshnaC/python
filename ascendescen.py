my_dict={'apple':5,'banana':2,'orange':8,'grape':3}
ascending_dct=dict(sorted(my_dict.items()))
print("Ascending is:",ascending_dct)
descending_dct=dict(sorted(my_dict.items(),reverse=True))
print("Descending is:",descending_dct)