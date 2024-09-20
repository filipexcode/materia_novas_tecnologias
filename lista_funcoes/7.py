def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == '__main__':
    n = int(input("Digite um valor (n>= 3):"))
    if n < 3:
        print("O valor deve ser maior ou igual a 3.")
    else:
        print(f"O {n}-ésimo termo da série de Fibonacci é: {fibonacci(n)}")