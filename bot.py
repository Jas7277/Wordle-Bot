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
    new_word = False
    last_results = None
    
    old_words = words
    
    guess = 1
    while (running and guess <= 6):
        try:
            word = choice(words)
        except IndexError():
            print("Something went wrong, there are no remaining words in the list! Please enter the solution so that it may be added to the list of words.")
            i = input("Word to add: ")
            i = i.lower()
            WORDS.append(i)
            break
        
        word = word.lower()
        
        if guess == 1:
            word = choice(["adept", "clamp", "plaid", "scalp", "clasp", "depot", "print", "recap", "strap", "tramp",
                           "slice", "tried", "crane", "leant", "close", "trice", "train", "slate", "lance", "trace"])
            print(word)
        elif new_word:
            word = choice(old_words)
            print(word)
        else:
            scores = []
            
            for i in range(len(words)):
                scores.append(calculate_word_score(words, word, i))
                
            score = max(scores)
            
            for i in range(len(scores)):
                if scores[i] == score:
                    word = words[i]
            
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
        elif results == "-----":
            print("Removing {} from the word list...".format(word))
            WORDS.remove(word)
            words.remove(word)
            old_words.remove(word)
            sleep(0.5)
            continue
        
        results = [char.strip() for char in results]
        
        if last_results != results:
            words = update_word_list(words, word, results)
            new_word = False
        else:
            new_word = True
        
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

def calculate_word_score(words, word, index):
    score = 0
    scores = []
    
    for i in range(len(word)):
        score = 0
        for j in range(len(words)):
            if word[i] in words[j]:
                score += 1
        scores.append(score)
        
    score = sum(scores)
                
    return score

if __name__ == "__main__":
    main()
    system("pause")