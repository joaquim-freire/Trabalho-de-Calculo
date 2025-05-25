def newton(tol=1e-10, max_inter=10):
    # função inicial f(x) = x^2 - 2
    f = lambda x: x**2 - 2
    # derivada f'(x) = 2x
    df = lambda x: 2 * x
    # chute inicial
    x = 1.0
    for i in range(max_inter):
        fx = f(x)
        dfx = df(x)
        # fórmula de Newton
        x_2 = x - fx / dfx
        # convergência
        if abs(x_2 - x) < tol:
            return x_2
        x = x_2
    return x  
# execução
raiz = newton()
print(f"A raiz de 2 é aproximadamente: {raiz}")
