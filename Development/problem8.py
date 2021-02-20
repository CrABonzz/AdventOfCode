def total_acc_one_run(raw_instructions):
    instructions = [(instruction.split(" ")[0], int(instruction.split(" ")[1])) for instruction in raw_instructions]

    accumulator = 0
    current_instruction = 0
    exectued_instructions = set()

    while True:
        if current_instruction in exectued_instructions:
            break

        exectued_instructions.add(current_instruction)

        command, argument = instructions[current_instruction]
        if "acc" == command:
            accumulator += argument
            current_instruction += 1
        elif "jmp" == command:
            current_instruction += argument
        else: # nop
            current_instruction += 1

    print("Part 1: Accumulator end of first run", accumulator)


def problem8():
    with open(r"assets\p8_input.txt", 'r') as file_input:
        intstructions = file_input.readlines()

        total_acc_one_run(intstructions)