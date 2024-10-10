def mascara_cpf(cpf):
    estado = 'q0'
    cpf_mascarado = ""

    for char in cpf:
        if estado == 'q0':
            cpf_mascarado += 'X'
            estado = 'q1'
        elif estado == 'q1':
            cpf_mascarado += 'X'
            estado = 'q2'
        elif estado == 'q2':
            cpf_mascarado += 'X'
            estado = 'q3'
        elif estado == 'q3':
            cpf_mascarado += char
            estado = 'q4'
        elif estado == 'q4':
            cpf_mascarado += char
            estado = 'q5'
        elif estado == 'q5':
            cpf_mascarado += char
            estado = 'q6'
        elif estado == 'q6':
            cpf_mascarado += char
            estado = 'q7'
        elif estado == 'q7':
            cpf_mascarado += char
            estado = 'q8'
        elif estado == 'q8':
            cpf_mascarado += char
            estado = 'q9'
        elif estado == 'q9':
            cpf_mascarado += 'X'
            estado = 'q10'
        elif estado == 'q10':
            cpf_mascarado += 'X'
            estado = 'q_aceita'
        elif estado == 'q_aceita':
            return f"CPF mascarado com sucesso! ==> {cpf_mascarado}"
        else:
            estado = 'q_rejeita'
            return "CPF inválido, tente novamente."
    
    return "CPF inválido, tente novamente." if estado != 'q_aceita' else cpf_mascarado

print(mascara_cpf('99999999999'))

