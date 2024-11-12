lista = []
nome_lista = input('Qual nome deseja a dar a sua lista?')

while True:
    comando = input('Para adiconar um item em sua lista de compras digite (A), \n'
                'para excluir um item digite (X) \n'
                'para mostrar sua lista digite (S).\n'
                'para finalizar sua lista e sair digite (F)')
    
    if comando == 'A':
        item_adicionado =input('Qual item deseja adicionar?')
        lista.append(item_adicionado)
        print(f'Você adicionou {item_adicionado} em sua lista')
    
    elif comando == 'X':
         indice_str = input('Qual item deseja excluir?')
         indice = int(indice_str)
         del lista[indice]
         print(f'Você excluiu {indice_str} de sua lista.')
    
    elif comando == 'S':
        lista_enumerada = enumerate(lista)
        for indice, nome in enumerate(lista):
            print(indice, nome)
    
    elif comando == 'F':
       print(f'Sua lista {nome_lista} contem os seguintes itens: {lista}')
       break

    else:
        print('Digite um comando valido!') 
    
