#Create a Dice roll game that uses import random and random.randint and will print a number between 1 and 6, also will ask the user if they want to roll again

#This is a function that can be called later 
def Dice_Roll():
    #This will import random
    import random
    #for will be used to make a loop, to be used to roll again
    for i in range(10) :
        #print "rolling"
        dice = random.randint(1,6)
    #print "roll"
        print(f"rolled : {dice}")
    #Roll_again is a variable that will be used to ask the user if they want to roll again
        Roll_again = input("Do you want to roll again? (y/N): ")
    #if and else will be used to check if the user in Roll_again typed y or n if they type y continue if n break
        if Roll_again == "y":
            continue
        else:
            break
#This will call the function Dice_Roll()
Dice_Roll()



