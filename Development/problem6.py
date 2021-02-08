def count_anyone_yes(group):
    found_question = set()
    for person in group.split('\n'):
        found_question.update([char for char in person.strip()])

    return len(found_question)


def count_everyone_yes(group):
    persons = group.strip().split("\n")
    found_question = set([char for char in persons[0].strip()])  # The first person's yes questions

    for person in persons[1:]:
        found_question = found_question.intersection(set([char for char in person.strip()]))

    return len(found_question)


def problem6():
    with open(r"assets\p6_input.txt", 'r') as file_input:
        data = file_input.read()

        # Part 1
        print("The amount of anyone yes q:", sum(count_anyone_yes(group) for group in data.split("\n\n")))

        # Part 2
        print("The amount of everyone yes q:", sum(count_everyone_yes(group) for group in data.split("\n\n")))
