import random
number_of_friends_joining = int(input("Enter the number of friends joining (including you):"))
if number_of_friends_joining > 0:
    friends_list = []
    print("")
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends_joining):
        friends_list.append(input())
    print("")
    amount = int(input("Enter the total bill value:"))
    print("")
    lucky_feature = input("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
    if lucky_feature == "Yes":
        print("")
        lucky = friends_list[random.randint(0, len(friends_list) - 1)]
        print("{} is the lucky one!".format(lucky))
        print("")
        bill = dict().fromkeys(friends_list, round(amount / (len(friends_list) - 1), 2))
        bill[lucky] = 0
        print(bill)
    else:
        print("")
        print("No one is going to be lucky")
        print("")
        print(dict().fromkeys(friends_list, round(amount / len(friends_list), 2)))
else:
    print("")
    print("No one is joining for the party")