def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()

    r['TOTAL'] = len(n)
    r['MAIOR'] = max(n)
    r['MENOR'] = min(n)
    r['MÉDIA'] = sum(n)/len(n)
    if sit:
        if r['MÉDIA'] >= 7:
            r['SITUAÇÃO'] = 'BOA NOTA'
        elif r['MÉDIA'] >= 5:
            r['SITUAÇÃO'] = 'NOTA RAZOÁVEL'
        else:
            r['SITUAÇÃO'] = 'NOTA RUIM'
    return r

resp = notas(5.0, 5.0, 9.5, sit=True)
print(resp)
print('-=-' * 25)
help(notas)
