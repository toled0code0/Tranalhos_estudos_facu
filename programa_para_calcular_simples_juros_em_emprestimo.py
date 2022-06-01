#programa para calcular juros simples em emprestimo 
#linha de codigo
valor_1 = float(input('Digite o valor do emprestimo: '))
taxa_1 = float(input('Digite a porcentagem da taxa: ')) 
periodo_1 = int(input('Digite o tempo que o cliente deseja pagar o emprestimo: '))
juros_1 = ((valor_1/100)*taxa_1)
resultado_1 = valor_1+juros_1
valor_me_2 = resultado_1/periodo_1
#print's
print('O valor do emprestimo junto com a taxa  de {}% é: {} R$'.format(taxa_1, resultado_1))
print('o valor mensal fica de:{} R$'.format(valor_me_2))

