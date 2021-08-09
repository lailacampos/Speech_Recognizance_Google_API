# Analyse text files and search for key words

# To-do:
# Get user input for keywords (separated by ';')
# Count the number of words the user wants to search
# Append words to a list
# Initialize a variable for counting the number of times the first word appears
# Keep count of lines in the text
# Search text for first word
# Return index and line it was found for beginning of first word
# Continue the search
# Return index and line of text for the next time the word is found
# Append the indexes in a list (or maybe a dictionary?):
# key = word, value = [count, line, index 1, index 2]
# return dictionary

# Separate functions:
# 1 - Get words from user. Return list with words.
# 4 - Append each line of text in a list
# 2 - Search text (list - one by one) and return index of string and line index
# 3 - Count number of times the word appears. Return count.


def separate_lines_of_text_file(complete_txt_path):
    with open(complete_txt_path) as file:
        lines = file.readlines()
    return lines


# Takes a list containing each line of a text and counts the number of occurrences of a given word
# Searches the list of words for the chosen word

# takes a text and a word
# splits text into list of words
# Iterates over each element and checks if word is in the list
#
def count_word(text_line, word):
    counts = {}
    line_words_list = text_line.split()
