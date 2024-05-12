import re

def factorial(n):
    if n == 0:
        return "HelloWorld "
    else:
    	return n * factorial(n - 1)
	
number = 5
result = factorial(number)
print(f"The factorial of {number} Hello World(s) is {result}.")


def count_words(text):
    """
    This function counts the number of words in a string
    """
    # Split the text into a list of words by white spaces
    words = text.split()

    #Returns the length of the list of words
    return len(words)

#Example use
text = result
word_count = count_words(text)
print(f"The text has {word_count} words.")