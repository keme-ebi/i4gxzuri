# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(first, second):
    # [assignment] Add your code here
    first = input("input first word: ")
    second = input("input second word: ")
    
    if (sorted(first) == sorted(second)):
        print("True")
    else:
        print("False")
    return True


first = "plead"
second = "paled"
find_anagrams(first, second)
