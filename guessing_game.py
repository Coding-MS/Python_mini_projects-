import random 

top_of_range = input ("Type a number for the limit: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
     if top_of_range <= 0: 
        print('The number must be larger than 0')
        quit()
     else:
        print('Invalid Input please enter a number next time.')
        quit()




random_number = random.randint(0, top_of_range)

while True: 
    user_guess = input ("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid input. Please enter a number")
        continue

    if user_guess == random_number 
        print ("Congratulations you have entered the Correct number! ")    
        break
    elif: user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

print ("You got it in" + str(guesses) + "guesses")

print(r)
