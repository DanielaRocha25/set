#Inicialização dos sets A e B.
set_a = set()
set_b = set()

#Inserção de elementos
for i in range(4): #Utiliza um  loop para adicionar em cada conjunto 4 números informados pelo usuário.
    item_a = int(input("Informe um número para adicionar ao conjunto A:"))
    set_a.add(item_a)
    item_b = int(input("Informe um número para adicionar ao conjunto B:"))
    set_b.add(item_b)

#OPERAÇÕES
uniao = set_a.union(set_b) #Junta os elementos de ambos os conjuntos.
print("União dos conjuntos:", uniao)

interseccao = set.intersection(set_a,set_b)
print("Intersecção dos conjuntos: ", interseccao) #Retorna o que tem em comum nos dois conjuntos.

diferencaAB = set_a.difference(set_b) # Retorna o que tem no conjunto A, mas não tem no B.
print("Diferença entre os conjuntos (A-B): ", diferencaAB)

diferencaBA = set_b.difference(set_a) # Retorna o que tem no conjunto B, mas não tem no A.
print("Diferença entre os conjuntos (B-A): ", diferencaBA)

print("Conjunto A:",set_a)
print("Conjunto B",set_b)

#Remoção
remov = int(input("Informe um valor para remover do conjunto A: "))
set_a.remove(remov)
print("Conjunto após remoção:",set_a)

#Busca
item = int(input("Informe um valor para busca: "))
if item in set_a and item in set_b:
    print(f"{item} encontrado nos conjuntos A e B.")
elif item in set_a:
    print(f"{item} encontrado no conjunto A.")
elif item in set_b:
    print(f"{item} encontrado no conjunto B.")
else:
    print("Elemento não encontrado.")

