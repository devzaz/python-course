expenses = [2200, 2350, 2600, 2130, 2190]


#1. In Feb, how many dollars you spent extra compare to January?
extra = int(expenses[1]) - int(expenses[0])
# print(extra)

# 2. Find out your total expense in first quarter (first three months) of the year.

total =  0
for x in expenses[:3]:
    total += x

# print(total)

# 3. Find out if you spent exactly 2000 dollars in any month


# print(2000 in expenses)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)

# print(expenses)

"""5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

expenses[3] = expenses[3] - 200
# print(expenses)


heros=['spider man','thor','hulk','iron man','captain america']


"""
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

print(heros.__len__())

heros.append('black panther')
heros.remove('black panther')

heros.insert(3, 'black panther')

heros[1:3] = ['doctor strange']

heros.sort()

print(heros)

