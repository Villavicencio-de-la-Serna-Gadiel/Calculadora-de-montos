def calcular(operacion):
    nueva_operacion = operacion
    if operacion == "":
        return ""
    else:
        for indice, elemento in enumerate(operacion):
            if elemento == "×":
                nueva_operacion = nueva_operacion.replace(elemento, "*")
            elif elemento == "÷":
                nueva_operacion = nueva_operacion.replace(elemento, "/")
        try:
            return eval(nueva_operacion)
        except SyntaxError:
            return "Operación inválida"
        except TypeError:
            return ["Operación inválida", '''Debe especificarse la operación a realizar
                                             si se usan paréntesis.''']
        except ZeroDivisionError:
            return ["Operacion indefinida", '''La división de un número, como numerador,
                                               con cero se considera indefinida.''']