## 20.8.3
essay_content = input("Essay = ")

word_counts = {}

for word in essay_content:
    word_counts[word] = word_counts.get(word, 0)

print(word_counts)
