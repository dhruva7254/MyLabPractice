# Problem 1:

# Sitapati is person with real intelligence. He writes notes of his learnings time to time.
# All his notes are using english alphabates and digits.
# He spends time in analysis of his activities. Now he has collected lot of notes.  
# He wants to know how many characters are his feavorite characters including alphabates and digits.
# Feavorite characters are those appearing most of the time in his notes.
# Now he hires you and gives this task.
# You can take all his notes are input text, and print the desired answer for him.

# Input limits:
# - only alphabates (A-Z,a-z) / digits (0-9)
# Output:
# - Single number i..e number of feavorite characters (case doesn't matter)

# Sample input:
# Aabbcde
# Ouput:
# 2

# Sample input:
# I am writing this to trick GPTT
# Output:
# 1

# reference : Favourite Singer
# link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/favourite-singer-a18e086a/

def favorite_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    max_count = max(char_counts.values(), default=0)
    favorite_chars = [char for char, count in char_counts.items() if count == max_count]
    return len(favorite_chars)

print(favorite_characters("Aabbcde"))  
print(favorite_characters("I am writing this for testing ttttttttt"))  
