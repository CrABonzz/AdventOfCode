def parse_line(rule):
    # Example of rule: drab gold bags contain 2 posh aqua bags, 3 dark olive bags.
    [container, bags] = rule.split(" bags contain ")

    bags = [bag[2:bag.index(" bag")] for bag in (bags.strip()[:-1].split(", "))]

    return container, bags


def can_contain(rules):
    can_be_in = {}

    for rule in rules:
        container, bags = parse_line(rule)

        for bag in bags:
            if bag in can_be_in:
                can_be_in[bag].append(container)
            else:
                can_be_in[bag] = [container]

    shiny_gold_container = set()
    shiny_gold_container.update(can_be_in["shiny gold"])
    new_containers = shiny_gold_container

    while 0 != len(new_containers):
        temp_new_contatins = set()
        for bag in new_containers:
            try:
                temp_new_contatins.update(can_be_in[bag])
            except KeyError:
                pass

        new_containers = temp_new_contatins

        shiny_gold_container.update(new_containers)

    print(len(shiny_gold_container))


def problem7():
    with open(r'assets\p7_input.txt', 'r') as file_input:
        rules = file_input.readlines()

        can_contain(rules)
