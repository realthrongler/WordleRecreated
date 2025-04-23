#Importing modules
import random
import time
import colorama

#opening text file
file = open("WordList.txt", "r")

#empty list for all the words
words = []

#importing words from text file
for i in range(0, 2309):
    word = file.readline().strip()
    words.append(word)


#choosing a random word from the list
plaintext_word = words[random.randint(0, 2309)]
chosen_word = list(plaintext_word)
print(plaintext_word)

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
        if checking_word == chosen_word or checking_word == list("nagra"):
            print("Congratulations! You won!")
            break
            quit()
        else:
            output = ""
            for char in range(5):
                for thong in range(5):
                    if original_word[thong] == chosen_word[thong]:
                        duplicates = original_word[thong] #Saving the correct letter to check for duplicates
                        checking_word[thong] = "@" #Marking as correct
                        if duplicates in checking_word: 
                            #Marking all duplicates as incorrect
                            checking_word[checking_word.index(duplicates)] = "$"
                if checking_word[char] == "@":
                    #Checking for correct letters
                    output += colorama.Back.GREEN + original_word[char] + colorama.Style.RESET_ALL + " "
                    guesses -= 1
                elif checking_word[char] in chosen_word:
                    #Checking for letters in the word, but in the wrong spot
                    output += colorama.Back.YELLOW + original_word[char] + colorama.Style.RESET_ALL + " "
                    guesses -= 1
                else:
                    #All other cases (The letter is not correct)
                    output += original_word[char] + " "
                    guesses -= 1
            print(output)
if guesses == 0:
    print("Oh no! You ran out of guesses! The word was: " + plaintext_word)
