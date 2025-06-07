word_list = open('../supplemental/enable1.txt').read().splitlines()

# Problem 1: List where every word has a length of 6
six_letter_words = [word for word in word_list if len(word) == 6]
print("Six letter words:")
print(six_letter_words[:10])  # Print just the first 10 to avoid flooding the console
print(f"Total count: {len(six_letter_words)}")
print()

# Problem 2: Words that include the letter 'e'
words_with_e = [word for word in word_list if 'e' in word]
print("Words that include the letter 'e':")
print(words_with_e[:10])  # Print just the first 10
print(f"Total count: {len(words_with_e)}")
print()

# Problem 3: Words that do not include the letter 'e'
words_without_e = [word for word in word_list if 'e' not in word]
print("Words that do not include the letter 'e':")
print(words_without_e[:10])  # Print just the first 10
print(f"Total count: {len(words_without_e)}")
print()

# Problem 4: 5 letter words that contain the letter 'e', but not in the first position
five_letter_e_not_first = [word for word in word_list if len(word) == 5 and 'e' in word and word[0] != 'e']
print("Five letter words that contain the letter 'e', but not in the first position:")
print(five_letter_e_not_first[:10])  # Print just the first 10
print(f"Total count: {len(five_letter_e_not_first)}")