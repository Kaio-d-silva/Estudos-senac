a = 4 
b = 10
c = 5.0 
d = 1 
f = 5.



# print(f"a == c : {a == c}") 
# print(f"a < b : {a < b}")
# print(f"b > b : {b > b}")
# print(f"c != f : {c != f}")
# print(f"c < d : {c < d}")
# print(f"b > a : {b > a}")
# print(f"c >= f : {c >= f}")
# print(f"f >= c : {f >= c}")
# print(f"c <= c : {c <= c}")
# print(f"c <= f : {c <= f}")


def executa_comparacao(valor1, comparador, valor2):
    if comparador == "==":
        return valor1 == valor2 
    elif comparador == "<":
        return valor1 < valor2
    elif comparador == ">":
        return valor1 > valor2
    elif comparador == "!=":
        return valor1 != valor2
    elif comparador == ">=":
        return valor1 >= valor2
    elif comparador == "<=":
        return valor1 <= valor2



equacoes = [
    {"valor1" : a, 
     "comparador" : "==",
     "valor2" : c
    }
    ,{"valor1" : a, 
     "comparador" : "<",
     "valor2" : b
    }
    ,{"valor1" : b, 
     "comparador" : ">",
     "valor2" : b
    }
    ,{"valor1" : c, 
     "comparador" : "!=",
     "valor2" : f
    }
    ,{"valor1" : a, 
     "comparador" : "==",
     "valor2" : b
    }
    ,{"valor1" : c, 
     "comparador" : "<",
     "valor2" : d
    }
    ,{"valor1" : b, 
     "comparador" : ">",
     "valor2" : a
    }
    ,{"valor1" : c, 
     "comparador" : ">=",
     "valor2" : f
    }
    ,{"valor1" : f, 
     "comparador" : ">=",
     "valor2" : c
    }
    ,{"valor1" : c, 
     "comparador" : "<=",
     "valor2" : c
    }
    ,{"valor1" : c, 
     "comparador" : "<=",
     "valor2" : f
    }
]

for exp in equacoes:
    exp1 = exp["valor1"]
    exp2 = exp["valor2"]
    comparador = exp["comparador"]
    resultado_logico = executa_comparacao(exp1, comparador, exp2)
    print(f'{exp1} {comparador} {exp2} : {resultado_logico}')


