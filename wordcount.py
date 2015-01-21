from sys import argv 

script, textfile = argv

file_object = open(textfile)



def make_word_occurrence_dict(the_file):
    
    word_occurrence_dict = {}
    
    for each_line in file_object:
        line = each_line.rstrip()
        line = line.split(" ")

        for each in line:
            if each in word_occurrence_dict:
                word_count = word_occurrence_dict.get(each)
                word_occurrence_dict[each] = word_count + 1
            else:
                word_occurrence_dict[each] = 1

    return word_occurrence_dict

def print_word_counts(a_dictionary):
    """This can take the output of word_occurrence_dict and prettify it 
    to print out."""

    for each_item in a_dictionary.items():
        print 'the word %s appears in the file %s times.' % each_item

words = make_word_occurrence_dict(file_object)
print_word_counts(words)

# TODO get a count for the number that each word appears in the file,
# NOT a straight up word count.