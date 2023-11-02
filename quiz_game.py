print ("Welcome to my quiz!")

playing = input("Do you want to play the game? ")
score = 0 

if playing,lower() != "yes": 
    quit()

print ("Okay! You have bravely taken the next step! Let the game begin!")

answer = input ("What does CPU Stand for? ").lower()
if answer == "central processing unit ":
    print ("Correct")
    score += 1
else: 
    print ("Answer is Incorrect!")
    score -= 1


answer = input ("What does RAM stand for? ").lower()
if answer == "random access memory":
    print ("Correct")
    score += 1
else: 
    print ("Answer is Incorrect!")
    score -= 1 


answer = input ("What are animals with a backbone called? ").lower()
if answer == "Vertebrate ":
    print ("Correct")
    score += 
else: 
    print ("Answer is Incorrect!")
    score -= 1 


answer = input ("What are Force is responsible keeping planets in orbit? ").lower()
if answer == "gravity ":
    print ("Correct")
    score += 3
else: 
    print ("Answer is Incorrect!")
    score -= 1 

print ("You got " + str(score) + "questions correct!")
print ("You got " + str((score / 4 )*100)+"%")

