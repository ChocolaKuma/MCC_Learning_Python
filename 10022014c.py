##
##
##
##
text_file = open("read_it.txt", "r")
print (text_file.read(1))   #reads first char
print (text_file.read(7))
print (text_file.read())    #Reads whole File
print (text_file.readlines()) #Reads Everything ()Hiddenchars also
for line in text_file:   #for loop to print text
    print(line)



text_file = open("read_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line on new write 3\n")

text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
##
##
text_file = open("read_it.txt", "r")
print (text_file.readlines()) #Reads Everything ()Hiddenchars also makes
                                  #a list that breaks par line
##
text_file.close()


##Error handeling
##try:
##    num = float(input("Enter a number: "))
##except:
##    print ("Something went wrong!")
##
##


