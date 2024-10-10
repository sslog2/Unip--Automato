def reconhece_placa(string):
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
            if char == '-':
                estado = 'q4'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q4':
            if char.isdigit():
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
        elif estado == 'q6':
            if char.isdigit():
                estado = 'q7'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q7':
            if char.isdigit():
                estado = 'q7'  
            else:
                estado = 'q_rejeita'
                break

    if estado in ['q1', 'q7']:
        return string + " É Placa."
    else:
        return string + " Não é placa"

print(reconhece_placa('ABC-DEFG'))
print(reconhece_placa('ABC-1234'))

