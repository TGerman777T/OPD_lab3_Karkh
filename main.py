from flask import Flask
import codecs

app = Flask(__name__)

@app.route('/')
def find_most_common_word():
    with codecs.open('text1.txt', 'r', encoding='utf-8') as file:
        words = file.read()
        words1 = words.split()
        word_count = {}
        for word in words1:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common_word = max(word_count, key=word_count.get)
        return f'Самое часто повторяющееся слово: \"{most_common_word}\"'

if __name__ == '__main__':
    app.run()

#http://127.0.0.1:5000