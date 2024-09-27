def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

if __name__ == "__main__":
    while True:
        num = int(input("Informe um número: "))
        if is_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")