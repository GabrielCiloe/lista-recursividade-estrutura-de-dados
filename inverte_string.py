def inverte_string(palavra):
    if len(palavra) == 0:
        return palavra
    else:
        return inverte_string(palavra[1:]) + palavra[0]