import openpyxl

book = openpyxl.Workbook()

book.create_sheet('Teste')

teste_page = book['Teste']

teste_page.append(['Produto', 'Quantidade', 'Preço'])

# Importação de dados para a planilha

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        teste_page.append([produto, quantidade, preco])

book.save('Teste.xlsx')