temperatura = input('Ingrese temperatura a convertir: ')

new_temp = float(temperatura)

tipo = input('Es Fahrenheit(F) o Celsius(C)?: ').lower()

if tipo == 'F':
  print((new_temp - 32) * 5 / 9)
elif tipo == 'C':
  print((9 / 5 * new_temp) + 32)
else:
  print('Invalido')