import numpy as np

#Encrypt massage
def split_massage(massage):
    entire_mini_massage = []

    mini_massage = []

    micro_massage = []

    massage_size = len(massage)

    for n in massage:
        size = len(mini_massage)
        #mini_massage.append(n)

        micro_massage.append(n)
        mini_massage.append(micro_massage)
        micro_massage = []

        if size == 3:
            massage_size = massage_size - 4
            entire_mini_massage.append(mini_massage)
            mini_massage = []

    if massage_size < 4:
        new_number = 4 - len(mini_massage)
        j = 0
        while(j < new_number):
            #mini_massage.append(' ')
            
            micro_massage.append(' ')
            mini_massage.append(micro_massage)
            
            j = j + 1
            micro_massage = []
        entire_mini_massage.append(mini_massage)
    
    return entire_mini_massage

def translate(splitted_massage):
    for n in splitted_massage:
        for m in range(4):
            n[m][0] = sub_translate(n[m][0])

    return splitted_massage

def sub_translate(m):
    if m == ' ':
        m = 0
    elif m == 'a':
        m = 1
    elif m == 'b':
        m = 2
    elif m == 'c':
        m = 3
    elif m == 'd':
        m = 4
    elif m == 'e':
        m = 5
    elif m == 'f':
        m = 6
    elif m == 'g':
        m = 7
    elif m == 'h':
        m = 8
    elif m == 'i':
        m = 9
    elif m == 'j':
        m = 10
    elif m == 'k':
        m = 11
    elif m == 'l':
        m = 12
    elif m == 'm':
        m = 13
    elif m == 'n':
        m = 14
    elif m == 'ñ':
        m = 15
    elif m == 'o':
        m = 16
    elif m == 'p':
        m = 17
    elif m == 'q':
        m = 18
    elif m == 'r':
        m = 19
    elif m == 's':
        m = 20
    elif m == 't':
        m = 21
    elif m == 'u':
        m = 22
    elif m == 'v':
        m = 23
    elif m == 'w':
        m = 24
    elif m == 'x':
        m = 25
    elif m == 'y':
        m = 26
    elif m == 'z':
        m = 27

    return m

def encrypt_massage(translated_massage):
        
    new_massage_helper = []

    encrypt_matrix = np.array([[3,1,-5,1],[6,1,2,4],[3,4,5,1],[2,8,9,5]])


    for n in translated_massage:
        mini_massage_helper = np.array(n)
        encrypted_massage = np.dot(encrypt_matrix,mini_massage_helper)
        new_massage_helper.append(encrypted_massage)
        

    #encrypt_matrix = np.array([[3,1,-5,1],[6,1,2,4],[3,4,5,1],[2,8,9,5]])
    #encrypted_massage = np.dot(translated_massage,encrypt_matrix)

    #return just_numbers(encrypted_massage),encrypt_matrix
    return just_numbers(new_massage_helper),encrypt_matrix

def just_numbers(encrypted_massage):
    code = ''
    for n in encrypted_massage:
        for m in n:
            code = code + ','+str(m[0])
    
    return code[1:]

#decrypt massage
def split_massage_received(massage_received):
    code = massage_received.split(',')
    
    entire_mini_massage = []

    mini_massage = []

    micro_massage = []

    massage_size = len(code)

    for n in code:
        size = len(mini_massage)
        micro_massage.append(int(n))
        
        #mini_massage.append(int(n))

        mini_massage.append(micro_massage)
        micro_massage = []


        if size == 3:
            massage_size = massage_size - 4
            entire_mini_massage.append(mini_massage)
            mini_massage = []
    
    return entire_mini_massage

def descrypt_massage(received_splitted_massage,encrypt_matrix):
#    key_matrix = np.array([[1/34,3/34,7/34,-2/17],[23/136,-65/408,41/408,5/68],[-41/272,13/272,19/272,-3/136],[-3/272,109/816,-301/816,23/136]])

#    key_matrix = np.array([[0.0294,0.0882,0.2059,-0.1176],[0.1691,-0.1593,0.1005,0.0735],[-0.1507,0.0478,0.0699,-0.0221],[-0.0110,0.1336,-0.3689,0.1692]])

    new_massage_helper = []

    key_matrix = np.linalg.inv(encrypt_matrix)

    #descrypted_massage = np.dot(received_splitted_massage,key_matrix)

    for n in received_splitted_massage:
        mini_massage_helper = np.array(n)
        descrypted_massage = np.dot(key_matrix,mini_massage_helper)
        new_massage_helper.append(descrypted_massage)

    secret_massage = []
    mini_secret_massage = []

    for o in new_massage_helper:
        for p in range(4):
            mini_secret_massage.append(round(float(o[p][0])))
        secret_massage.append(mini_secret_massage)
        mini_secret_massage = []

    return secret_massage

def reverse_translate(descrypted_massage):

    original_massage = ''

    for n in descrypted_massage:
        for m in range(4):
            original_massage = original_massage + reverse_sub_translate(n[m])

    return original_massage


def reverse_sub_translate(m):
    if m == 0:
        return ' '
    elif m == 1:
        return 'a'
    elif m == 2:
        return 'b'
    elif m == 3:
        return 'c'
    elif m == 4:
        return 'd'
    elif m == 5:
        return 'e'
    elif m == 6:
        return 'f'
    elif m == 7:
        return 'g'
    elif m == 8:
        return 'h'
    elif m == 9:
        return 'i'
    elif m == 10:
        return 'j'
    elif m == 11:
        return 'k'
    elif m == 12:
        return 'l'
    elif m == 13:
        return 'm'
    elif m == 14:
        return 'n'
    elif m == 15:
        return 'ñ'
    elif m == 16:
        return 'o'
    elif m == 17:
        return 'p'
    elif m == 18:
        return 'q'
    elif m == 19:
        return 'r'
    elif m == 20:
        return 's'
    elif m == 21:
        return 't'
    elif m == 22:
        return 'u'
    elif m == 23:
        return 'v'
    elif m == 24:
        return 'w'
    elif m == 25:
        return 'x'
    elif m == 26:
        return 'y'
    elif m == 27:
        return 'z'
