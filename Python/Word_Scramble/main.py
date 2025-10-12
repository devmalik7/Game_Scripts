import random

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

words = ["python", "developer", "programming", "challenge"]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)

attempts = 3
while attempts > 0:
   guess = input("Guess the word: ").lower()
   if guess == word:
       print("Correct! ????")
       break
   else:
       attempts -= 1
       print(f"Wrong! {attempts} attempts left.")

if attempts == 0:
   print(f"Game over! The correct word was {word}.")