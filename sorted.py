from typing import final


def Union(lst1,lst2):
    final_list = sorted(lst1+lst2)
    return final_list

#driverscode
lst1 = [23,4,56,7,888,6544,2,4]
lst2 = [56,77,34,67,88,99,9,]
print(Union(lst1,lst2))
#####################33

def Union(list1,list2):
    finallist = sorted(list1+list2)
    return finallist
list1 = [22,5456,6789,234,6,778]
list2 = [23566,775,34,2,5,546]
print(Union(list1,list2))

