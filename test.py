import random
# Take user input — how many people want to join, including the user;
user_input = int(input("Enter the number of friends joining (including you):"))
# Otherwise, take the friends' names as input, iteratively;
if user_input > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for i in range(user_input):
        friends[input()] = 0
    # Else, take user input: the final bill;
    if user_input > 0:
        # Split the total bill equally among everyone;
        print("Enter the total bill value:")
        bill = int(input())
# Round the split value to two decimal places;
        split = round(bill / user_input, 2)
        friends = dict.fromkeys(friends, split)
        # print(friends)
    else:
        print("No one is joining for the party")
        # Do you want to use the "Who is lucky?" feature? Write Yes/No:
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    # If the user answers "Yes", choose a random person, who will pay nothing;
    answer = input()
    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        # Otherwise, if the user choice is Yes, re-split the bill according to the feature;
        #  Print the updated dictionary
        #  Round the split value to two decimal places;
        split = round(bill / (user_input - 1), 2)
        for i in friends:
            friends[i] = split
        #  Update the dictionary with new split values and 0 for the lucky person;
        friends[lucky] = 0
        print(friends)
        #  Print the updated dictionary values;

        # If the user answers "No", print the list of all people, who are splitting the bill;
    elif answer == "No":
        print("No one is going to be lucky")
        print(friends)
        #  Round the split value to two decimal places;
        #  Print the updated dictionary values;
        #  If there are no people to split the bill (the number of friends is 0 or/
        #  an invalid input), output "No one is joining for the party";
    else:
        print("Invalid input")

        # If there are no people to split the bill (the number of friends is 0 or/
        #  an invalid input), output "No one is joining for the party";
    # Update the dictionary with the split values;
    # Print the updated dictionary
    #  In case of an invalid number of people (zero or negative), "No one is joining for the party"/
    #  is expected as an output;
    #  If there are no people to split the bill (the number of friends is 0 or an invalid input),/
    #  output "No one is joining for the party";
else:

    print("No one is joining for the party")
