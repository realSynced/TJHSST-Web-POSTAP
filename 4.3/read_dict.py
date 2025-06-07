word_list = open('../supplemental/enable1.txt').read().splitlines()

#1 a list where every word has a length of 6

six_letter_word_list = [word for word in word_list if len(word) == 6]
print("1. A list where every word has a length of 6:")
print(six_letter_word_list[:10]) 

#2 words that include the letter 'e'
words_with_e = [word for word in word_list if 'e' in word]
print("\n2. Words that include the letter 'e':")
print(words_with_e[:10])

#3 words that do not include the letter 'e'
words_without_e = [word for word in word_list if 'e' not in word]
print("\n3. Words that do not include the letter 'e':")
print(words_without_e[:10])

#4 5 letter words that contain the letter e, but not in the first position
e_is_not_first = [word for word in word_list if len(word) == 5 and 'e' in word and word[0] != 'e']
print("\n4. 5 letter words that contain the letter 'e', but not in the first position:")
print(e_is_not_first[:10])
