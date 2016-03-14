########################################################################
##
## CS 101
## Program #4
## Name Brooke McFarland
## Email blmz99@mail.umkc.edu
##
## PROBLEM : Given an origional text file, transcribe the file so that the message is unreadable. Also, a file must be able to be opened to untranscribe the file.
##          when untranscribed, the untranscribed file must be the same as the origional file.
##
## ALGORITHM :
##
##1.)	Import file
##2.)	function
##      a.	Ask user input
##         i.	Transpose file
##         ii.	Untranspose file
##         iii.	Quit
##1.	If quit:
##      a.	Break
##3.)	function
##      a.	User input for file name
##          i.	Try
##          ii.	Except FileNotFoundError:
## 1.	Print(“File” File_name, “not found. Please try another file name.”)
##      b.	User input for file name they want write to
##           i.	Try
##           ii.	Except:
## 1.	Print(“invalid input. Please try again)
## 4.)	Transpose
##      a.	Prompt for name of file to write too
##           i.	Try:
##           ii.	Except:
## 1.	Print(“invalid input”)
##      b.	Iterate over file line by line
##           i.	 Strip white space
##           ii.	Slice string [0::2]
##           iii.	Slice string [ 1:: 2]
##            iv.	Concatenate both slices to transpose file
##            v.	Print concatenated slices
##5.)	Un-transpose
##       a.	Iterate over file
##           i.	Isolate even characters [0::2]
##           ii.	Isolate odd characters [1::2]
##           iii.	Concatenate the first character of the even string with the first character of the odd string
##            v.	Print Un-transposed string
##           vi.	Write Un-   transposed string to user indicated file
##
##
## ERROR HANDLING:
##      Try and except error handling for FileNotFoundError errors.
##      error message printed for invalid input when prompted what process the user would like to execute.
## OTHER COMMENTS:
##      "I fart in your general direction. Your mother was a hamster and your father smelled of elderberries!" - Monty Python
##
########################################################################
def get_answer(question, choice1, choice2, choice3):
    """get user input and pass it through with three different options for the user.Error handling if user doesn't input 1,2,or 3 for their answer"""
    while True:
        final_choice = input(question)#user's answer is passed through and checked if response is valid or not.
        final_choice = final_choice.lower()
        if final_choice in [choice1, choice2, choice3]:
            return final_choice
        else:
            print("Please enter one of the presented choices of 1,2 or 3.")#prompt to tell user incorrect input was entered

def get_file(userFile, read_write):
    """get user input for file to open, two parameters(file name and if the user is reading or writing file)"""
    while True:
        file_given = input(userFile)#if user input does not throw a FileNotFoundError
        try:
            realFile = open(file_given, read_write)
        except FileNotFoundError:
            print("File name invalid, please try again.")#if user input does throw an error, warning is printed
        else:
            return realFile#when loop is completed and no error has occured, the file the user entered is returned

def jumble_file(userFile):
    """the user file that has been opened is iterated over and sliced. The even characters are concatonated at the start of a new string, and the odd characters are concatonated at the end."""
    for line in userFile:#file iterated over with the white space stripped and sliced
        no_wht_spcs = line.strip("\n")
        even_char = no_wht_spcs[0::2]
        odd_char = no_wht_spcs[1::2]
        cncat_char = even_char + odd_char
        print(cncat_char, file=outputFile)#resulting concatination is printed and written out to a new folder

def unjumble(dec_userFile):
    """the user's file is untranscribed and printed to another new file"""
    for line in dec_userFile:
        no_wht_spcs = line.strip("\n")#the file is iterrated over and the white spaces are stripped
        result = ""

        if (len(no_wht_spcs)%2 ==0):#if statement for strings with an even number of intergers
            evn_char = no_wht_spcs[0:(int(len(no_wht_spcs)/2))]#slice of string starting from begining of string and stopping at half the length of the string
            od_char = no_wht_spcs[-1:(int(len(no_wht_spcs)/2)-1):-1][::-1]#slice of string starting at the last character and reversing the string, then unreversing the s
        else:
            evn_char = no_wht_spcs[0:(int(len(no_wht_spcs)/2)+1)]#if string has odd number of characters, one character is added to the slice so that it prints correctly
            od_char = no_wht_spcs[-1:(int(len(no_wht_spcs)/2)):-1][::-1]#this slice remains the same


        for index in range(len(evn_char)):
            result += evn_char[index]
            if index < len(od_char) or (len(no_wht_spcs)%2==0):#prevents and error when the length of the two strings are not the same. The evn_char will always be longer when the number of characters is odd.
                result += od_char[index]
        print(result, file= dec_outputFile)#prints the resulting string and creates a file in the same space as the program is found.


while True:
    result = ""

    user_choice = get_answer("What would you like to do?\n 1.)Transpose\n 2.)Un transpose\n 3.)Quit\n", "1", "2", "3")

    if user_choice == "1":
        userFile = get_file("Input the file you would like to encipher.", "r")#gets user input for the file they would like to transcribe and assigning r to read the file
        outputFile = get_file("Choose a file to write to." , "w")#gets user input for the file the user would like to write, assign w to write out to a file
        jumble_file(userFile)#pass user file through the jumble function
        userFile.close()#closing file
        outputFile.close()#closing file
        print("welcome to the jumble")

    elif user_choice == "2":
        dec_userFile = get_file("Input the file you would like to decipher.","r")#get user input and assign r to indicate read file
        dec_outputFile = get_file("Choose a file to write to.","w")#get user input and assign w to write to file
        unjumble(dec_userFile)#pass dec_userFile through the unjumble function
        dec_userFile.close()#close file
        dec_outputFile.close()#close file
        print("george, george, george of the jumble!")

    elif user_choice == "3":#if user chooses to quit the program, the break will end the program
        break



