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
print(chosen_word) #TESTING

guesses = 6

#The main part of the program, the main character, the bigger fish to fry, the whole enchilada, the man the myth the legend, head honcho
while guesses != 0:
    guessed_word = input("What word do you guess?\n")
    #word for checking their input, it's a list for easier comparison of each letter
    checking_word = list(guessed_word)

    #error handling
    if guessed_word.strip().lower() not in words:
        print("Sorry! That word in invalid, please try again!\n")
        continue
    elif guessed_word.strip().lower() in words:
        if checking_word == chosen_word:
            print("Congratulations! You won!")
            break
        else:
            for char in range(5):
                if checking_word[char] == chosen_word[char]:
                    print(colorama.Back.GREEN + checking_word[char] + colorama.Style.RESET_ALL + " ")
                    guesses -= 1
                elif checking_word[char] in chosen_word:
                    print(colorama.Back.YELLOW + checking_word[char] + colorama.Style.RESET_ALL + " ")
                    guesses -= 1
                else:
                    print(checking_word[char] + " ")
                    guesses -= 1
                
