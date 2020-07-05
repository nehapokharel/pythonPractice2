def is_palindrome(word):
    rev_word = word[::-1]
    if rev_word == word:
        return True
    else:
        return False

w = input("Enter word: ")
p = is_palindrome(w)
if p:
    print(w + " is a palindrome")
else:
    print(w + " is not a palindrome")

