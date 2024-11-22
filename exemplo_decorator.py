def minha_funcao_decorator(funcao_decorator):
    def func_wrapper():
        print("exemplo do decorador, parte wrapper.")

        funcao_decorator()
    return func_wrapper

@minha_funcao_decorator
def funcao_texto():
    print("Utilizando o decorator")

funcao_texto()