def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        first_number, operator, second_number = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first_number.isdigit() and second_number.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first_number), len(second_number)) + 2

        first_line.append(first_number.rjust(width))
        second_line.append(operator + second_number.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)
            answers.append(str(result).rjust(width))

    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
