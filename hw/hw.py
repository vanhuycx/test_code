# # hw3
# fahrenheit = int(input('Please enter the temperature in Fahrenheit: '))
# celsius = round((fahrenheit-32) * 5/9)
# print('You entered', fahrenheit, 'degrees Fahrenheit.', fahrenheit,
#       'degrees Fahrenheit is', celsius, 'degrees Celsius')

# # print(f'You entered {fahrenheit} degrees Fahrenheit. {fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius')

# celsius = int(input('Please enter the temperature in Celsius: '))
# fahrenheit = round(celsius*1.8 + 32)
# print('You entered', celsius, 'degrees Celsius.', celsius,
#       'degrees    Celsius is', fahrenheit, 'degrees Fahrenheit')

# # print(f'You entered {celsius} degrees Celsius. {celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit')

##########################################################
# hw4
# score = int(input('Please enter your score: '))
# if score >= 93:
#     grade = 'A'
# elif score >= 90:
#     grade = 'A-'
# elif score >= 86:
#     grade = 'B+'
# elif score >= 83:
#     grade = 'B'
# elif score >= 80:
#     grade = 'B-'
# elif score >= 76:
#     grade = 'C+'
# elif score >= 73:
#     grade = 'C'
# elif score >= 70:
#     grade = 'C-'
# elif score >= 66:
#     grade = 'D+'
# elif score >= 63:
#     grade = 'D'
# elif score >= 60:
#     grade = 'D-'
# elif score < 60:
#     grade = 'F'

# print('The grade for a score of', score, 'is', grade)

###############################################
# # hw 5

# print('Celsius  Fahrenheit')
# print('--------------')
# for celsius in range(0,21):
#     fahrenheit = round(celsius*1.8 + 32)
#     print(celsius,'\t',fahrenheit)

###############################################
# hw 6


# def print_table_line(celsius):
#     fahrenheit = round(celsius*1.8 + 32)
#     print(celsius, '\t', fahrenheit)


# def print_conversion_table(min, max):
#     print('Celsius\tFahrenheit')
#     print('-------------------')
#     for celsius in range(min, max+1):
#         print_table_line(celsius)


# min = int(input("Please enter the starting temperature for the table: "))
# max = int(input("Please enter the ending temperature for the table: "))
# print()
# print_conversion_table(min, max)


# hw7
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = round(celsius * 9 / 5 + 32)
#     return fahrenheit


# def print_celsius_to_fahrenheit_conversion_table(min, max):
#     print('Celsius Fahrenheit')
#     print('---------------------')

#     for celsius in range(min, max+1):
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(celsius, '\t', fahrenheit)


# def fahrenheit_to_celsius(fahrenheit):
#     celsius = round((fahrenheit-32) * 5 / 9)
#     return celsius


# def print_fahrenheit_to_celsius_conversion_table(min, max):
#     print('Fahrenheit Celsius')
#     print('---------------------')

#     for fahrenheit in range(min, max+1):
#         celsius = fahrenheit_to_celsius(fahrenheit)
#         print(fahrenheit, '\t', celsius)


# min_kelvin = int(input("Minimum Celsius temperature: "))
# max_kelvin = int(input("Maximum Celsius temperature: "))
# print()
# print_celsius_to_fahrenheit_conversion_table(min_kelvin, max_kelvin)

# print()
# min_fahrenheit = int(input("Minimum Fahrenheit temperature: "))
# max_fahrenheit = int(input("Maximum Fahrenheit temperature: "))
# print()
# print_fahrenheit_to_celsius_conversion_table(min_fahrenheit, max_fahrenheit)

################################
# #hw8
# # Comment
# import random

# # Comment
# def random_number_file_create(min,max,filename,entries):
#     with open(filename,'w') as file:
#         for n in range(entries):
#             number = random.randint(min,max)
#             file.write(str(number) + '\n')
# # Comment
# def lines_print(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             print(line.strip())
# # Comment
# def lines_count(filename):
#     count = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             count += 1
#     return count
# # Comment
# def total_numbers_in_file(filename):
#     total = 0
#     with open(filename, 'r') as file:
#         for number in file:
#             total += int(number)
#     return total

# FILENAME = "numbers.txt"
# random.seed(83)
# random_number_file_create(50, 100, FILENAME, 20)
# lines_print(FILENAME)
# print()
# entries = lines_count(FILENAME)
# total   = total_numbers_in_file(FILENAME)
# average = round(total/entries)
# print("Entries:", entries)
# print("Total:", total)
# print("Average:", average)

################################
# hw9
# def average_temps(max, min):
#     average = (max + min)/2
#     return average


# file = open('temps_max_min.txt', 'r')

# min_average = 100
# max_average = 0
# min_date = ''
# max_date = ''

# for line in file:
#     date, max, min = line.strip().split()
#     max = int(max)
#     min = int(min)
#     average = average_temps(max, min)

#     if average > max_average:
#         max_average = round(average)
#         max_date = date

#     if average < min_average:
#         min_average = round(average)
#         min_date = date

# print('Maximum average temperature:', max_average, 'on', max_date)
# print('Minimum average temperature:', min_average, 'on', min_date)

################################
# hw 10:
# def list_average(number_list):
#     average = round(sum(number_list)/len(number_list))
#     return average
# def list_minimum(number_list):
#     minimum = 100
#     for number in number_list:
#         if number < minimum:
#             minimum = number
#     return minimum
# def list_maximum(number_list):
#     maximum = 0
#     for number in number_list:
#         if number > maximum:
#             maximum = number
#     return maximum

# def above_average(number_list):
#     count = 0
#     average = list_average(number_list)
#     for number in number_list:
#         if number > average:
#             count += 1
#     return count

# numbers =  [62,60,58,50,85,93,99,77,72,74,61,68,73,65,57]
# print('numbers:         ', numbers)
# print('average:         ', list_average(numbers))
# print('minimum:         ', list_minimum(numbers))
# print('maximum:         ', list_maximum(numbers))
# print('above_average:   ', above_average(numbers))


################################
# hw 11:
# def read_file_into_integer_list(filename):
#     number_list = []
#     with open(filename, 'r') as file:
#         for line in file:
#             number_list.append(int(line))
#     return number_list


# def list_mean(number_list):
#     mean = round(sum(number_list)/len(number_list))
#     return mean


# def list_median(number_list):
#     sorted_number_list = sorted(number_list)
#     lstLen = len(number_list)
#     index = (lstLen - 1) // 2

#     if (lstLen % 2):
#         return sorted_number_list[index]
#     else:
#         return (sorted_number_list[index] + sorted_number_list[index + 1])/2.0


# def list_range(number_list):
#     list_min = min(number_list)
#     list_max = max(number_list)
#     list_range = list_max - list_min
#     return list_range


# numbers = read_file_into_integer_list('numbs.txt')
# print("numbers:             ", numbers)
# print("list_mean(numbers):  ", list_mean(numbers))
# print("list_median(numbers):", list_median(numbers))
# print("list_range(numbers): ", list_range(numbers))


print(2 % 2)
