ACCUMALTOR_COMMAND = "acc"
JMP_COMMAND = "jmp"
NOP_COMMAND = "nop"

def run_until_loop(raw_instructions):
    instructions = [(instruction.split(" ")[0], int(instruction.split(" ")[1])) for instruction in raw_instructions]

    accumulator = 0
    current_instruction = 0
    exectued_instructions = set()

    while True:
        if current_instruction in exectued_instructions or \
                current_instruction < 0 or current_instruction >= len(instructions):
            break

        exectued_instructions.add(current_instruction)

        command, argument = instructions[current_instruction]

        if ACCUMALTOR_COMMAND == command:
            accumulator += argument
            current_instruction += 1
        elif JMP_COMMAND == command:
            current_instruction += argument
        else:  # NOP_COMMAND
            current_instruction += 1

    return accumulator, current_instruction


def fix_program(instructions):
    """
    We need to make the program end, means the last instruction will be len(instructions)
    """
    for index, instruction in enumerate(instructions):
        command = instruction.split(" ")[0]

        if command == JMP_COMMAND:
            new_command = NOP_COMMAND
        elif command == NOP_COMMAND:
            new_command = JMP_COMMAND
        else:
            continue

        old_instruction = instructions[index]
        instructions[index] = instruction.replace(command, new_command)

        accumulator, last_instructions = run_until_loop(instructions)
        if len(instructions) == last_instructions:
            return accumulator

        # Restore
        instructions[index] = old_instruction


def problem8():
    with open(r"assets\p8_input.txt", 'r') as file_input:
        intstructions = file_input.readlines()

        accumulator, _ = run_until_loop(intstructions)
        print("Part 1: Accumulator end of first run", accumulator)

        accumulator = fix_program(intstructions)
        print("Part 2 Accumulator of the fixed program", accumulator)
