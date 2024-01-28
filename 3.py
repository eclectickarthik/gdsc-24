'''3) 	Input a sentence from the user and convert all the non-palindrome words into palindromes by concatenating the reverse of the word to itself.'''

def is_palindrome(word):
    return word == word[::-1]

def make_palindrome(word):
    return word + word[::-1]

def process_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if not is_palindrome(word):
            word = make_palindrome(word)
        result.append(word)
    return ' '.join(result)

user_input = input("Enter a sentence: ")
output = process_sentence(user_input)
print("Output:", output)