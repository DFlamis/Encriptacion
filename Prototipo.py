import numpy as np
import Funciones as fn

#Prototipo de Algebra Lineal

massage = input('Ingrese el mensaje que desea encriptar: ')

splitted_massage = fn.split_massage(massage)

translated_massage = fn.translate(splitted_massage)
print(f'Su mensaje traducido es: {translated_massage}')

main_encrypted_massage = fn.encrypt_massage(translated_massage)

encrypted_massage = main_encrypted_massage[0]
print(f'Su mensaje encriptado es: {encrypted_massage}')

massage_received = input('Ingrese su mensaje encriptado: ')
received_splitted_massage = fn.split_massage_received(massage_received)

descrypted_massage = fn.descrypt_massage(received_splitted_massage,main_encrypted_massage[1])


reverse_translated_massage = fn.reverse_translate(descrypted_massage)

print(f'su mensaje es: {reverse_translated_massage}')

