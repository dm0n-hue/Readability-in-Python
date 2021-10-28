# Implement a program that computes the approximate grade level needed to comprehend some text

def main():
    text = input('Text: ')  # Gets input from user

    # functions to get the number of letters, words, and sentences
    char_count = int(count_l(text))
    word_count = int(count_w(text))
    sent_count = int(count_s(text))

    # Coleman-Liau index is returned and stored
    i = round(index(char_count, word_count, sent_count))

    # returns the grade level of the inputted text
    grade = grade_level(i)
    print(grade)

def count_l(l):
    char_count = 0

    # creates a list of only alphanumeric characters, ignoring special characters, spaces, and punctuation
    res = ''.join(e for e in l if e.isalnum())

    for i in res:
        char_count += 1

    return char_count

def count_w(w):
    word_count = 1

    # counts the number of spaces in the string
    word_count += w.count(' ')

    return word_count

def count_s(s):
    sent_count = 0

    # counts the number of sentences there are in the string based off these three characters
    sent_count += s.count('.')
    sent_count += s.count('!')
    sent_count += s.count('?')

    return sent_count

# Coleman-Liau index function
def index(l, w, s):
    letter = (l / w) * 100
    sentence = (s / w) * 100

    # Coleman-Liau index
    i = (0.0588 * letter) - (0.296 * sentence) - 15.8

    return i

def grade_level(index):
    statement = ''

    if index < 0:
        statement = 'Before Grade 1'
    elif (index > 1 and index <= 16):
        statement = 'Grade ' + str(index)
    else:
        statement = 'Grade 16+'

    return statement

main()