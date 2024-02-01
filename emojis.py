msg = input()
words = msg.split(' ')
emojis = {
    ':)': '😊',  # windows + .
    ':(': '😒'
}
text = ''
for word in words:
    text += emojis.get(word, word) + ' '
print(text)
