import csv

def maiorPublico (filmes):
    cabeçalho = next(filmes)
    totalPublico = 0
    nomeFilme = ''
    anoLancamento = ''

    for filme in filmes:
        coluna = float(filme[9])

        if coluna > totalPublico:
            totalPublico = coluna
            nomeFilme = filme[2]
            anoLancamento = filme[1]
        else:
            continue

        print(f'O filme com maior público é {nomeFilme}')
        print(f'O total do público foi igual a {totalPublico}')
        print(f'O ano de lançamento foi {anoLancamento}')

with open('filmes.csv', newline='', encoding='utf-8') as filmes:
    lerFilmes = csv.reader(filmes)
    maiorPublico(lerFilmes)