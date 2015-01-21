from sys import argv 

script, textfile = argv

file_object = open(textfile)

counter = 0
for each_line in file_object:
    line = each_line.rstrip()
    line_words = line.split(" ")

    counter = counter + len(line_words)
print counter

