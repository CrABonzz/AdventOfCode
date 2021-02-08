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


with open('assets/p6_input.txt', 'r') as forms:
    groups = [group_answers.strip() for group_answers in forms.read().split('\n\n')]

overall_yes = 0
for group in groups:
    group_yes = set()
    for member_yes in group.split('\n'):
        for char in member_yes:
            group_yes.add(char)

    overall_yes += len(group_yes)

# Answer One
print("Sum of all groups yes counts:", overall_yes)

overall_group_yes = 0
for group in groups:
    members = group.split('\n')
    group_yes = set([char for char in members[0]])
    for member in members[1:]:
        group_yes = set([char for char in member]).intersection(group_yes)

    overall_group_yes += len(group_yes)

# Answer Two
print("Sum of all group overall yes counts:", overall_group_yes)
