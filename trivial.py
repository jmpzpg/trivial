from partida import Partida
from jugador import Jugador
from pregunta import Pregunta
from respuesta import Respuesta
from modo import Modo

def main():
    pass

# creamos pregunta con dos respuestas
p1 = Pregunta(1, 'Es verano?')
r1 = Respuesta(1, 'Sí', False)
r2 = Respuesta(2, 'No', True)
# enganchamos la pregunta con sus respuestas
p1.respuestas = [r1, r2]

j = Jugador('Teo')              # creamos jugador
m = Modo()                      # creamos el modo

mi_partida = Partida(j,m,[p1])  # creamos la partida con la coleccion de preg.

mi_partida.iniciar()

for preg in mi_partida.col_preguntas:
    print(preg.cuerpo)
    for resp in preg.respuestas:
        print(resp.cuerpo)
