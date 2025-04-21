#Importing modules
import random
import time
import colorama

#opening text file
file = open("WordList.txt", "r")

#empty list for all the words
words = []

#importing words from text file
for i in range(0, 2308):
    word = file.readline().strip()
    words.append(word)


#choosing a random word from the list
chosen_word = list(words[random.randint(0, 2308)])

guesses = 6

#The main part of the program, the main character, the bigger fish to fry, the whole enchilada, the man the myth the legend, head honcho
while guesses != 0:
    guessed_word = input("What word do you guess?\n")
    #word for checking their input, it's a list for easier comparison of each letter, will be modified later on for that strange double rule
    checking_word = list(guessed_word)
    #word for checking input
    original_word = list(guessed_word)
    #error handling
    if guessed_word.strip().lower() not in words:
        print("Sorry! That word in invalid, please try again!\n")
        continue
    #Checking for the win condition
    elif guessed_word.strip().lower() in words:
        if checking_word == chosen_word:
            print("Congratulations! You won!")
            break
        else:
            output = ""
            for char in range(5):
                for thong in range(5):
                    if original_word[thong] == chosen_word[thong]:
                        duplicates = original_word[thong]
                        checking_word[thong] = "@" #Marking as correct
                        if duplicates in checking_word:
                            checking_word[checking_word.index(duplicates)] = "$"
                if checking_word[char] == "@":
                    output += colorama.Back.GREEN + original_word[char] + colorama.Style.RESET_ALL + " "
                    guesses -= 1
                elif checking_word[char] in chosen_word:
                    output += colorama.Back.YELLOW + original_word[char] + colorama.Style.RESET_ALL + " "
                    guesses -= 1
                else:
                    output += original_word[char] + " "
                    guesses -= 1
            print(output)
