
# 07/17/2026
# ---------- Number guesssing game
#K.D
i = 0
def checkGuess(n):
    if (n > 20):
        print(str(n) + " is too high. Please guess again. ")
        askGuess()
    elif (n < 20):
        print(str(n) + " is too low. Please guess again. ")
        askGuess()
    else:
        print("Congratulations! You guessed right!")
        
        
def checkInput(n):
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
        
def checkInputRec(n):
    collectalpha = []
    if (n[i].isalpha()):
        collectalpha.append(i)
        collectalpha.clear()
        
        askGuess()
    else:
        checkInputRec()
        

def askGuess():
    #collectalpha = []
    print("Enger your guess: ")
    n = input()
    
    checkInput(n)

    




def main():
    askGuess()
    
    #checkGuess(n)
    
    #print(n)



main()
"""
    Since I have forgotten how arrays work in Python, here is credit:
    W3 Schools (Python Arrays, 2026): https://www.w3schools.com/python/python_arrays.asp
"""

