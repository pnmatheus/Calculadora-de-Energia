'''
Turma: 4ECR
Alunos: 
Felipe Torigoe Carrera              RM 79896
Guilherme Fujii Ramalho Filgueiras  RM 79932
Matheus Issao Bocci                 RM 81542
Matheus Pereira Nascimento          RM 81618
Richard Rodrigues                   RM 80906
'''

tusd = 0.24332
te = 0.3099
bandeiraAmarela = 0.001874
bandeiraVermelhaP1 = 0.003971
bandeiraVermelhaP2 = 0.009492
bandeiraEscassez = 0.1420
pisPasep = 1.0092
cofins = 1.0391
cosip = 4.40
icms = 12

kwh = float(input('Insira o seu consumo no mês em kWh: '))

print(f'Consumo do mês (kWh): {kwh}')

opt = int(input('\nSelecione uma bandeira tarifária:'
'\n1 - Bandeira Verde: sem adição de tarifa'
f'\n2 - Bandeira Amarela: R${bandeiraAmarela} por kWh'
f'\n3 - Bandeira Vermelha Patamar 1: R${bandeiraVermelhaP1} por kWh'
f'\n4 - Bandeira Vermelha Patamar 2: R${bandeiraVermelhaP2} por kWh'
f'\n5 - Bandeira Escassez Hídrica: R${bandeiraEscassez} por kWh'
'\n\nDigite sua opção: '))

if opt == 1:
    bandeira = 0
elif opt == 2:
    bandeira = bandeiraAmarela
elif opt == 3:
    bandeira = bandeiraVermelhaP1
elif opt == 4:
    bandeira = bandeiraVermelhaP2
elif opt == 5:
    bandeira = bandeiraEscassez
else:
    print('\nBandeira inválida!')
    exit()

print(f'\n\nDetalhamento do Sistema Tarifario:'
f'\nTarifa de Uso do Sistema e Destribuição (TUSD): R${tusd}* por kWh' 
f'\nTarifa de Energia (TE): R${te}* por kWh\n'
f'\nAdicional Bandeira Amarela: R${bandeiraAmarela} por kWh'
f'\nPIS/PASEP: {round((pisPasep - 1)* 100, 2)}%'
f'\nCOFINS: {round((cofins - 1)* 100, 2)}%'
f'\nCOSIP Barueri: R${cosip}'
f'\nICMS: {icms}%'
'\n\n*Valores com impostos\n')

tp1 = tusd*kwh

tp2 = te*kwh

tp3 = bandeira*kwh

tp4 = tp1 + tp2 + tp3

tp5 = tp4 * pisPasep

tp6 = tp5 * cofins

total = tp5 + cosip

print(f'\nO valor da conta de energia será de: R${total}\n')
