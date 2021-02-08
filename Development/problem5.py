# F=0, B=1
# L=0, R=1
# The seat is 10 letters, 7 left letters are row, 3 right are column
# Seat ID = row*8+col


class Seat(object):
    def __init__(self, row, col):
        self.row = self.convert_seat_to_number(row)
        self.col = self.convert_seat_to_number(col)

    @staticmethod
    def convert_seat_to_number(val):
        return int(val, 2)

    def seat_id(self):
        return self.row * 8 + self.col

    def __repr__(self):
        return "row: {0}, col: {1}, seat_id: {2}".format(self.row, self.col, self.seat_id())


def replace_letters(seat):
    letters_map = {
        'F': '0',
        'B': '1',
        'L': '0',
        'R': '1'
    }

    for char in ['F', 'B', 'L', 'R']:
        seat = seat.replace(char, letters_map[char])

    return seat


def check_real_id(seats_id, id):
    return id - 1 in seats_id and id + 1 in seats_id


def check_heights(seats):
    seats = [replace_letters(seat.strip()) for seat in seats]

    seats = [Seat(seat[0:7], seat[7:10]) for seat in seats]
    seats_id = [seat.seat_id() for seat in seats]

    print("Max seat ID:", max(seats_id))  # Part 1 result

    all_flight_id = sorted([id for id in seats_id if check_real_id(seats_id, id)])

    missing_ids = []
    for id in range(min(all_flight_id), max(all_flight_id) + 1):
        if id not in all_flight_id:
            missing_ids.append(id)

    print("Missing ID's:", missing_ids[1])


def problem5():
    with open(r"assets\p5_input.txt", 'r') as file_input:
        seats = file_input.readlines()

        check_heights(seats)
