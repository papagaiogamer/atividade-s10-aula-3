# feito por david
#feito por:david
palavra = input('digite uma palavra')

codificado = []#vetor
for i in palavra:
    if i =='a':
        i = 'b'
        codificado.append(i)
    elif i == 'b':
        i = 'c'    
        codificado.append(i)
    elif i == 'c':
        i = 'd'
        codificado.append(i)
    elif i == 'd':
        i = 'e'
        codificado.append(i)
    elif i == 'e':
        i = 'f'
        codificado.append(i)
    elif i == 'f':
        i = 'g'
        codificado.append(i)
    elif i == 'g':
        i = 'h'
        codificado.append(i)
    elif i == 'h':
        i = 'i'
        codificado.append(i)
    elif i == 'i':
        i = 'j'
        codificado.append(i)
    elif i == 'j':
        i = 'k'
        codificado.append(i)
    elif i == 'k':
        i = 'l'
        codificado.append(i)
    elif i == 'l':
        i = 'm'
        codificado.append(i)
    elif i == 'm':
        i = 'n'
        codificado.append(i)
    elif i == 'n':
        i = 'o'
        codificado.append(i)
    elif i == 'o':
        i = 'p'
        codificado.append(i)
    elif i == 'p':
        i = 'q'
        codificado.append(i)
    elif i == 'q':
        i = 'r'
        codificado.append(i)
    elif i == 'r':
        i = 's'
        codificado.append(i)
    elif i == 's':
        i = 't'
        codificado.append(i)
    elif i == 't':
        i = 'u'
        codificado.append(i)
    elif i == 'u':
        i = 'v'
        codificado.append(i)
    elif i == 'v':
        i = 'w'
        codificado.append(i)
    elif i == 'w':
        i = 'x'
        codificado.append(i)
    elif i == 'x':
        i = 'y'
        codificado.append(i)
    elif i == 'y':
        i = 'z'
        codificado.append(i)

texto = "".join(codificado)
print('palavra codificada:',texto)
