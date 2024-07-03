# This program recieves three exam points from the user between 0 to 100 and calculates the avarage exam points.

""" Planning
From the beginning I thought of possible inputs recieved from the user. I wanted to check if the input is valid.
To check if the input is valid, I need to check if the input is between 0 to 100 (the available points for an exam). 
I need to check all the inputs, so to avoid repeating the same if statement multiple times, I created a function called handleInput.
"""

def handlePointsInput(examPoints): 
    if examPoints < 0 or examPoints > 100:
        print("Felaktig inmatning. Gör om gör rätt :)")
        exit()
    else: 
        return examPoints

firstExamPoints =int(input("Skriv in poängen från första provet (0-100): ")) 
handlePointsInput(firstExamPoints)

secondExamPoints =int(input("Skriv in poängen från andra provet (0-100): "))
handlePointsInput(secondExamPoints)

thirdExamPoints = int(input("Skriv in poängen från tredje provet (0-100): "))
handlePointsInput(thirdExamPoints)

totalPoints = firstExamPoints + secondExamPoints + thirdExamPoints
avaragePoints = totalPoints / 3 

if avaragePoints >= 90:
    print("Medelvärdet är {}. Bra jobbat!".format(avaragePoints))
else: 
    print("Medelvärdet är {}".format(avaragePoints))


