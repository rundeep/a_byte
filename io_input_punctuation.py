import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    # Modifying text into Scriptio Continua

    print 'Eliminating any spaces, tabs, newlines and so on:'
    text = ''.join(text.split())
    print text

    print 'Eliminating any punctuation characters:'
    for c in string.punctuation:
        text = text.replace(c,'')
    print text

    print 'Convert all cased characters to lowercase:'
    text = text.lower()
    print text

    return text == reverse(text)

something = raw_input('Enter text: ')
if is_palindrome(something):
    print 'Yes, it is a palindrome'
else:
    print 'No, it is not a palindrome'
