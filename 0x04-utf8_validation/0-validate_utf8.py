#!/usr/bin/python3

def validUTF8(data):
    """ Check if the data set is a valid UTF-8 encoding """
    n_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            if (byte >> 5) == 0b110:  # 2 bytes
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3 bytes
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4 bytes
                n_bytes = 3
            elif byte >> 7:  # 1 byte character should start with 0
                return False
        else:
            # Continuation bytes must start with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    # All characters should be fully processed
    return n_bytes == 0
