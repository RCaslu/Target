def proximo_na_sequencia_impar(seq):
    return seq[-1] + 2

def proximo_na_sequencia_dobrando(seq):
    return seq[-1] * 2

def proximo_na_sequencia_quadrados(seq):
    n = int(len(seq) ** 0.5) + 1
    return n * n

def proximo_na_sequencia_quadrados_pares(seq):
    n = int((seq[-1] ** 0.5) // 2 * 2) + 2
    return n * n

def proximo_na_sequencia_fibonacci(seq):
    return seq[-1] + seq[-2]

def proximo_na_sequencia_personalizada(seq):
    if seq[-1] == 10:
        return 12
    return seq[-1] + 1

a = [1, 3, 5, 7]
b = [2, 4, 8, 16, 32, 64]
c = [0, 1, 4, 9, 16, 25, 36]
d = [4, 16, 36, 64]
e = [1, 1, 2, 3, 5, 8]
f = [2, 10, 12, 16, 17, 18, 19]

a.append(proximo_na_sequencia_impar(a))
b.append(proximo_na_sequencia_dobrando(b))
c.append(proximo_na_sequencia_quadrados(c))
d.append(proximo_na_sequencia_quadrados_pares(d))
e.append(proximo_na_sequencia_fibonacci(e))
f.append(proximo_na_sequencia_personalizada(f))

print("a)", a)
print("b)", b)
print("c)", c)
print("d)", d)
print("e)", e)
print("f)", f)