
def hex_to_bit(hex_list):
    bin_list = []
    for hex_string in hex_list:
        binary = bin(int(hex_string, 16))[2:].zfill(8)
        bin_list.append(binary)
    return bin_list


def bit_to_hex(bit_list):
    hex_list = []
    for binary_string in bit_list:
        hex_value = format(int(binary_string, 2), '02X')
        hex_list.append(hex_value)
    return hex_list

def modified_LDW_AlertStatus(arg_list):
    arg_list = hex_to_bit(arg_list)
    byte2=arg_list[2][::-1]
    list_byte2=list(byte2)
    list_byte2[4:6] = '01'
    new_byte2 = ''.join(list_byte2)
    arg_list[2]=new_byte2[::-1]
    return arg_list

def modified_LCA_OverrideDisplay (arg_list):
    arg_list = hex_to_bit(arg_list)
    byte5=arg_list[5][::-1]
    list_byte5=list(byte5)
    list_byte5[-3] = '1'
    new_byte5 = ''.join(list_byte5)
    arg_list[5]=new_byte5[::-1]
    return arg_list


def modified_DW_FollowUpTimeDisplay(arg_list):
    arg_list = hex_to_bit(arg_list)
    byte4=arg_list[4][::-1]
    list_byte4=list(byte4)
    list_byte4[2:8] = bin(45)[2:]
    new_byte4 = ''.join(list_byte4)
    arg_list[4]=new_byte4[::-1]
    return arg_list

def write_to_file(hex_list, path_file):
    with open(path_file, 'a') as f:
            f.write(' '.join(hex_list))
            f.write('\n')



def parse_hex_sequence(hex_sequence):
    index = 1
    list_PDU_after=['00']
    while index < len(hex_sequence):
        signal_header  = hex_sequence[index:index + 2]
        signal_length = int(hex_sequence[index + 2], 16)
        signal_PDU = hex_sequence[index + 3:index + 3 + signal_length]


        if signal_header==['06', '02']:
            new_list_LDW_AlertStatus=modified_LDW_AlertStatus(signal_PDU)
            list_PDU_after.extend(signal_header)
            list_PDU_after.append(hex_sequence[index + 2])
            list_PDU_after.extend(bit_to_hex(new_list_LDW_AlertStatus))
            list_PDU_after.append('00')

        elif signal_header == ['05', 'D0']:
            new_list_DW_FollowUpTimeDisplay  = modified_DW_FollowUpTimeDisplay (signal_PDU)
            list_PDU_after.extend(signal_header)
            list_PDU_after.append(hex_sequence[index + 2])
            list_PDU_after.extend(bit_to_hex(new_list_DW_FollowUpTimeDisplay))
            list_PDU_after.append('00')


        elif signal_header==['06', '01']:
            new_list_LCA_OverrideDisplay=modified_LCA_OverrideDisplay(signal_PDU)
            list_PDU_after.extend(signal_header)
            list_PDU_after.append(hex_sequence[index + 2])
            list_PDU_after.extend(bit_to_hex(new_list_LCA_OverrideDisplay))
            list_PDU_after.append('00')



        if signal_header[0:2] ==['06', '01']:
            list_after_index=hex_sequence[index:]
            list_PDU_after.extend(list_after_index)
            break
        else:
            index += 4 + signal_length

    return list_PDU_after


if __name__ == '__main__':
    file_path = 'set_value2'
    out_file_path = 'out_signal2'
    with open(out_file_path, 'w'):
        pass

    with open(file_path, 'r') as file:
        for line in file:
            bytes = line.split()
            list_after=parse_hex_sequence(bytes)
            write_to_file(list_after,out_file_path)
