# try:
#     machine = input('Machine: ')
#     if machine.isnumeric():
#         print('Only character')
#     elif machine != 'a' and machine != 'b':
#         raise Exception
#     else:
#         print('Hello machine ', machine)
# except Exception:
#     print('You should enter only a or b')

list1 = list()


machine = input('Machine: ')
score = float(input('Score: '))

if machine == 'a':
    if score >= 88:
        print('The grade is: A')
    elif score >= 76 and score <= 87:
        print('The grade is: B')
    elif score >=62 and score <= 75:
        print('The grade is: C')
    elif score >=48 and score <= 61:
        print('The grade is: D')
    elif score <=47:
        print('The grade is: E')
  
elif machine == 'b':
    if score >= 92:
        print('A')
    elif score >= 85 and score <= 91:
        print('B')
else:
    pass
    #print('Error')


