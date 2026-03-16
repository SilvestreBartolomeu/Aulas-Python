TAMANHO = 10
notas1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("notas1", notas1)
# ou
notas2 = [0]*TAMANHO
print("notas2", notas2)
# ou
import numpy as np # type: ignore
notas3 = np.zeros(TAMANHO).astype(int)
print("notas3", notas3)
# ou
vetor = ['O carro','peixe',123,111.12]
print("vetor",vetor)
# etc.