def calculate_floor(string):
    current_floor = 0
    for i in range(4):
        if string[i] == 'U':
            current_floor += 1
        else:
            current_floor += -1
    return current_floor


if __name__ == '__main__':
    print(calculate_floor('UUDU'))