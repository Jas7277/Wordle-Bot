from random import choice
from os import system
from words import *
from time import sleep

def main():
    system("color 0a")
    running = True
    
    words = WORDS
    
    i = input("Have you already made a first guess? y/n ")
    i = i.lower()
    
    if i == "y":
        words, guess = mid_game_join()
        main_bot_loop(guess, words, running)
    elif i == "n":
        main_bot_loop(1, words, running)
    else:
        main()
        
    
def mid_game_join():
    words_guessed = input("Enter each individual word you've already guessed with a space in between them. ")
    words_guessed = words_guessed.lower()
    
    guessed = words_guessed.split(" ")
    
    for i in range(len(guessed)):
        if guessed[i] not in WORDS:
            WORDS.append(guessed[i])
            
    words_results = input("Enter the results of each word you've already guessed, with a space in between them. ")
    
    results_of_words = words_results.split(" ")
    
    words = WORDS
    
    for i in range(len(guessed)):
        words.remove(guessed[i])
        words = update_word_list(words, guessed[i], results_of_words[i])
        
    return words, len(guessed) + 1
    
def main_bot_loop(guess, words, running = False):
    new_word = False
    last_results = None
    
    old_words = WORDS
    
    while (running and guess <= 6):
        try:
            word = choice(words)
        except IndexError:
            print("Something went wrong, there are no remaining words in the list! Please enter the solution so that it may be added to the list of words.")
            i = input("Word to add: ")
            i = i.lower()
            WORDS.append(i)
            break
        
        if guess == 1:
            word = choice(["adept", "clamp", "plaid", "scalp", "clasp", "depot", "print", "recap", "strap", "tramp",
                           "slice", "tried", "crane", "leant", "close", "trice", "train", "slate", "lance", "trace"])
            print(word)
            words.remove(word)
        elif new_word:
            word = choice(old_words)
            print(word)
            words.remove(word)
        else:
            scores = calculate_word_scores(words)
            score = calculate_word_score(words, word)
            
            if score == max(scores):
                should_print_word = True
            else:
                should_print_word = False
                
            if should_print_word:
                print(word)
                words.remove(word)
            else:
                continue
        
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
    for i in range(len(results)):
        if results[i] == "x":
            words = [x for x in words if word[i] not in x]
        
        if results[i] == "g":
            words = [x for x in words if word[i] == x[i]]
            
        if results[i] == "y":
            words = [x for x in words if word[i] != x[i]]
            words = [x for x in words if word[i] in x]
    
    return words

def calculate_word_scores(words):
    scores = [] 
    
    for i in range(len(words)):
        score = 0 
        
        for j in range(len(words[i])):
            if words[i][j] in words:
                score += 1
        scores.append(score)
        
    return scores

def calculate_word_score(words, word):
    score = 0
    
    for i in range(len(word)):
        if word[i] in words:
            score += 1
            
    return score

if __name__ == "__main__":
    main()
    system("pause")