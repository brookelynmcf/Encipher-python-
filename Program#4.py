########################################################################
##
## CS 101
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM :
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def get_answer(question, choice1, choice2, choice3):
    while True:
        final_choice = input(question)
        final_choice = final_choice.lower()
        if final_choice in [choice1, choice2, choice3]:
            return final_choice
        else:
            print("Please enter one of the presented choices.")

def get_file(userFile, read_write):
    while True:
        file_given = input(userFile)
        try:
            realFile = open(file_given, read_write)
        except FileNotFoundError:
            print("File name invalid, please try again.")
        else:
            return realFile

def jumble_file(userFile):
    for line in userFile:
        no_wht_spcs = line.strip("\n")
        even_char = no_wht_spcs[0::2]
        odd_char = no_wht_spcs[1::2]
        cncat_char  = even_char + odd_char
        print(cncat_char, file = outputFile)

def unjumble(scramblase):
    for item in range(ramblase):
        no_wht_spcs = line.strip("\n")
        evnchar = no_wht_spcs



#test_txt = open("test(program#4).txt","r")




#question = int(input("What would you like to do?\n 1.)Encipher\n 2.)Decipher\n 3.)Quit"))

while True:

    user_choice = get_answer("What would you like to do?\n 1.)Encipher\n 2.)Decipher\n 3.)Quit\n", "1", "2", "3")

    if user_choice == "1":
        userFile = get_file("Input the file you would like to encipher.", "r")
        outputFile = get_file("Choose a file to write to." , "w")
        jumble_file(userFile)


        #for line in userFile:
            #no_wht_spaces = line.strip()
        #put into jumble function later
        #print("you picked one")
        userFile.close()
        outputFile.close()
        print("welcome to the jumble")
    elif user_choice == "2":
        scramblase = get_file(userFile)


        print("you picked two")
    elif user_choice == "3":
        print("you picked three")



