"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

count = 0 #initailize Counter to 0
while count !=3: #Proram terminates only when the user get 3 correct in a row
    # Declare two random numbers number1 and number2
    number1 = random.randint(10,99)
    number2 = random.randint(10,99)
    # save question to ask user by concatenating number1 and number2
    question = "What is {} + {}?"
    # store the correct answer as answer
    answer = number1 + number2
    # Ask user to sum up the two numbers 
    print(question.format(number1,number2))
    try:#Error handling
        # Request for the user to type his/her answer as interger
        userAnswer = int(input("Your Answer: "))
        # a function to test if user answer if correct or not
        if answer==userAnswer:
            count +=1 #increement count by 1 for each correct answer
            print(f"Correct!, you've gotten {count} answer in a row.")
            if count == 3: #gets executed only when count user gets 3 correct in a row
                print("Congrats!, you've mastered Addition.")
        else:
            count = 0 #Reset count to 0 for each incorrect answer given
            print(f"Incorrect! The expected answer is {answer}.")
    except:#raise an error if user enters any input apart from integer
        print("Invild input, Kindly enter a Valid Number eg. 54. Decimals are not accepted.")