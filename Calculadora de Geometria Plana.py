import time


def limpar():
    print('     ' * 50)


def linha():
    print('-' * 30)

def quadro_de_mensagem():
    print('''
Temos essas opções:
1 - Triângulo (T)
2 - Quadrado  (Q)
3 - Retângulo (R)
4 - Losango   (L)
5 - Trapézio  (Tr)
6 - Círculo   (C)
''')
def verificar_formula(txt):
    print(txt)

def explicação(txt):
    print('   '*30)
    print('-'*50)
    print(txt)
    print('-'*50)

def retorno(msg):
    return msg

while True:
    linha()
    print('Olá estudante!')
    linha()

    print('Deseja aprender sobre geometria plana ou fazer cálculos?')
    decisão = input('Responda com Cálculo(C) ou Estudo(E): escreva a vogal ou a cosoante!').lower()
    if decisão == 'e':
        limpar()
        linha()
        print('Ok, vamos começar')
        linha()
        linha()
        quadro_de_mensagem()
        linha()
        escolha = input('As opções estão ao lado do nome digite aqui sua opção:').lower()
        
        if escolha == 't':
            explicação('''
Triângulo
                       
Para calcular a área de um triângulo, basta multiplicar a medida 
da base (b) com a medida da altura (h) e dividir o resultado por dois.
A=b.h/2
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break

        elif escolha == 'q':
            explicação('''
Quadrado
Sabemos que os lados do quadrado são todos iguais. Para calcular sua área, multiplicamos a medida da base com a medida altura. 
Como as medidas são as mesmas, multiplicá-las é o mesmo que elevar o lado ao quadrado.
A=L*2
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break

        elif escolha == 'r':
            explicação('''
Retângulo
A área do retângulo é dada pela multiplicação da base pela altura.
A=b.h
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break

        elif escolha == 'l':
            explicação('''
Losango
A área do losango é dada pelo produto da diagonal maior 
(D) com a diagonal menor (d) dividido por dois.
A= D.d/2
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break

        elif escolha == 'tr':
            explicação('''
Trapézio
A área do trapézio é dada pelo produto da altura com a soma da base maior (B) e a base menor (b) dividido por dois.
A=(B+b).h/2
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break
        
        elif escolha == 'c':
            explicação('''
Círculo
A área do círculo de raio r é dada pelo produto do raio ao 
quadrado com o número irracional ℼ (em geral utilizamos o valor ℼ = 3,14).
A= ℼ.r*2                  
''')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break   
        
        else:
            print('Essa opção não existe!')
            finalizar = input('Prosseguir(p) ou encerrar(e) o programa:').lower()
            if finalizar == 'p':
                print('Ok, o programa voltará do inicio!')
                time.sleep(5)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
            else:
                print('O programa finalizará!')
                break 
    
    elif decisão == 'c':
        limpar()
        linha()
        print('Ok, vamos começar')
        linha()
        linha()
        quadro_de_mensagem()
        linha()
        escolha = input('As opções estão ao lado do nome digite aqui sua opção:').lower()
        
        if escolha == 't':
            print('Lembrando que o calculo do triângulo é:A=b.h/2')
            area = input('Essa conta possui valor na área? s/n').lower()
            limpar()
            if area == 's':
                print('Ok, agora me fale a área')
                limpar()
                valor_da_area = int(input('Digite o valor da área:'))
                limpar()
                opção = input('Possui valor da altura(h) ou da base(b)? ')
                if opção == 'h':
                    limpar()
                    valor_da_altura = int(input('Digite o valor da altura:'))
                    limpar()
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_altura}.b/2')
                    limpar()
                    confirmar = input('Está certo a formúla? s/n').lower()
                    limpar()
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        resultado_da_area = valor_da_area * 2
                        resultado_da_altura = valor_da_altura
                        calculo_final = resultado_da_area / resultado_da_altura
                        print(f'''
 {valor_da_area}/1 = {valor_da_altura}.b/2                             
 {resultado_da_area} = {resultado_da_altura}.b
 {calculo_final} = b
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
                    else:
                        print('Ops, então vamos retomar!')
                        time.sleep(3)
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        retorno(retorno('Retornarmos'))
                elif opção == 'b':
                    valor_da_base = int(input('Digite o valor da base:'))
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_base}.h/2')
                    confirmar = input('Está certo a formúla? s/n')
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        resultado_da_area = valor_da_area * 2
                        resultado_da_base = valor_da_base
                        calculo_final = resultado_da_area / resultado_da_base
                        print(f'''
 {valor_da_area}/1 = {valor_da_base}.h/2                             
 {resultado_da_area} = {resultado_da_base}.h
 {calculo_final} = h
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
            else:
                valor_da_base = int(input('Digite o valor da base:'))
                valor_da_altura = int(input('Digite o valor da altura:'))
                calculo = (valor_da_base * valor_da_altura)
                calculo_final = calculo/2
                print(f'''
A = {valor_da_base}.{valor_da_altura} / 2
A = {calculo} / 2
A = {calculo_final}
Espero que tenha gostado ;)
''')
                print('Vamos terminar por aqui, até logo!')
                break
        
        elif escolha == 'q':
            print('Lembrando que a formúla do quadrado é A = L**2')
            limpar()
            area = input('Possui valor da área? s/n').lower()
            limpar()
            if area == 's':
                valor_da_area = int(input('Digite o valor da área:'))
                limpar()
                valor_final_da_area = valor_da_area // 2
                print(f'''
 {valor_da_area} = L**2
 {valor_da_area} // 2 = L
 {valor_final_da_area} = L
 
 Espero que tenha gostado ;)
''')
                print('Vamos terminar por aqui, até logo!')
                break
            else:
              valor_do_lado = int(input('Ok, digite o valor dos lados:'))
              limpar()
              valor_final_do_lado =valor_do_lado ** 2
              print(f'''
 {valor_do_lado} = L**2
 {valor_do_lado} ** 2 = A
 {valor_final_do_lado} = A
 
 Espero que tenha gostado ;)
''')
              print('Vamos terminar por aqui, até logo!')
              break
        
        elif escolha == 'r':
            print('Lembrando que a formúla da área do retângulo é: A = b.h')
            area = input('Possui o valor da área: s/n').lower()
            limpar()
            if area == 's':
                print('Ok, agora me fale a área')
                limpar()
                valor_da_area = int(input('Digite o valor da área:'))
                limpar()
                opção = input('Possui valor da altura(h) ou da base(b)? ').lower()
                limpar()
                if opção == 'h':
                    valor_da_altura = int(input('Digite o valor da altura:'))
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_altura}.b')
                    limpar()
                    confirmar = input('Está certo a formúla? s/n').lower()
                    limpar()
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        calculo_final = valor_da_area / valor_da_altura
                        print(f'''
 {valor_da_area}/1 = {valor_da_altura}.b                             
 {valor_da_area} / {valor_da_altura} = b
 {calculo_final} = b
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
                    else:
                        print('Ops, então vamos retomar!')
                        time.sleep(3)
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        retorno(retorno('Retornarmos'))
                elif opção == 'b':
                    valor_da_base = int(input('Digite o valor da base:'))
                    limpar()
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_base}.h/2')
                    limpar()
                    confirmar = input('Está certo a formúla? s/n')
                    limpar()
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        calculo_final = valor_da_area / valor_da_base
                        print(f'''
 {valor_da_area}/1 = {valor_da_base}.h                             
 {valor_da_area} / {valor_da_base} = h
 {calculo_final} = b
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
                    else:
                        print('Ops, então vamos retomar!')
                        time.sleep(3)
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        retorno(retorno('Retornarmos'))
            else:
                valor_da_base = int(input('Digite o valor da base:'))
                valor_da_altura = int(input('Digite o valor da altura:'))
                calculo_final = valor_da_base * valor_da_altura
                print(f'''
 A = {valor_da_base} . {valor_da_altura}                             
 {valor_da_base} . {valor_da_altura} = A
 {calculo_final} = A
 Espero que tenha gostado ;)
''')
                print('Vamos terminar por aqui, até logo!')
                break
        
        elif escolha == 'l':
            print('Lembrando que a formúla da área do losango é A = D.d/2 ')
            limpar()
            area = input('Essa conta possui valor na área? s/n').lower()
            limpar()
            valor_da_area = int(input('Digite o valor da área:'))
            if area == 's':
                print('Seja especifico, coloque caixa alta para Diagonal maior e digite sem normal para a menor')
                opção = input('Possui valor na Diagonal(D) maior ou na menor(d):')
                if opção ==  'D':
                    limpar()
                    valor_da_diagonal = int(input('Digite o valor da Diagonal maior:'))
                    limpar()
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_diagonal}.d/2')
                    limpar()
                    confirmar = input('Está certo a formúla? s/n').lower()
                    limpar()
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        resultado_da_area = valor_da_area * 2
                        resultado_da_diagonal = valor_da_diagonal
                        calculo_final = resultado_da_area / resultado_da_diagonal
                        print(f'''
 {valor_da_area}/1 = {valor_da_diagonal}.d/2                             
 {resultado_da_area} = {resultado_da_diagonal}.d
 {calculo_final} = d
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
                    else:
                        print('Ops, então vamos retomar!')
                        time.sleep(3)
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        retorno(retorno('Retornarmos'))
                elif opção == 'd':
                    limpar()
                    valor_da_diagonal = int(input('Digite o valor da diagonal menor:'))
                    limpar()
                    verificar_formula(f'{valor_da_area}/1 = {valor_da_diagonal}.D/2')
                    limpar()
                    confirmar = input('Está certo a formúla? s/n').lower()
                    limpar()
                    if confirmar == 's':
                        print('Ok, vamos continuar')
                        resultado_da_area = valor_da_area * 2
                        resultado_da_diagonal = valor_da_diagonal
                        calculo_final = resultado_da_area / resultado_da_diagonal
                        print(f'''
 {valor_da_area}/1 = {valor_da_diagonal}.D/2                             
 {resultado_da_area} = {resultado_da_diagonal}.D
 {calculo_final} = D
 Espero que tenha gostado ;)
''')
                        print('Vamos terminar por aqui, até logo!')
                        break
                    else:
                        print('Ops, então vamos retomar!')
                        time.sleep(3)
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        limpar()
                        retorno(retorno('Retornarmos'))
            else:
                valor_da_diagonal_maior = int(input('Digite o valor da Diagonal maior:'))
                valor_da_diagonal_menor = int(input('Digite o valor da diagonal menor:'))
                resultado_da_diagonal = valor_da_diagonal_menor * valor_da_diagonal_maior
                calculo_final = resultado_da_diagonal / 2
                print(f'''
A = {valor_da_diagonal_maior} . {valor_da_diagonal_menor} / 2
A = {resultado_da_diagonal} / 2
A = {calculo_final}
Espero que tenha gostado ;)
''')
                print('Vamos acabar por aqui, até logo!')
                break
        
        elif escolha == 'tr':
            print('Esse vai ser um pouco diferente, pesquisei algumas contas e notei que sempre possui as das bases')
            print('Lembrando que a formúla da área do trapézio é a = (B+b).h/2')
            limpar()
            valor_da_altura = int(input('Digite o valor da altura:'))
            limpar()
            valor_da_base_maior = int(input('Digite o valor da Base maior:'))
            valor_da_base_menor = int(input('Digite o valor da base menor:'))
            print(f'A = ({valor_da_base_maior}+{valor_da_base_menor}).{valor_da_altura}/2')
            confirmar = input('Está certo a formúla? s/n').lower()
            limpar()
            if confirmar == 's':
                print('Ok, vamos continuar')
                resultado_das_bases = valor_da_base_maior + valor_da_base_menor
                resultado_da_base_vezes_altura = resultado_das_bases * valor_da_altura
                calculo_final = resultado_da_base_vezes_altura / 2
                print(f'''
 A = ({valor_da_base_maior}+{valor_da_base_menor}).{valor_da_altura}/2
 A = {resultado_das_bases}.{valor_da_altura}/2
 A = {resultado_da_base_vezes_altura}/2
 A = {calculo_final}
 Espero que tenha gostado ;)
''')
                print('Vamos terminar por aqui, até logo!')
                break
            else:
                print('Ops, então vamos retomar!')
                time.sleep(3)
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                limpar()
                retorno(retorno('Retornarmos'))     
        
        elif escolha == 'c':
            print('Lembrando que a formúla da área do círculo é A= ℼ.r*2')
            limpar()
            area = input('A conta possui valor na área: s/n').lower()
            if area == 's':
                valor_da_area = float(input('Digite o valor da área:'))
                valor_da_area_divido_por_pi = float(valor_da_area / 3.14)
                descobrindo_raiz = valor_da_area_divido_por_pi // 2
                print(f'''
{valor_da_area} = 3.14 r*2
{valor_da_area_divido_por_pi} = r*2
{descobrindo_raiz} = r
Espero que tenha gostado ;)
''')
                print('Vamos encerrar por aqui, até logo!')
                break
            else:
                valor_do_raio = int(input('Digite o valor do raio:'))
                valor_do_raio1 = valor_do_raio ** 2
                valor_do_raio_multiplicado_por_pi = float(valor_do_raio1 * 3.14)
                print(f'''
A = {valor_do_raio}*2 . 3,14
A = {valor_do_raio1} . 3,14
A = {valor_do_raio_multiplicado_por_pi}
Espero que tenha gostado ;)
''')
                print('Vamos encerrar por aqui, até logo!')
                break
