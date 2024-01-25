def hex_to_bits(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    binary_string = binary_string.zfill(8)
    return binary_string




def Return_PassengerSeatMemoRequest(arg):
    return arg[0][0]

def Return_ClimFPrightBlowingRequest(arg):
    return int(arg[5][0:4], 2)

def Return_TimeFormatDisplay(arg):
    return arg[5][4]


def Get_bits_signal(list):
    dict_signal={}
    dict_signal['PassengerSeatMemoRequest']=Return_PassengerSeatMemoRequest(list)
    dict_signal['ClimFPrightBlowingRequest'] = Return_ClimFPrightBlowingRequest(list)
    dict_signal['TimeFormatDisplay'] = Return_TimeFormatDisplay(list)
    return dict_signal


def Print_signals(hexa,dict):
    print(hexa[:-2])
    print(dict)
    print()


if __name__ == '__main__':
    file_path = 'set_value1'

    with open(file_path, 'r') as file:
        for line in file:

            hex_values = line.split()
            bits_result=[]

            for hex_value in hex_values:
                bits_result.append(hex_to_bits(hex_value))

            dict_signals={}
            dict_signals=Get_bits_signal(bits_result)

            Print_signals(line,dict_signals)
