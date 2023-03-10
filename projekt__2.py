"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Katerina Kordiovska
email: kordiovskak@gmail.com
discord: Katerina K#9622
"""

import random

#Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0) ==== randint is an alias for randrange(start, stop+1).
start = 1000
stop = 9999
#computer_number = str(random.randint(start, stop))
#splitted_numbers = list(str(computer_number))
#unique_numbers = list()
        
#jedina funkce ktera mi zjisti jestli random generovane cislo od pc obsahuje duplicitni cifry        
def is_duplicate_pc_generated(number):
    list_of_numbers = list()
    for x in number:
        if x in list_of_numbers:
            return False
        else:
            list_of_numbers.append(x)
    return True


def is_duplicate(number):
    list_of_numbers = list()
    for x in number:
        if x in list_of_numbers:
            print("Number can not contain duplicated values")
            return False
        else:
            list_of_numbers.append(x)
    return True


#hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla

def correct_lenght(number) -> bool:
    if len(number) == 4:
        return True
    else:
        print("Has to be 4 digit number")
        return False

#print(correct_lenght(user_number))

#začínat nulou
def starts_with_zero(number) -> bool:
    if int(number[0]) == 0: 
        print("First number has tobe without zero.")
        return False
    else:
        return True

#print(starts_with_zero(user_number))

def is_numeric_number(number) -> bool:
    if number.isnumeric() == True:
        return True
    else:
        print("Has to be number.")
        return False

#print(is_numeric_number(user_number))

#fukce zjisti jestli je cislo unique = delka je 4, nema duplicitni cifry, je numeric cili obsahuje jen cisla a nezacina 0
def is_unique_number(number):
    return correct_lenght(number) and is_duplicate(number) and is_numeric_number(number) and starts_with_zero(number)

#print(is_unique_number(user_number))

#uhadnout cislo 

bulls_final = 0
#funkce ktera nam vrati pocet bulls a cows 
def cows_and_bulls(number1, number2):
    bulls = 0
    cows = 0
    
    computer_number = list(str(number1))
    user_number = list(str(number2))
    
    for x in user_number:
        if x in computer_number:
            cows = cows + 1

    for i in range(len(user_number)):
        if user_number[i] == computer_number[i]:
            bulls += 1
    
    cows = cows - bulls

    if cows == 1:
        result = str(cows) + " cow"
    else:       
        result = str(cows) + " cows"

    if bulls == 1:
        result1 = str(bulls) + " bull"
    else:
        result1 = str(bulls) + " bulls"

    result3 = str(result1)+", "+str(result)
    bulls_final = bulls
    return result3

def pc_generated_number():
    computer_number = str(random.randint(start, stop))
    while True:
        if is_duplicate_pc_generated(computer_number) == True:
            break
        else:
            computer_number = str(random.randint(start, stop))
            continue
    return computer_number

pc_number = pc_generated_number()

#Program pozdraví užitele a vypíše úvodní text
#print("PC NR: ",pc_number) #na testovani generovaneho cisla, zakomentovano
#print(is_unique_number(computer_number))

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")
user_number = input("Enter a number: ")
print("-----------------------------------------------")


counter = 1
answer = "y"
while answer != "n":
    if user_number == pc_number:
        print("Correct, you've guessed the right number in", counter, "guesses!")
        answer = input("Would you like another chance? [Y/N]")
        if answer.lower() == "n":
            print("Thank you for playing BULLS and COWS, come again :)")
            break
        else:
            pc_number = pc_generated_number()
            #print("NOVE PC NR: ",pc_number) #na testovani generovaneho cisla, zakomentovano
            user_number = input("Another guess: ")
            counter = 1
    elif is_unique_number(user_number) == True:
       counter += 1
       print(cows_and_bulls(user_number, pc_number))
       user_number = input("Another guess: ")
       continue
    else:
        user_number = input("Enter a correct number: ")
        continue
    
 
        


    

