#Dictionary: Count word occurrences in a given text and store them in a dictionary.

original_text = "This is Masum Jia. Masum is a student. Jia is also a student."

spllited_words = original_text.split()

word_count = {}

for word in word_count:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)