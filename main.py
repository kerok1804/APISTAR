import requests

print('Testando APISTAR')

star_input1 = input('Digite o que procura: ')


star_input2 = input('Digite o ID: ')

request = requests.get('https://swapi.dev/api/{0}/{1}/'.format(star_input1,star_input2))

movies_data = request.json()

if 'detail' not in movies_data:
    print('==> Filme encontrado! <==')

    print('Nome do filme: {}'.format(movies_data['title']))
    print('Nome do diretor: {}'.format(movies_data['director']))
    print('Nome do produtor: {}'.format(movies_data['producer']))
    print('Data de lançamento: {}'.format(movies_data['release_date']))


else:
     print('Não encontrado!')

option = int(input('Deseja realizar uma nova consulta?\n1. Sim.\n2. Sair.\n'))
if option == 1:
    main()
else:
 print('Saindo...')

if __name__ == '_main_':
    main()