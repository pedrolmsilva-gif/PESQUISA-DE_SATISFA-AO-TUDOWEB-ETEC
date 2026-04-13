# Contadores 
excelente = 0
ruim = 0

print("--- PESQUISA DE SATISFAÇÃO TUDOWEB ---")

for i in range(1, 51):
    print("") # Linha vazia para separar os entrevistados
    print("Entrevistado nº", i)
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião: 1-EXCELENTE | 2-BOM | 3-RUIM")
    opiniao = int(input("Sua resposta: "))

    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 3:
        ruim = ruim + 1

# Exibição final
print("")
print("==============================")
print("RESULTADO DA PESQUISA")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("==============================")