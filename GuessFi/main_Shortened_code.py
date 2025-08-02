import random
print("Welcome to Snake, Water, Gun game!")
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

# Buy now we have 2 number (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw!")

else:
    '''
    #if(computer == -1 and you == 1):
     #print("You win!")
     #print("Computer chose water")

    #elif(computer == -1 and you == 0):
      #print("You lose!")
      #print("Computer chose water")

    #elif(computer == 1 and you == 0):
      #print("You win!")
      #print("Computer chose snake")

    #elif(computer == 1 and you == -1):
      #print("You lose!")
      #print("Computer chose snake")

    #elif(computer == 0 and you == 1):
      #print("You lose!")
      #print("Computer chose Gun")

    #elif(computer == 0 and you == -1):
      #print("You win!")
      #print("Computer chose Gun")

    #else:
      #print("Something went wrong")

      This below logic is written on the basis of the valueof computer - You !
      '''
    
    if((computer - you) == -1 or (computer - you) == 2):
        print("You win!")
    else:
        print("You lose!")

