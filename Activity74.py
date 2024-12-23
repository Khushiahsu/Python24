#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.

list1 = [100,20,12]
list2 = [101,21,13]
res = map(lambda q,w :q+w,list1,list2)
print('The anser is:',list(res))
def res2(a):
    return a*a
list3 = list(map(res2,list2))
print(list3)