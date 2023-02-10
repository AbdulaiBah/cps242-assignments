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
    if n >= 0:
        return to_unsigned_binary_from_dec(n,bits)
    binary = to_ones_comp_binary_from_dec(n,bits)
    binary = binary_add_unsigned(binary,[0,0,0,0,0,0,0,1])
    return binary


# Binary Addition

def binary_add_unsigned(bm, bn):
    '''
    Adds 2 unsigned binary numbers.
    '''
    binary = []
    carry = 0
    i = 7
    while i >= 0:
        if bm[i] == 0 and bn[i] == 0:
            if carry == 0:
                binary.insert(0,0)
            else:
                binary.insert(0,1)
                carry = 0
        elif bm[i] == 1 and bn[i] == 1:
            if carry == 0:
                binary.insert(0,0)
                carry = 1
            else:
                binary.insert(0,1)
        else:
            if carry == 0:
                binary.insert(0,1)
            else:
                binary.insert(0,0)
        i-=1
    return binary


def binary_add_ones_comp(bm, bn):
    '''
    Adds 2 one's complement binary numbers.
    '''
    binary = binary_add_unsigned(bm,bn)
    if bm[0] == 0 and bn[0] == 0:
        return binary
    elif bm[0] == 1 and bn[0] == 1:
        binary = binary_add_unsigned(binary,[0,0,0,0,0,0,0,1])
    else:
        if binary[0] == 0:
            binary = binary_add_unsigned(binary,[0,0,0,0,0,0,0,1])
    return binary


def binary_add_twos_comp(bm, bn):
    '''
    Adds 2 two's complement binary numbers.
    '''
    return binary_add_unsigned(bm,bn)


# Binary to Decimal

def to_dec_from_unsigned_binary(bm):
    '''
    Converts an unsigned binary number to decimal.
    '''
    ans = 0
    i = 0
    while i < len(bm):
        if bm[i] == 1:
            ans += 2**(len(bm)-1-i)
        i+=1
    return ans


def to_dec_from_sign_mag_binary(bm):
    '''
    Converts a sign + magnitude binary number to decimal.
    '''
    if bm[0] == 0:
        return to_dec_from_unsigned_binary(bm)
    return -1*to_dec_from_unsigned_binary(bm[1:])


def to_dec_from_ones_comp_binary(bm):
    '''
    Converts a one's complement binary number to decimal.
    '''
    if bm[0] == 0:
        return to_dec_from_unsigned_binary(bm)
    i = 0
    while i < len(bm):
        if bm[i] == 1:
            bm[i] = 0
        elif bm[i] == 0:
           bm[i] = 1
        i+=1
    return -1*to_dec_from_unsigned_binary(bm)


def to_dec_from_twos_comp_binary(bm):
    '''
    Converts a two's complement binary number to decimal.
    '''
    ans = 0
    i = 1
    while i < len(bm):
        if bm[i] == 1:
            ans += 2**(len(bm)-1-i)
        i+=1
    if bm[0] == 1:
        ans -= 2**(len(bm)-1)
    return ans
