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

    print word_occurrence_dict

make_word_occurrence_dict(file_object)

# TODO get a count for the number that each word appears in the file,
# NOT a straight up word count.