# F=0, B=1
# L=0, R=1
# The seat is 10 letters, 7 left letters are row, 3 right are column
# Seat ID = row*8+col
from dataclasses import dataclass


class Seat(object):
    def __init__(self, row, col):
        self.row = self.convert_seat_to_number(row)
        self.col = self.convert_seat_to_number(col)

    def convert_seat_to_number(self, val):
        return int(val, 2)

    def seatID(self):
        return self.row*8+self.col

    def __repr__(self):
        return "row: {0}, col: {1}, seat_id: {2}".format(self.row, self.col, self.seatID())

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


def check_heights(seats):
    seats = [replace_letters(seat.strip()) for seat in seats]

    seats = [Seat(seat[0:7], seat[7:10]) for seat in seats]

    print(max(seat.seatID() for seat in seats))

def problem5():
    with open(r"assets\p5_input.txt", 'r') as file_input:
        seats = file_input.readlines()

        check_heights(seats)
