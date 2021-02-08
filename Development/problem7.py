def parse_rules(rules_lines):
    rules = {}
    amount = {}

    for rule in rules_lines:
        rule = rule.strip(".").split(" contain ")
        bag = rule[0][:-(4 if rule[0][-1] == "g" else 5)]  # bag or bags

        if rule[1] == "no other bags":
            rules[bag] = []
            amount[bag] = []
        else:
            inside_bags = [inside_bags.split() for inside_bags in rule[1].split(", ")]

            # Parse inside bags line
            rules[bag] = [" ".join(inside_bag[1:3]) for inside_bag in inside_bags]
            amount[bag] = [int(inside_bag[0]) for inside_bag in inside_bags]
    return rules, amount


def can_contain(rules: dict, rule, bag, cache):
    if rule in cache:
        return cache[rule]
    if bag in rules[rule]:
        cache[rule] = True
    else:
        cache[rule] = any(can_contain(rules, b, bag, cache) for b in rules[rule])
    return cache[rule]


def can_contain_recursive(rules: dict) -> int:
    cache = {}
    print("Can contain:", sum([can_contain(rules, rule, "shiny gold", cache) for rule in rules]))


def count_bags(rules: dict, amount: dict, bag, included_bags):
    if bag in included_bags:
        return included_bags[bag]

    if len(rules[bag]) == 0:
        included_bags[bag] = 0
        return 0

    included_bags[bag] = sum([amount[bag][in_bag_index] * (count_bags(rules, amount, rules[bag][in_bag_index], included_bags) + 1)
                              for in_bag_index, _ in enumerate(rules[bag])])
    return included_bags[bag]


def bags_required(rules: dict, amount: dict) -> int:
    included_bags = {}
    print("Required bags: ", count_bags(rules, amount, "shiny gold", included_bags))


def problem7():
    with open(r"assets\p7_input.txt", 'r') as file_input:
        rules = file_input.readlines()

    rules, amount = parse_rules([rule.strip() for rule in rules])

    # Part 1
    can_contain_recursive(rules)

    # Part 2
    bags_required(rules, amount)
