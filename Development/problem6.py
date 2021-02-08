def count_yes_ans(group):
    found_question = set()
    for person in group:
        found_question.update([char for char in person.strip()])

    return len(found_question)



def problem6():
    with open(r"assets\p6_input.txt", 'r') as file_input:
        data = file_input.read()

        # Part 1
        print("The amount of yes q:", sum(count_yes_ans(group) for group in data.split("\n\n")))