arquivo = open('arqText.text' , 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

#leitura do arquivo texto

leitura = open('arqText.text', 'r')
print(leitura.read())
leitura.close()