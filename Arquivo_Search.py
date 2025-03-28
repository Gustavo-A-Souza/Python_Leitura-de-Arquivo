def calcular_media(numeros):
    """Calcula a média dos números em uma lista."""
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def ler_numeros_do_arquivo(arquivo_nome):
    """Lê números de um arquivo e armazena em uma lista."""
    numeros = []
    
    # Abre o arquivo para leitura
    with open(arquivo_nome, 'r') as arquivo:
        linha = arquivo.readline()
        
        while linha:  # Enquanto houver linha no arquivo
            linha = linha.strip()  # Remove espaços em branco da linha
            
            if linha.isdigit():  # Verifica se a linha contém apenas números
                numeros.append(int(linha))  # Adiciona o número à lista
            else:
                print(f'Ignorando linha não numérica: {linha}')
            
            linha = arquivo.readline()  # Lê a próxima linha
    
    return numeros

# Função principal
def main():
    # Caminho do arquivo
    nome_arquivo = 'Text'  # Nome do arquivo atualizado
    
    # Lê os números do arquivo
    numeros = ler_numeros_do_arquivo(nome_arquivo)
    
    # Se houver números na lista, calcula e imprime a média
    if numeros:
        media = calcular_media(numeros)
        print(f'A média dos números é: {media}')
    else:
        print('Não foi possível calcular a média. Nenhum número válido foi encontrado no arquivo.')

# Chama a função principal
main()