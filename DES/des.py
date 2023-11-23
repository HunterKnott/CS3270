'''Hunter Knott, Utah Valley University, CS 3100'''

m = "0123456789ABCDEF" # Plain text in hex
k = "133457799BBCDFF1" # Hex key
c = "" # Cipher text
k1=k2=k3=k4=k5=k6=k7=k8=k9=k10=k11=k12=k13=k14=k15=k16='' # Initial empty keys

def hex_to_binary(bin_string):
    '''Converts a hex string to a binary string'''
    hex_values = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"}

    binary_string = ""
    for element in bin_string:
        binary_string += hex_values[element]
    return binary_string

def subkeys(binary_k):
    '''Creates 16 subkeys by permutation and bit shifting'''
    global k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16

    pc1 = [57, 49, 41, 33, 25, 17,  9,
            1, 58, 50, 42, 34, 26, 18,
           10,  2, 59, 51, 43, 35, 27,
           19, 11,  3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
           14,  6, 61, 53, 45, 37, 29,
           21, 13,  5, 28, 20, 12,  4]
    
    pc2 = [14, 17, 11, 24,  1,  5,
            3, 28, 15,  6, 21, 10,
           23, 19, 12,  4, 26,  8,
           16,  7, 27, 20, 13,  2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    binary_k2 = table_perm(binary_k, pc1)
    c0 = binary_k2[:28]
    d0 = binary_k2[28:]

    c1 = bit_shift_left(c0, 1)
    d1 = bit_shift_left(d0, 1)
    k1 = table_perm(c1+d1, pc2)

    c2 = bit_shift_left(c1, 1)
    d2 = bit_shift_left(d1, 1)
    k2 = table_perm(c2+d2, pc2)

    c3 = bit_shift_left(c2, 2)
    d3 = bit_shift_left(d2, 2)
    k3 = table_perm(c3+d3, pc2)

    c4 = bit_shift_left(c3, 2)
    d4 = bit_shift_left(d3, 2)
    k4 = table_perm(c4+d4, pc2)

    c5 = bit_shift_left(c4, 2)
    d5 = bit_shift_left(d4, 2)
    k5 = table_perm(c5+d5, pc2)

    c6 = bit_shift_left(c5, 2)
    d6 = bit_shift_left(d5, 2)
    k6 = table_perm(c6+d6, pc2)

    c7 = bit_shift_left(c6, 2)
    d7 = bit_shift_left(d6, 2)
    k7 = table_perm(c7+d7, pc2)

    c8 = bit_shift_left(c7, 2)
    d8 = bit_shift_left(d7, 2)
    k8 = table_perm(c8+d8, pc2)

    c9 = bit_shift_left(c8, 1)
    d9 = bit_shift_left(d8, 1)
    k9 = table_perm(c9+d9, pc2)

    c10 = bit_shift_left(c9, 2)
    d10 = bit_shift_left(d9, 2)
    k10 = table_perm(c10+d10, pc2)

    c11 = bit_shift_left(c10, 2)
    d11 = bit_shift_left(d10, 2)
    k11 = table_perm(c11+d11, pc2)

    c12 = bit_shift_left(c11, 2)
    d12 = bit_shift_left(d11, 2)
    k12 = table_perm(c12+d12, pc2)

    c13 = bit_shift_left(c12, 2)
    d13 = bit_shift_left(d12, 2)
    k13 = table_perm(c13+d13, pc2)

    c14 = bit_shift_left(c13, 2)
    d14 = bit_shift_left(d13, 2)
    k14 = table_perm(c14+d14, pc2)

    c15 = bit_shift_left(c14, 2)
    d15 = bit_shift_left(d14, 2)
    k15 = table_perm(c15+d15, pc2)

    c16 = bit_shift_left(c15, 1)
    d16 = bit_shift_left(d15, 1)
    k16 = table_perm(c16+d16, pc2)

def table_perm(sequence, table):
    '''General function to perform permutation'''
    new_sequence = ''
    for element in table:
        new_sequence += sequence[element-1]
    return new_sequence

def bit_shift_left(bits, places):
    '''General function to shift bits in a string'''
    temp = bits[:places]
    bits = bits[places:]
    bits += temp
    return bits

def encode(binary_m):
    '''Creates a final hex value by using permutation, xor addition, and S boxes'''
    global c
    ipc = [58, 50, 42, 34, 26, 18, 10,  2,
          60, 52, 44, 36, 28, 20, 12,  4,
          62, 54, 46, 38, 30, 22, 14,  6,
          64, 56, 48, 40, 32, 24, 16,  8,
          57, 49, 41, 33, 25, 17,  9,  1,
          59, 51, 43, 35, 27, 19, 11,  3,
          61, 53, 45, 37, 29, 21, 13,  5,
          63, 55, 47, 39, 31, 23, 15,  7]
    
    e_bit_selection = [32,  1,  2,  3,  4,  5,
                        4,  5,  6,  7,  8,  9,
                        8,  9, 10, 11, 12, 13,
                       12, 13, 14, 15, 16, 17,
                       16, 17, 18, 19, 20, 21,
                       20, 21, 22, 23, 24, 25,
                       24, 25, 26, 27, 28, 29,
                       28, 29, 30, 31, 32,  1]
    
    ip_inv = [40,  8, 48, 16, 56, 24, 64, 32,
              39,  7, 47, 15, 55, 23, 63, 31,
              38,  6, 46, 14, 54, 22, 62, 30,
              37,  5, 45, 13, 53, 21, 61, 29,
              36,  4, 44, 12, 52, 20, 60, 28,
              35,  3, 43, 11, 51, 19, 59, 27,
              34,  2, 42, 10, 50, 18, 58, 26,
              33,  1, 41,  9, 49, 17, 57, 25]
    
    ip = table_perm(binary_m, ipc)
    l0 = ip[:32]
    r0 = ip[32:]
    
    l1 = r0
    er = table_perm(r0, e_bit_selection)
    xored_sequence = xor(k1, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r1 = xor(l0, f_sequence)

    l2 = r1
    er = table_perm(r1, e_bit_selection)
    xored_sequence = xor(k2, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r2 = xor(l1, f_sequence)

    l3 = r2
    er = table_perm(r2, e_bit_selection)
    xored_sequence = xor(k3, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r3 = xor(l2, f_sequence)

    l4 = r3
    er = table_perm(r3, e_bit_selection)
    xored_sequence = xor(k4, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r4 = xor(l3, f_sequence)

    l5 = r4
    er = table_perm(r4, e_bit_selection)
    xored_sequence = xor(k5, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r5 = xor(l4, f_sequence)

    l6 = r5
    er = table_perm(r5, e_bit_selection)
    xored_sequence = xor(k6, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r6 = xor(l5, f_sequence)

    l7 = r6
    er = table_perm(r6, e_bit_selection)
    xored_sequence = xor(k7, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r7 = xor(l6, f_sequence)

    l8 = r7
    er = table_perm(r7, e_bit_selection)
    xored_sequence = xor(k8, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r8 = xor(l7, f_sequence)

    l9 = r8
    er = table_perm(r8, e_bit_selection)
    xored_sequence = xor(k9, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r9 = xor(l8, f_sequence)

    l10 = r9
    er = table_perm(r9, e_bit_selection)
    xored_sequence = xor(k10, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r10 = xor(l9, f_sequence)

    l11 = r10
    er = table_perm(r10, e_bit_selection)
    xored_sequence = xor(k11, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r11 = xor(l10, f_sequence)

    l12 = r11
    er = table_perm(r11, e_bit_selection)
    xored_sequence = xor(k12, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r12 = xor(l11, f_sequence)

    l13 = r12
    er = table_perm(r12, e_bit_selection)
    xored_sequence = xor(k13, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r13 = xor(l12, f_sequence)

    l14 = r13
    er = table_perm(r13, e_bit_selection)
    xored_sequence = xor(k14, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r14 = xor(l13, f_sequence)

    l15 = r14
    er = table_perm(r14, e_bit_selection)
    xored_sequence = xor(k15, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r15 = xor(l14, f_sequence)

    l16 = r15
    er = table_perm(r15, e_bit_selection)
    xored_sequence = xor(k16, er)
    s_sequence = s_boxes(xored_sequence)
    f_sequence = s_permutation(s_sequence)
    r16 = xor(l15, f_sequence)

    final_sequence = table_perm(r16+l16, ip_inv)
    c = (hex(int(final_sequence, 2)))
    c = c[2:].upper()

def xor(seq1, seq2):
    '''Xor function for strings of binary'''
    sequence = ''
    for i in range(len(seq1)):
        if(seq1[i] == seq2[i]):
            sequence += '0'
        else:
            sequence += '1'
    return sequence

def s_boxes(orig_sequence):
    '''Creates a sequence of S box values from a bit sequence'''
    s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    s_box_sequence = ''
    s_box_counter = 0
    while len(orig_sequence) > 0:
        part_sequence = orig_sequence[:6]
        orig_sequence = orig_sequence[6:]
        row = part_sequence[0] + part_sequence[5]
        row_dec = bin(int(row, 2))
        row_dec = int(row_dec, 2)
        col = part_sequence[1:5]
        col_dec = bin(int(col, 2))
        col_dec = int(col_dec, 2)

        s_box_val = s_box[s_box_counter][row_dec][col_dec]
        s_box_sequence += format(s_box_val, '04b')
        s_box_counter+=1
    return s_box_sequence

def s_permutation(sequence):
    '''Does a final permutation before determining the final hex value'''
    p = [16,  7, 20, 21,
         29, 12, 28, 17,
          1, 15, 23, 26,
          5, 18, 31, 10,
          2,  8, 24, 14,
         32, 27,  3,  9,
         19, 13, 30,  6,
         22, 11,  4, 25]
    
    return table_perm(sequence, p)

def hex_input_check(sequence):
    if '0x' in sequence or '0X' in sequence:
        sequence = sequence[2:]
    if len(sequence) != 16:
        raise ValueError("The input must be 16 hex values long")
    try:
        hex_to_binary(sequence)
    except KeyError:
        print("The input can only have numbers 0-9 and letters A-F")
    return sequence

def string_to_hex(str):
    hex_result = ''.join(hex(ord(char))[2:] for char in str)
    print('String hex representation: ' + hex_result)
    return hex_result

def main():
    '''Produces encypted text based on an initial plain-text value and key,
        and then accepts new values to encrypt'''
    global k, m
    binary_k = hex_to_binary(k)
    subkeys(binary_k)
    binary_m = hex_to_binary(m)
    encode(binary_m)
    # print('Original text:' + m)
    # print('Original key:' + k)
    # print('Encrypted text:' + c)

    print('Enter an 8-character string to encode:')
    start_string = input()
    m = string_to_hex(start_string)
    print('Enter a 16-character hex value for a key:')
    k = input()
    k = hex_input_check(k.upper())
    binary_k = hex_to_binary(k)
    subkeys(binary_k)
    m = hex_input_check(m.upper())
    binary_m = hex_to_binary(m)
    encode(binary_m)
    print('Encrypted text:' + c)

if __name__ == "__main__":
    main()