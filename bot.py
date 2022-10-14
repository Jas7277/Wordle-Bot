from random import choice
from os import system
from time import sleep
from words import *

def main():
    system("color 0a")
    
    guess = 1
    
    words = WORDS
    
    while guess <= 6:
        word = choice(words)
        
        if guess == 1:
            word = choice(["adept", "clamp", "plaid", "scalp", "clasp", "depot", "print", "recap", "strap", "tramp",
                           "slice", "tried", "crane", "leant", "close", "trice", "train", "slate", "lance", "trace", "other", "tales"])
        else:
            scores = word_score(words)
            maxValue = max(scores)
            
            word = words[scores.index(maxValue)]
            
        print(word)
        
        i = input("Enter the results in the format 'xxxxx'\n")
        i = i.lower()
        
        words = update_word_list(words, word, i)
        
        guess += 1
        
def update_word_list(words, word, result):
    words.remove(word)
    
    guessed = [*word]
    results = [*result]
    
    
    for i in range(len(results)):
        if results[i] == "g":
            words = [x for x in words if guessed[i] == x[i]]
        elif results[i] == "y":
            words = [x for x in words if guessed[i] in x]
            words = [x for x in words if guessed[i] != x[i]]
        elif results[i] == "x":
            if "g" in results:
                if guessed[i] == guessed[results.index("g")]:
                    continue
            elif "y" in results:
                if guessed[i] == guessed[results.index("y")]:
                    continue
                
            words = [x for x in words if guessed[i] not in x]
            
    return words

def word_score(words):
    totals = []
    
    for word in words:
        value = 0
        for i in range(len(word)):
            if word[i] in words:
                value += 1
                
        totals.append(value)
        
    return totals

if __name__ == "__main__":
    main()