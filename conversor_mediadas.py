#convertor em python de "m" para "cm" e "m" para "mn"
valor_metro = float(input('Digite o velor de mestro que você deseja converter :'))
medida_cm = 100
medida_mn = 1000
calculo_cm = float(valor_metro*medida_cm)
calculo_mn = float(valor_metro*medida_mn)
print("A sua medida em cm é {}cm ".format(calculo_cm))
print("a sua medida em mn é {}mn ".format(calculo_mn))
