word1 = input("Enter word: ")
word2 = input("Enter word: ")

word1_list = list(word1)
word1_list.sort()
word2_list = list(word2)
word2_list.sort()

if word1_list == word2_list:
    print(word1 + ' and ' + word2 + ' are anagrams')
else:
    print(word1 + ' and ' + word2 + ' are not anagrams')
