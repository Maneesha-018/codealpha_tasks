#HANGMAN GAME
import random

words = ["mango","java","telecom","road","sunlight",]
word = random.choice(words)
guessed = ["_"]*len(word)
attempts = 6
guessed_letters = []

print("Welcome to a simple Hangman game")
print("Total Attempts = 6")
print("Guess the word")
print(" ".join(guessed))


while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()
    
    if not guess.isalpha():
        print("\n❗Please enter only letters")
        continue
    elif len(guess) !=1:
        print("\n❗Please enter only one letter")
        continue
    elif guess in guessed_letters:
        print("\n❗You've already guessed that letter")
        continue

    guessed_letters.append(guess)


    if guess in word:
        print("\n👍Correct")

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess

    else:
        attempts-=1
        print("\n👎Wrong,Attempts left: ",attempts)
    print(" ".join(guessed))


if "_" not in guessed:
    print("\n🎉🎉Congratulations,You Win")
    print("The word was",word)

elif attempts == 0:
    print("💔Oops,Better luck next time")   
    print("The word was",word)

