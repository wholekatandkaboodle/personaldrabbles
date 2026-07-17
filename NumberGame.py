
# 07/17/2026
# ---------- Number guesssing game
#K.D
i = 0
def checkGuess(n): #This function checks to see if the user's guess is either too high, too low, or in this case: 20.
    if (n > 20):
        print(str(n) + " is too high. Please guess again. ")
        askGuess()
    elif (n < 20):
        print(str(n) + " is too low. Please guess again. ")
        askGuess()
    else:
        print("Congratulations! You guessed right!")
        
        
def checkInput(n): #This function checks the input for any alphabetical characters. May update this to include other keyboard inputs such as operators, in the future.
    collectalpha = []
    for i in n:  # Credit to Cobrexus, (Stack Overflow 2020): https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python
        if (i.isalpha()):
            # Credit to Legolas Bloom (Stack Overflow 2019):  # Credit to Cobrexus, (Stack Overflow 2020): https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python
            collectalpha.append(i)
    if (len(collectalpha) == 0):
        collectalpha.clear()
        checkGuess(int(n))
    else:
        collectalpha.clear()
        askGuess()
        
def checkInputRec(n): #Recursive version of checkInput. Currently it is in progress and not called.
    collectalpha = []
    if (n[i].isalpha()):
        collectalpha.append(i)
        collectalpha.clear()
        
        askGuess()
    else:
        checkInputRec()
        

def askGuess(): #This function asks for the users input, then calls a function to validate user input (if it's just digits only or it's chaos instead).
    #collectalpha = []
    print("Enger your guess: ")
    n = input()
    
    checkInput(n)

    




def main():
    askGuess() #Start or program here!



main()
"""
    Since I have forgotten how arrays work in Python, here is credit:
    W3 Schools (Python Arrays, 2026): https://www.w3schools.com/python/python_arrays.asp
"""

