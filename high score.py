######Highscore.py
######Johnathan Hinebrook
######09-19-2014-10:48
######assignment
######make function 3-5
######corect logic
######vaildation
import time


scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]

#print (scores)
#2 and 0 is a matrix
#print (scores[2])
#print (scores[2][0])

score, name= ("Shemp",175)
entry = (score, name)
scores.append(entry)

score, name= ("John",9999)
#print(name)
#print(score)
entry = (score, name)
scores.append(entry)


print("============")
print("Name", " ", " ", "Score")
for entry in scores:
    #print("here 4")
    name, score = entry
    print(name, "\t", score)
print("============")

print("")
print("")
print("What action would you like to preform")
print("")
print("0=quit")
print("1=print player score ")
print("2=add players and scores")
print("3=sort")
print("4=remove item")
print("5=reverse list")


player=int(input())
while player !=None:
    #name = input()
    #score = input()
    #print("I am here1")
    player = int(input())

    if player == 0:
        #print("here 2")
        print("You have chosen option number 0")
        print("Program Now Exiting")
        time.sleep(2)
        print("Good Bye. Have a nice day!")
        break

    if player == 1:
        #print("here 3")
        print("You have chosen option number 1")
        print("")
        print("============")
        print("Name", " ", " ", "Score")
        for entry in scores:
            #print("here 4")
            name, score = entry
            print(name, "\t", score)
        print("============")
        print("")
        print("")
        print("What action would you like to preform")
        print("")
        print("0=quit")
        print("1=print player score ")
        print("2=add players and scores")
        print("3=sort")
        print("4=remove item")
        print("5=reverse list")

    if player == 2:
        #print("here5")
        print("Please type the players name.")
        name =input()
        print("Please write there score.")
        score = int(input())
        entry = (name, score)
        scores.append(entry)
        print("Name and score is being added to the list")
        print("")
        print("One moment please")
        time.sleep(2)
        print("List will now display")
        time.sleep(1)
        print("============")
        print("Name", " ", " ", "Score")
        for entry in scores:
            #print("here 4")
            name, score = entry
            print(name, "\t", score)
        print("============")
        print("")
        print("")
        print("What action would you like to preform")
        print("")
        print("0=quit")
        print("1=print player score ")
        print("2=add players and scores")
        print("3=sort")
        print("4=remove item")
        print("5=reverse list")

    if player == 3:
        #sort
        #print("here 6")
        print("You have chosen option number 3")
        print("list will now be sorted alphabetically")
        time.sleep(3)
        scores.sort()
        print("============")
        print("Name", " ", " ", "Score")
        for entry in scores:
            #print("here 4")
            name, score = entry
            print(name, "\t", score)
        print("============")
        print("")
        print("")
        print("What action would you like to preform")
        print("")
        print("0=quit")
        print("1=print player score ")
        print("2=add players and scores")
        print("3=sort")
        print("4=remove item")
        print("5=reverse list")
        
    if player == 4:
        #remove
        #print("here 7")
        print("You have chosen option number 4")
        print("Prepareing to make changes")
        time.sleep(2)
        print("Please type the players name. (Dont forget capitlization.)")
        name =input()
        print("Please write there score.")
        score = int(input())
        entry = (name, score)
        scores.remove(entry)
        print("Okay I'll work on that")
        time.sleep(5)
        print(name, "has been removed from list.")
        time.sleep(3)
        print("Prepareing to print new list.")
        time.sleep(3)
        print("============")
        print("Name", " ", " ", "Score")
        for entry in scores:
            #print("here 4")
            name, score = entry
            print(name, "\t", score)
        print("============")
        print("")
        print("")
        print("What action would you like to preform")
        print("")
        print("0=quit")
        print("1=print player score ")
        print("2=add players and scores")
        print("3=sort")
        print("4=remove item")
        print("5=reverse list")        



    if player == 5:
        #remove
        print("You have chosen option number 5")
        print("list will now be shown in reverse order")
        scores.reverse()
        time.sleep(2)
        print("============")
        print("Name", " ", " ", "Score")
        for entry in scores:
            #print("here 4")
            name, score = entry
            print(name, "\t", score)
        print("============")
        print("")
        print("")
        print("What action would you like to preform")
        print("")
        print("0=quit")
        print("1=print player score ")
        print("2=add players and scores")
        print("3=sort")
        print("4=remove item")
        print("5=reverse list")
