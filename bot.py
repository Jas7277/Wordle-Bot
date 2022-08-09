from random import choice
from os import system
from words import *
from time import sleep

def main():
    system("color 0a")
    running = True
    
    words = WORDS
    
    main_bot_loop(words, running)
        
        
def main_bot_loop(words, running = False):
    guess = 1
    while (running and guess <= 6):
        word = choice(words)
        word = word.lower()
        
        if guess == 1:
            if "j" in word or "q" in word or "z" in word or "x" in word:
                continue
            elif has_duplicate_letters(word):
                continue
            else:
                print(word)
        else:
            print(word)
        
        results = input('Enter the results in the format "xxxxx"\n')
        results = results.lower()
        
        if results == "ggggg":
            print("Congratulations! You win!")
            
            should_continue = input("Do you want to continue? Y/N\n")
            should_continue = should_continue.lower()
            
            if should_continue == "y":
                print("Restarting...")
                sleep(1)
                print("\n")
                main()
            elif should_continue == "n":
                break
        elif results == "restart":
            print("Restarting...")
            sleep(1)
            print("\n")
            main()
        
        results = [char.strip() for char in results]
        
        words = update_word_list(words, word, results)
        
        guess += 1
        
def has_duplicate_letters(word):
    return not len(set(word)) == len(word)

def update_word_list(words, word, results):
    words.remove(word)
    
    for i in range(len(results)):
        if results[i] == "x":
            words = [x for x in words if word[i] not in x]
        
        if results[i] == "g":
            words = [x for x in words if word[i] == x[i]]
            
        if results[i] == "y":
            words = [x for x in words if word[i] != x[i]]
            words = [x for x in words if word[i] in x]
    
    return words

if __name__ == "__main__":
    main()
    system("pause")