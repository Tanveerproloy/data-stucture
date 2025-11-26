#Question - Implement an algorithm to determine if a list has all unique characters, using python list


myList = [5, 12, 7, 12, 19, 3, 8, 5, 14, 2, 17, 8, 10, 4, 19, 6, 1, 14, 9, 7]


def isUnique(list):
    a =[]
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

    
print(isUnique(myList))
