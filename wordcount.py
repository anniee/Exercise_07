from sys import argv 
import re
import string

script, textfile = argv

file_object = open(textfile)


def make_word_occurrence_dict(the_file):
    
    word_occurrence_dict = {}
    
    for each_line in file_object:

        line = each_line.rstrip()
        line = re.sub('[,.?!]', '', line)
        # TODO: the commented line below doesn't strip punctuation; figure out why?
        # line = string.replace(line, string.punctuation, '')
        line = line.split()

        for each in line:
            # This can be condensed to one line; do that after lunch?
            if each in word_occurrence_dict:
                word_count = word_occurrence_dict.get(each)
                word_occurrence_dict[each] = word_count + 1
            else:
                word_occurrence_dict[each] = 1

    return word_occurrence_dict

def print_word_counts(a_dictionary):
    """This can take the output of word_occurrence_dict and prettify it 
    to print out."""

    for key, value in a_dictionary.items():
        if value == 1:
            # print type(key)
            print 'The word "%s" appears in the file %d time.' % (key, value)
        else:
            print 'the word "%s" appears in the file %d times.' % (key, value)

words = make_word_occurrence_dict(file_object)
print_word_counts(words)