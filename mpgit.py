print("Bem-vindo ao Programa de Cálculo de Áreas Geométricas!\n\n\n")



while True:
    forma = int(input("\nEscolha a forma geométrica para calcular a área:\n 1 - Quadrado\n 2 - Retangulo\n 3 - Triângulo\n 0 - Encerrar Programa\n\n"))
    while True:
    if forma == 1:
        quad = float(input("\nQual o tamanho dos lados do Quadrado?:\n"))
        print("\nA área do quadrado é:\n" + str(quad*quad) )
        
    elif forma == 2:
        comp = float(input("\nQual o comprimento do retângulo?:\n"))
        larg = float(input("\nQual a largura do retângulo?:\n"))
        print("\nA área do retângulo é:\n\n" + str(larg*comp) )
        
    elif forma == 3:
        base = float(input("\n\nQual a base do triângulo?:\n"))
        alt = float(input("\nQual a altura do triângulo?:\n"))
        print("\nA área do retângulo é:\n" + str((base * alt) / 2) ) 

    elif forma == 0:
        print("\nAté mais.\n")
        break
    
    else:
        print("Forma geométrica não encontrada")