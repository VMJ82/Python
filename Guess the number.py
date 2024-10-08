import random 
digits = list(range(10)) 
random.shuffle(digits)
computer=digits[:3]   # first 3 digits from random shuffle
print("random no generated ",computer)

def game():

#below code if need to shuffle on every run
    # digits = list(range(10)) 
    # random.shuffle(digits)
    # computer=digits[:3]   # first 3 digits from random shuffle
    # print(computer)

    guess = input("\n What is your guess? enter 3 digit number: ")      # gives string as output
    #print(guess) 
    userinput=list(guess)  
    userinput=[int(i) for i in userinput]   # list comprehention to convert list items from string to int
    #print(userinput)

    if computer== userinput:
        print("Match: You've guessed all correct numbers in the correct position")
        return  #exit()    #to exit the function as correct number is guessed
    else:
        positionmatch =0
        positionUnmatch=0
        for i in range(len(computer)):
            for j in range(len(userinput)):
                if computer[i]==userinput[j] and i==j:
                    positionmatch +=1
                elif computer[i]==userinput[j] and i!=j:
                    positionUnmatch +=1

        if positionmatch>0 and  positionUnmatch>0 :
            print(f"close: You've guessed {positionmatch} correct number in the correct position and {positionUnmatch} correct number in the wrong position ")    
        elif positionmatch>0 and  positionUnmatch==0:
            print(f"close: You've guessed {positionmatch} correct number in the correct position")
        elif positionmatch==0 and  positionUnmatch>0:
            print(f"close: You've guessed {positionUnmatch}  correct number but in the wrong position ")
        else:
            print("Nope: You haven't guess any of the numbers correctly") 
            
    
    newgame = input("Do you want to try again? Y/N ") 
    if newgame.upper() =='Y' : 
        game()
    else: 
        print("Thanks for playing, See you soon !")
        
game()    # main function call

##############################################################################################


#common students
"""
English = int(input("Number of students who have subscribed to the English newspaper : "))
print(English)

english_std = input(f"Enter the roll numbers of  {English} student for English newpaper comma separated  : ")
english_std =list(english_std.replace(",",""))
print(english_std )

French = int(input("Number of students who have subscribed to the French newspaper : "))
print(French)

french_std = input(f"Enter the roll numbers of  {French} student for English newpaper comma separated  : ")
french_std =list(french_std.replace(",",""))
print(french_std )
count=0
for i in english_std:
    for j in french_std:
        if i==j:
            count +=1
            break

print("No of students who has subscription to both :  ",count)
"""
        




