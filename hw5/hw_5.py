##John Hinebrook
##HW 5
##9
##Python 3.2
##3 Opts guess_num_rand, Tuup_list, Story


def fun1():
    """Guess the Number"""
    import random
    guessesTaken = 0
    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 20)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    while guessesTaken < 6:
        print('Take a guess.') # There are four spaces in front of print.
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low.') # There are eight spaces in front of print.

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)


def fun2():
    import time
    """Tuups and lists"""
##    print('funWithTuups has been selected')
    print('What would you like to do')
    print('')
    print('(1)add(2)print(3)Delete list(0)Break')
    player2 = int(input())
    while player2 !=None:
        player2 = int(input())
        print('(1)add(2)print(3)Delete list')
        if player2 == 1:
            print('Okay restarting')
            text_file = open("tuup.txt", "a+")
            print('Give me some thing')
            listin = input()          
            text_file.write(listin)
            text_file.write("\t")

            
####################################
            
            print('Heres your list')
            text_file = open("tuup.txt", "r")


            for line in text_file:   #for loop to print text
                print(line)           
        elif player2 == 2:
            print('Okay loading last session')
            time.sleep(2)
            print('List now loaded')
            text_file = open("tuup.txt", "r")
            for line in text_file:   #for loop to print text
                print(line) 
            
        elif player2 == 3:
            print('deleting previous data')
            text_file = open("tuup.txt", "w")
            lines = [""]
            text_file.writelines(lines)        
        elif player2 >=4:
            print('Quit trying to break it')
        elif player2 == 0:
            print('Breaking')
            text_file.close()
            break
            

def fun3():
    """storyTime"""
    print('You have chosen story')
    text_file = open("story.txt", "r")

    print (text_file.readlines(1))
    import time
    time.sleep(1)
    print (text_file.readlines(2))
    time.sleep(1)
    print (text_file.readlines(3))
    time.sleep(1)
    print (text_file.readlines(4))
    time.sleep(1)
    print (text_file.readlines(5))
    time.sleep(1)
    print (text_file.readlines(6))
    text_file.close()

    
def fruityloops():
    import time
##    print('You have chosen fruittlyLoops')
    player=int(input())
    while player !=None:
        player = int(input())
        if player == 0:
            print('You have chose 0 Break')
            time.sleep(1)
            break
        elif player == 1:
            print('You have chosen 1 Guess Number')
            fun1()
            Menu()
        elif player == 2:
            print('You have chosen 2 Lists and Tuples')
            fun2()
            Menu()
        elif player == 3:
            print('Thou have chosen 3 Story')
            fun3()
            Menu()
        elif player >= 4:
            print('Unprogramed option Please try again')
            Menu()



def Menu():
    text_file = open("menu.txt", "r")
    for line in text_file:   #for loop to print text
        print(line)
    
    

def main():
##    print('Main Has started')
    Menu()
    fruityloops()
##    fun2()
    
main()
    






