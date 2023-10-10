from random import randint

def digito_verificador(cpf:str):
  
  '''CPF: deve inserir os 9 digito do cpf'''
  cpf= cpf
  d=0
  for i in range(10,1,-1):
    #print(f'{cpf[10-i]}x{i}= {int(cpf[10-i])*i}')
    d = d + int(cpf[10-i])*i
  #coletando o resto da divisão por 11
  d = d%11
  if d == 0 or d == 1:
    d=0
  else:
    d = 11 - d
  return d

def numeroAleatorio():
  '''
Função para gerar os 9 primeiros digitos do CPF de maneira aleatoria
  '''
  dig_aleat=''
  for i in range(0,9):
    dig_aleat += str(randint(0,9)) 
  return dig_aleat

def nomeTitulo(titulo:str):
    '''NOMEIA A PORRA DO DESAFIO DE MANEIRA BONITINHA'''
    print(f'{'-'*45 :45}\n{ titulo:^45}\n{'-'*45:45}')

nomeTitulo('GERADOR E VERIFICADOR DE CPF')
while True:
  op = input('''
Insira uma das opções desejadas:
        [ 1 ] - GERAR CPF;
        [ 2 ] - CONFERIR UM CPF DADO OS 9 PRIMEIROS DIGITOS;
        [ 3 ] - SAIR
    ''')
  if op == '1':
    cpf=numeroAleatorio()                   #gera numero aleatorio
    cpf += str(digito_verificador(cpf))     #gera o PRIMEIRO digito verificador e concatena no cpf
    cpf +=str(digito_verificador(cpf[1:10]))#gera o SEGUNDO digito verificador e concatena no cpf
                                            #cpf final formatado
    cpf = cpf[0:9] + '-' + cpf[9:]
    nomeTitulo('CPF GERADO É: '+cpf)
  elif op == '2':
    while True:
      cpf = input('Digite os 9 primeiros digitos do CPF:')
      if len(cpf) != 9:
        print('Número invalido, digite novamente!')
      else:
        cpf = cpf + str(digito_verificador(cpf))
        cpf = cpf + str(digito_verificador(cpf[1:10]))
        nomeTitulo('OS DIGITOS VERIFICADORES SÃO:' + cpf[9:])
        break

  elif op == '3':
    nomeTitulo('FECHANDO O PROGRAMA')
    break
