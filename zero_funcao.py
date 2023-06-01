import math

class ZeroFuncao:
    def __init__ (self, expr, a, b, err):
        self.expr = expr
        self.a = a;
        self.b = b;
        self.err = err;

    def metodoBissecao (self):
        err = [self.err];
        x = [];
        a = [self.a];
        b = [self.b];
        i = 0;
        expr = self.expr;
        while err[i] >= self.err:
            print("Iteracao ",i+1,":");
            x.append((a[i] + b[i]) / 2);
            err.append((b[i] - a[i]) / 2);

            if expr(a[i]) < 0:
                if expr(x[i]) < 0:
                    a.append(x[i]);
                    if expr(b[i]) > 0:
                        b.append(b[i]);
                else:
                    a.append(a[i]);
                    if expr(x[i] > 0):
                        b.append(x[i]);
            print("===============================");
            print("X0:",i+1," = ", x[i]);
            print("[ ",a[i+1]," , ",b[i+1]," ]");
            print("Erro <= ", err[i+1]);
            print("===============================");
            print("\n");
            i = i + 1;
            
                
            
        
