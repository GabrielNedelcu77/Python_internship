def Split_list_8byte(arg_list):
    it = 0
    list_8byte = []
    list_list_8byte = []

    for byte8 in arg_list:
        it += 1
        list_8byte.append(byte8)

        if it == 8:
            it = 0
            list_list_8byte.append(list_8byte[:])
            list_8byte.clear()

    return list_list_8byte


def Hex_to_bit(hex_strings):
    bin_list = []
    for hex_string in hex_strings:
        bin_sublista = [format(int(hex_val, 16), '08b') for hex_val in hex_string]
        bin_list.append(bin_sublista)
    return bin_list


def Bit_to_hex(bit_strings):
    hex_list = []
    for bit_string in bit_strings:
        hex_sublista = [format(int(bin_val, 2), '02X') for bin_val in bit_string]
        hex_list.append(hex_sublista)
    return hex_list


# Values to be set for each of the signals:
# LDW_AlertStatus = 2
# DW_FollowUpTimeDisplay = 45
# LCA_OverrideDisplay = 1
def Modified_signal(arg_list):
    arg_list = Hex_to_bit(arg_list)
    for signal in arg_list:
        # LDW_AlertStatus = 2
        byte2 = signal[2][::-1]
        list_byte2 = list(byte2)
        list_byte2[4:6] = '01'
        new_byte2 = ''.join(list_byte2)
        signal[2] = new_byte2[::-1]

        # LCA_OverrideDisplay = 1
        byte5 = signal[5]
        list_byte5 = list(byte5)
        list_byte5[-3] = '1'
        new_byte5 = ''.join(list_byte5)
        signal[5] = new_byte5[:]

        # DW_FollowUpTimeDisplay = 45
        byte4 = signal[4][::-1]
        list_byte4 = list(byte4)
        list_byte4[2:8] = bin(45)[2:]
        new_byte4 = ''.join(list_byte4)
        signal[4] = new_byte4[::-1]

    return Bit_to_hex(arg_list)


def Write_to_file(hex_list, path_file):
    with open(path_file, 'a') as f:
        for sublista in hex_list:
            linie = ' '.join(sublista) + ' '
            f.write(linie)
        f.write('\n')


if __name__ == '__main__':
    file_path = 'set_value2'
    out_file_path = 'out_signal2'
    with open(out_file_path, 'w'):
        pass

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            list_8bytes = []
            list_8bytes_before = Split_list_8byte(words)
            list_8bytes_after = Modified_signal(list_8bytes_before)
            Write_to_file(list_8bytes_after, out_file_path)
