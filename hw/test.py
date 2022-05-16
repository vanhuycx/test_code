# /usr/bin/python3
# This script reads the file, count the words, adad,dad


# This function try to create a file object for reading and return the file object
def open_file_read(filename):
    try:
        file=open(filename,'r')
        return file
    except:
        print('Cannot open the file.')

# This...daw.d...d.adw.
def count_words(file):
    count = 0
    for line in file:
        word_list = line.split()
        count += len(word_list)
    return count

# THis dawdaawdawd
def word_set_create(file):
    word_set = set()
    for line in file:
        word_list = line.split()
        for word in word_list:
            word_set.add(word.lower())
    return word_set

# thidaiwd
def different_words(set_1,set_2):
    return set_1.symmetric_difference(set_2) 

#hufhaufdw
def common_words(set_1,set_2):
    return set_1.intersection(set_2)

filename_1 = "gettysburg.txt"
filename_2 = "gettysburg_hay.txt"
file_1     = open_file_read(filename_1)
file_2     = open_file_read(filename_2)
count_1 = count_words(file_1)
print(count_1)
count_2 = count_words(file_2)
print(count_2)
print()

file_1     = open_file_read(filename_1)
file_2     = open_file_read(filename_2)
word_set_1 = word_set_create(file_1)
word_set_2 = word_set_create(file_2)

print("Filename            Words  Unique Words")
print("---------------------------------------")
print(filename_1 + "      " + str(count_1) + "    " + str(len(word_set_1)))
print(filename_2 + "  " + str(count_2) + "    " + str(len(word_set_2)))
print()

different_word_set = different_words(word_set_1, word_set_2)
print("The two files have", len(different_word_set), "words in one file, but not the other" )
for word in sorted(different_word_set):
     print(word)
print()

common_words_set = common_words(word_set_1, word_set_2)

print("The two files have", len(common_words_set), "words in common")

