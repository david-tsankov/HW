text = input("Enter a sentence, preferably with repeating words(do not use any punctuation symbols): ")
text=text.lower()
# print(text)
text_words=text.split(" ")

for word in text_words:
    print(f"{word:<10} - {text_words.count(word)}")
