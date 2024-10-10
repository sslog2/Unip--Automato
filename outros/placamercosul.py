def reconhece_numero(string):
  estado = 'q0'

  for char in string:
    if estado == 'q0':
      if char.isalpha():
        estado = 'q1'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q1':
      if char.isalpha():
        estado = 'q2'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q2':
      if char.isalpha():
        estado = 'q3'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q3':
      if char.isdigit():
        estado = 'q4'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q4':
      if char.isalpha():
        estado = 'q5'
      else:
        estado = 'q_rejeita'
        break
    elif estado == 'q5':
      if char.isdigit():
        estado = 'q6'
      else:
        estado = 'q_rejeita'
        break
  if estado in ['q1', 'q6']:
      return "É placa"
  else:
      return "Não é placa"

def main():

  placa = input("Digite a placa modelo mercosul: ")

  e_placa = reconhece_numero(placa)

  print(e_placa)

if __name__ == "__main__":
  main()
