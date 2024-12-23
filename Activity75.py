#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
list4 = [123,234,345,456,567,678]
list5 = [456,567,678,789,890,901]
list6 = list(zip(list4,list5))
print(list6)
list7 = [987,876,765,654,543,432,321]
list8 = [2019,2020,2021,2022,2023,2024,2025]
for i,e in zip(list7,list8[::-1]):
    print(i,e)
list9 = [1,2,3,4,5]
list10 = [6,7,8,9,10]
dict1 = {list9:list10 for list9,list10 in zip(list9,list10)}
print(dict1)
