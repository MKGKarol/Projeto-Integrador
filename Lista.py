Presidentes = {
    0: {
        'Indice': '0',
        'Nome': 'Branco',
        'votos': 0
    },
    1: {
        'Indice': '1',
        'Nome': 'Chewbacca de Assis',
        'votos': 0
    },
    2: {
        'Indice': '2',
        'Nome': 'Bem-te-vi Almeida',
        'votos': 0
    },
    3: {
        'Indice': '3',
        'Nome': 'Princesa Leia Organa',
        'votos': 0
    },
    4: {
        'Indice': '4',
        'Nome': 'R2D2',
        'votos': 0
    },
    5: {
        'Indice': '5',
        'Nome': 'Ada Lovelace',
        'votos': 0
    },
    6: {
        'Indice': 'Número inválido',
        'Nome': 'Nulo',
        'votos': 0
    },
}

Governadores = {
    0: {
        'Indice': '0',
        'Nome': 'Branco',
        'votos': 0
    },
    1: {
        'Indice': '1',
        'Nome': 'Aécio',
        'votos': 0
    },
    2: {
        'Indice': '2',
        'Nome': 'Romeu Zema',
        'votos': 0
    },
    3: {
        'Indice': '3',
        'Nome': 'Anastasia',
        'votos': 0
    },
    4: {
        'Indice': '4',
        'Nome': 'ciro',
        'votos': 0
    },
    5: {
        'Indice': '5',
        'Nome': 'Dilma',
        'votos': 0
    },
    6: {
        'Indice': 'Número inválido',
        'Nome': 'Nulo',
        'votos': 0
    },
}


def lista_votacao():

    print("Lista de Governadores")
    for candidato in Governadores:
        print('Candidato: ' + Governadores[candidato]['Indice'] + ' ' +
              Governadores[candidato]['Nome'])

    print("Lista de Presidentes")
    for candidato in Presidentes:
        print('Candidato: ' + Presidentes[candidato]['Indice'] + ' ' +
              Presidentes[candidato]['Nome'])
