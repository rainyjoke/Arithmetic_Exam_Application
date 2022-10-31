# write your code here
import random

def generate_expression():
    # It will generate simple arithmatic expresssions and return them in string format
    operators = '+-*'
    operand_1= random.randint(2,9)
    operator = random.choice(operators)
    operand_2 = random.randint(2,9)
    expression = str(operand_1)+' '+operator+' '+str(operand_2)
    return expression

def parse_expression(expression):
    # This function parses the passed expression into operands and operators and return them.
    split = expression.split(' ')
    operand_1, operator, operand_2 = int(split[0]), split[1], int(split[2])
    return operand_1, operand_2, operator
    
def calc_result(operand_1, operand_2, operator):
    # This function calculates the results based on the operands and operators
    result = 0
    if operator=='+':
        result += operand_1 + operand_2
    elif operator=='-':
        result += operand_1 - operand_2
    elif operator=='*':
        result += operand_1 * operand_2
    elif operator=='/':
        result += operand_1 / operand_2
    return result

def check_user_result(actual_result):
    # This function validates user result
    while True:
        try:
            user_input = int(input())
            if user_input == actual_result:
                return 'Right!'
            else:
                return 'Wrong!'
        except Exception:
            print("Wrong format! Try again.")

class WrongLevel(Exception):
    # This class is inherits the exception class to raise error if wrong level is entered by user.
    pass
def validate_level():
    # This function validates the level the user wants to participate in
    text = "Which level do you want? Enter a number:\n" \
           "1 - simple operations with numbers 2-9\n" \
           "2 - integral squares of 11-29\n"
    while True:
        try:
            level = int(input(text))
            if level in [1, 2]:
                return level
            else:
                raise Exception
        except Exception:
            print("Incorrect format.")


def tasks(level = 1):
    # generates five random tasks and stores it in a dictionary
    # with the corresponding results and returns
    # the dictionary.
    tasks = {}
    for i in range(5):
        if level == 1:
            expression = generate_expression()
            parsed = parse_expression(expression)
            result = calc_result(parsed[0], parsed[1], parsed[2])
            tasks[expression] = result

        elif level == 2:
            num = random.randint(11, 29)
            sq = num * num
            tasks[num] = sq
    return tasks

def test_user(tasks):
    # This is where the user is tested with the generated expressions based on
    # the corresponding the level the user has selected.
    # finally it returns the marks.
    marks = 0
    for expression in tasks:
        print(expression)
        check = check_user_result(tasks[expression])
        print(check)
        if check == 'Right!':
            marks += 1
    print(f"Your mark is {marks}/5. Would you like to save the result?")
    return marks


def save_results(marks, level):
    # saves the result in file results.txt if called.
    name = input("What is your name?\n")
    file = open('results.txt','a+')
    text = ""
    if level == 1:
        text += name+ ": " + str(marks) + "/5 in level 1 (simple operations with numbers 2-9)."
    else:
        text += name + ": " + str(marks) + "/5 in level 2 (integral squares 11-29)."
    file.write(text)
    file.close()

    print('The results are saved in "results.txt".')


def main():
    level = validate_level()
    exam = tasks(level)
    marks = test_user(exam)
    while True:
        save = input("Enter yes or no.\n")
        if save in ['Yes','y','YES','yes']:
            save_results(marks, level)
            break
        elif save in ['no', 'n', 'NO','No']:
            break
        else:
            break

main()