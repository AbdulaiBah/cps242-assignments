# Decimal to Binary

def to_unsigned_binary_from_dec(n, bits=8):
    '''
    Converts a decimal number to unsigned binary.
    '''
    binary = []
    while n > 0:
        binary.insert(0,n % 2)
        n //= 2
    if len(binary) < bits:
        binary = [0] * (bits - len(binary)) + binary
    return binary

    
def to_sign_mag_binary_from_dec(n, bits=8):
    '''
    Converts a decimal number to sign + magnitude binary.
    '''
    binary = []
    if n < 0:
        n *= -1
        binary = to_unsigned_binary_from_dec(n,bits)
        binary[0] = 1
    else:
        binary = to_unsigned_binary_from_dec(n,bits)
    return binary


def to_ones_comp_binary_from_dec(n, bits=8):
    '''
    Converts a decimal number to one's complement binary.
    '''
    binary = []
    if n < 0:
        n *= -1
        binary = to_unsigned_binary_from_dec(n,bits)
        i = 0
        while i < len(binary):
            if binary[i] == 1:
                binary [i] = 0
            elif binary[i] == 0:
                binary [i] = 1
            i+=1
    else:
        binary = to_unsigned_binary_from_dec(n,bits)
    return binary


def to_twos_comp_binary_from_dec(n, bits=8):
    '''
    Converts a decimal number to two's complement binary.
    '''
    
    return []


# Binary Addition

def binary_add_unsigned(bm, bn):
    '''
    Adds 2 unsigned binary numbers.
    '''
    
    return []


def binary_add_ones_comp(bm, bn):
    '''
    Adds 2 one's complement binary numbers.
    '''
    return []


def binary_add_twos_comp(bm, bn):
    '''
    Adds 2 two's complement binary numbers.
    '''
    return []


# Binary to Decimal

def to_dec_from_unsigned_binary(bm):
    '''
    Converts an unsigned binary number to decimal.
    '''
    return 0


def to_dec_from_sign_mag_binary(bm):
    '''
    Converts a sign + magnitude binary number to decimal.
    '''
    return 0


def to_dec_from_ones_comp_binary(bm):
    '''
    Converts a one's complement binary number to decimal.
    '''
    return 0


def to_dec_from_twos_comp_binary(bm):
    '''
    Converts a two's complement binary number to decimal.
    '''
    return 0
