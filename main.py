from zero_funcao import ZeroFuncao
import math

def pegarIntervalo (intervalo):
    intervalo = list(intervalo);
    i = 0;
    a = "";
    b = "";
    while intervalo[i] != ",":
        a = a + intervalo[i];
        i = i + 1;

    i = i + 1;
    while i != len(intervalo):
        b = b + intervalo[i];
        i = i + 1;
        
    a = float(a);
    b = float(b);

    return a,b;

if __name__ == '__main__':
    strExpr = input("F(x)= ");
    expr = lambda x: eval(strExpr);
    
    while True:
        intervalo = input("Insira o intervalo de amplitude 1, ex: 1,2: ");
        intervalo = list(intervalo);
        if intervalo:
            a, b = pegarIntervalo(intervalo);
            break;
        else:
            print("Insira um intervalo valido");


    err = input("Defina o valor maximo de erro: ");
    err = float(err);

    zFunc = ZeroFuncao(expr,a,b,err);
    zFunc.metodoBissecao();
