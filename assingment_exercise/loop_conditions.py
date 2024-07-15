result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
expense_list = [2340, 2500, 2100, 3100, 2980]

total_heads = 0

for x in result:
    if x == "heads":
        total_heads += 1

# print(total_heads)


# for x in range(1, 11):
#     print(x.__pow__(2))

"""month_list = ['jan', 'feb', 'march', 'april', 'may']
e = int(input("enter expense amount: ", ))

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print("You spent {} in {}".format(e, month_list[month]))
else:
    print("You didn't spend {} in any listed months".format(e))"""


"""completed = 0

while completed <= 5:
    completed += 1
    print(completed)
    user_input = input("Are you tired? ", )

    if user_input == "yes":
        print("you didn't finish the race")
        break
    if user_input == "no":
        print("are you tired")
        continue

    if completed == 5:
        print("You did it :)")
        break
"""

for i in range(1, 6):
    s = ''
    for j in range(i):
        s += "*"
    print(s)






