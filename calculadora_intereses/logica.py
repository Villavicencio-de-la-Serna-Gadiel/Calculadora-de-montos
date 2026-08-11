import math
class Letra:
    def __init__(self, capital, redito, tiempo):
        self.capital = capital
        self.redito = redito
        self.tiempo = tiempo
    def interes(self, monto):
        return round(monto - self.capital, 2)
class LetraSimple(Letra):
    def __init__(self, capital, redito, tiempo):
        super().__init__(capital, redito, tiempo)
    def monto(self):
        return round(self.capital * (self.redito * self.tiempo + 1), 2)
    def progresion_monto(self):
        montos = {}
        for periodo in range(1, round(self.tiempo) + 1):
            monto_nuevo = LetraSimple(capital = self.capital,
                                      redito = self.redito,
                                      tiempo = periodo)
            montos[monto_nuevo.monto()] = periodo
        return montos
    def faltante(self, monto):
        resultado = None
        for atributo in self.capital, self.redito, self.tiempo:
            if atributo == "":
                if atributo is self.capital:
                    resultado = monto/(self.redito*self.tiempo + 1)
                elif atributo is self.redito:
                    resultado = (monto - self.capital)/(self.tiempo*self.capital)
                else:
                    resultado = (monto - self.capital)/(self.redito*self.capital)
        return resultado
class LetraCompuesta(Letra):
    def __init__(self, capital, redito, tiempo, capitalizacion):
        super().__init__(capital, redito, tiempo)
        self.capitalizacion = capitalizacion
    def monto(self):
        def capitalizacion_no_continua():
            return round(self.capital * (1 + self.redito) ** self.tiempo, 2)
        def capitalizacion_continua():
            return round(self.capital * math.e ** (self.redito * self.tiempo), 2)
        if self.capitalizacion == "capitalización continua":
            return capitalizacion_continua()
        else:
            return capitalizacion_no_continua()
    def progresion_monto(self):
        montos = {}
        for periodo in range(1, round(self.tiempo) + 1):
            letra_nueva = LetraCompuesta(capital = self.capital,
                                         redito = self.redito,
                                         tiempo = periodo,
                                         capitalizacion = self.capitalizacion)
            montos[letra_nueva.monto()] = periodo
        return montos
    def faltante(self, monto):
        resultado = None
        for atributo in self.capital, self.redito, self.tiempo:
            if atributo == "":
                if self.capitalizacion == "capitalización no continua":
                    if atributo is self.capital:
                        resultado = monto/((self.redito + 1)**self.tiempo)
                    elif atributo is self.redito:
                        resultado  = math.sqrt(monto/self.capital) - 1
                    else:
                        resultado = math.log(monto/self.capital, self.redito + 1)
                else:
                    if atributo is self.capital:
                        resultado = monto/(math.e**(self.redito*self.tiempo))
                    elif atributo is self.redito:
                        resultado = math.log(monto/self.capital, math.e)/self.tiempo
                    else:
                        resultado = math.log(monto/self.capital, math.e)/self.redito
        return resultado
def para_graficos(montos):
    return {"Monto":list(montos.keys()),
            "Periodo": list(montos.values())}
def recorrer_diccionario(diccionario, clave_valor, minimo, maximo):
    resultado = diccionario.copy()
    if clave_valor == "clave":
        for clave in diccionario.keys():
            if not minimo <= clave <= maximo:
                resultado.pop(clave)
    else:
        for clave, valor in diccionario.items():
            if not minimo <= valor <= maximo:
                resultado.pop(clave)
    return resultado
unidades = {"Días":0,"Meses":1, "Bimestres":2,
            "Trimestres":3, "Cuatrimestres":4,
            "Semestres":6, "Años":12}
def tiempo_transcurrido(fecha_inicial, fecha_final):
    return (fecha_final - fecha_inicial).days
def unidades_tiempo_admisibles(tiempo):
    admisibles = []
    tiempo = tiempo/30
    for unidad in unidades:
        if tiempo > unidades[unidad]:
            admisibles.append(unidad)
    return admisibles
def conversion_unidad_tiempo(tiempo, unidad):
    if unidad != "Días":
        return (tiempo/30)/unidades[unidad]
    else:
        return tiempo