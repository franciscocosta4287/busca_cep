import requests

def main():
    print()
    print("##################")
    print("### Consulta CEP ###")
    print("##################")
    print()
    
    cep_input = input('Digite o CEP para consulta: ')
    if len(cep_input) != 8:
      print('Quantidade de digitos invalidos')
      exit()
    req = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    
    addres_data = req.json()
    
    if 'erro' not in addres_data:
        print('===>CEP Encontrado<===')
        print('CEP: {}' .format(addres_data['cep']))
        print('LOGRADOURO: {}' .format(addres_data['logradouro']))
        print('COMPLEMENTO: {}' .format(addres_data['complemento']))
        print('BAIRRO: {}' .format(addres_data['bairro']))
        print('LOCALIDADE: {}' .format(addres_data['localidade']))
        print('UF: {}' .format(addres_data['uf']))
        print('IBGE: {}' .format(addres_data['ibge']))
        print('GIA: {}' .format(addres_data['gia']))
        print('DDD: {}' .format(addres_data['ddd']))

        
    else:
        print('{}: CEP Inválido' .format(cep_input))
        
    option = int(input('Deseja realizar umanova consulta ? \n1. Sim\n2. Saisr\n'))
    
    if option == 1:
        main()
if __name__ == "__main__":
    main()