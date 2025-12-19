import random

def bit_flip(data):
    if not data:
        return data
    i = random.randint(0, len(data)-1)
    b = list(format(ord(data[i]), "08b"))
    j = random.randint(0, 7)
    b[j] = "1" if b[j] == "0" else "0"
    return data[:i] + chr(int("".join(b), 2)) + data[i+1:]

def multiple_bit_flips(data):
    if not data:
        return data

    num_flips = random.randint(2, 4)  # 2–4 bit flip
    data_list = list(data)

    for _ in range(num_flips):
        i = random.randint(0, len(data_list) - 1)
        bits = list(format(ord(data_list[i]), "08b"))
        j = random.randint(0, 7)
        bits[j] = "1" if bits[j] == "0" else "0"
        data_list[i] = chr(int("".join(bits), 2))

    return "".join(data_list)

def char_substitution(data):
    
    i = random.randint(0, len(data)-1)
    return data[:i] + chr(random.randint(65, 90)) + data[i+1:]


def char_deletion(data):
    i = random.randint(0, len(data)-1)
    return data[:i] + data[i+1:]


def char_insertion(data):
    i = random.randint(0, len(data))
    return data[:i] + chr(random.randint(65, 90)) + data[i:]


def char_swap(data):
    if len(data) < 2:
        return data
    i = random.randint(0, len(data)-2)
    lst = list(data)
    lst[i], lst[i+1] = lst[i+1], lst[i]
    return "".join(lst)


def burst_error(data):
    if len(data) < 3:
        return data

    burst_len = random.randint(3, min(8, len(data)))
    start = random.randint(0, len(data) - burst_len)

    corrupted = list(data)
    for i in range(start, start + burst_len):
        corrupted[i] = chr(random.randint(65, 90))

    return "".join(corrupted)


def corrupt_data(data):
    methods = [
        ("Single Bit Flip", bit_flip),
        ("Multiple Bit Flips", multiple_bit_flips),
        ("Character Substitution", char_substitution),
        ("Character Deletion", char_deletion),
        ("Character Insertion", char_insertion),
        ("Character Swap", char_swap),
        ("Burst Error", burst_error)
    ]

    error_name, error_func = random.choice(methods)
    corrupted_data = error_func(data)

    return corrupted_data, error_name


