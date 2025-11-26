#Question - Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
list1 = [1, 4 ,6]
list2 = [6, 1 ,4]

print(permutation(list1,list2))