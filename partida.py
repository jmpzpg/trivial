class Partida():

    def __init__(self,
                obj_jugador,
                obj_modo,
                col_preguntas) -> None:
        
        self.__jugador = obj_jugador    # nos saltamso la validación
        self.__modo = obj_modo
        self.__col_preguntas = col_preguntas
        self.__marcador = 0

    @property
    def jugador(self):
        return self.__jugador
    @property
    def modo(self):
        return self.__modo
    @property
    def col_preguntas(self):
        return self.__col_preguntas
    @property
    def marcador(self):
        return self.__marcador

    def iniciar(self):
        print(self.__jugador)
        print(self.__modo)
        print(self.__col_preguntas)
        print(self.__marcador)
        print(self.__col_preguntas[0].respuestas)

    def finalizar(self):
        pass

    def barajar(self):
        pass

    def comprobar_respuesta(self, id_preg, id_resp):
        # necesitmaos el id de la pregunta y el id de la respuesta
        pass

    def actualizar_puntos(self):
        # si comprobar_respuesta es verdad --> jugador.resultado += 1
        pass