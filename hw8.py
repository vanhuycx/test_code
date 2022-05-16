#
#
import random


def random_number_file_create(min, max, filename, entries):
    file = open(filename, 'w')
    for i in range(20):
        number = str(random.randint(min, max))
        file.write(number + '\n')
    file.close()
    return file


def lines_print(filename):
    file = open(filename, 'r')
    for line in file:
        print(line)
    file.close()


def lines_count(filename):
    count = 0
    for line in filename:
        count += 1
    return count


def total_numbers_in_file(filename):
    total = 0
    file = open(filename, 'r')
    for line in file:
        number = int(line.strip())

        total += number

    return total


FILENAME = "numbers.txt"
random.seed(83)
random_number_file_create(50, 100, FILENAME, 20)
lines_print(FILENAME)
print()

entries = lines_count(FILENAME)
total = total_numbers_in_file(FILENAME)
average = round(total/entries)

print("Entries:", entries)
print("Total:", total)
print("Average:", average)
