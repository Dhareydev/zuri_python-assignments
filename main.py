# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
 
wordX = input("Enter your first word: ")
wordY = input("Enter your second word: ")

words_to_check = (find_anagram(wordX, wordY)) 

print(words_to_check)