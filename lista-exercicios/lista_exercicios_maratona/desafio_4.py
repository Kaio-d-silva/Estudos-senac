a = True
b = False
c = True


def executa_comparacao(valor1, comparador, valor2):
    if comparador == "and":
        return valor1 and valor2 
    elif comparador == "not":
        return not valor1 
    elif comparador == "or":
        return valor1 or valor2
   

exprecoes = [
    {"valor1" : a,
     "comparador" : "and",
     "valor2" : a
    }
    ,{"valor1" : b,
     "comparador" : "and",
     "valor2" : b
    }
    ,{"valor1" : c,
     "comparador" : "not",
      "valor2" : ""
    }
    ,{"valor1" : b,
     "comparador" : "not",
     "valor2" : ""
    }
    ,{"valor1" : a,
     "comparador" : "not",
     "valor2" : ""
    }
    ,{"valor1" : a,
     "comparador" : "and",
     "valor2" : b
    }
    ,{"valor1" : b,
     "comparador" : "and",
     "valor2" : c
    }
    ,{"valor1" : a,
     "comparador" : "or",
     "valor2" : c
    }
    ,{"valor1" : b,
     "comparador" : "or",
     "valor2" : c
    }
    ,{"valor1" : c,
     "comparador" : "or",
     "valor2" : a
    }
    ,{"valor1" : c,
     "comparador" : "or",
     "valor2" : b
    }
    ,{"valor1" : c,
     "comparador" : "or",
     "valor2" : c
    }
    ,{"valor1" : b,
     "comparador" : "or",
     "valor2" : b
    }
]

for exp in exprecoes:
    exp1 = exp["valor1"]
    exp2 = exp["valor2"]
    comparador = exp["comparador"]
    resultado_logico = executa_comparacao(exp1, comparador, exp2)
    print(f'{exp1} {comparador} {exp2} : {resultado_logico}')








# print(f"a: {a}, b: {b}, c: {c}")
# print(f"a and a: {a and a}")
# print(f"b and b: {b and b}")
# print(f"not c: {not c}")
# print(f"not b: {not b}")
# print(f"a and b: {a and b}")
# print(f"b and c: {b and c}")
# print(f"a or c: {a or c}")
# print(f"b or c: {b or c}")
# print(f"c or a : {c or a }")
# print(f"c or b: {c or b}")
# print(f"c or c: {c or c}")
# print(f"b or b: {b or b}")



