# control_methods.py

# ================= PARITY =================
def parity_bit(data):
    ones = 0
    for ch in data:
        ones += bin(ord(ch)).count("1")
    return str(ones % 2)   # even parity


# ================= 2D PARITY =================
def parity_2d(data):
    bits = []
    for ch in data:
        bits.append(format(ord(ch), "08b"))

    row_parity = ""
    for b in bits:
        row_parity += str(b.count("1") % 2)

    col_parity = ""
    for i in range(8):
        col = 0
        for b in bits:
            if b[i] == "1":
                col += 1
        col_parity += str(col % 2)

    return row_parity + "|" + col_parity


# ================= CRC16 =================
def crc16(data):
    crc = 0xFFFF
    for ch in data:
        crc ^= ord(ch)
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return format(crc, "04X")


# ================= HAMMING (7,4) =================
def hamming_encode(data):
    encoded = ""
    for ch in data:
        b = format(ord(ch), "08b")
        for i in range(0, 8, 4):
            d = list(map(int, b[i:i+4]))
            p1 = d[0] ^ d[1] ^ d[3]
            p2 = d[0] ^ d[2] ^ d[3]
            p3 = d[1] ^ d[2] ^ d[3]
            encoded += f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"
    return encoded


def hamming_decode(encoded):
    return encoded  # detection only (simplified)


# ================= MAIN CONTROLLER =================
def generate_control(data, method):
    if method == "PARITY":
        return parity_bit(data)
    elif method == "2D_PARITY":
        return parity_2d(data)
    elif method == "CRC16":
        return crc16(data)
    elif method == "HAMMING":
        return hamming_encode(data)
    else:
        return ""


