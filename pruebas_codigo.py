from sql import Sqlite
import sqlite3
from partida import Partida
from jugador import Jugador
from pregunta import Pregunta
from respuesta import Respuesta
from modo import Modo

def preparar_consulta_ins(tabla, cadena_campos, cadena_valores):
    lista_valores = cadena_a_lista(cadena_valores)
    cadena = f'insert into {tabla}({cadena_campos}) values('
    for campo in lista_valores:
        if not campo.isdigit():
            cadena += f'"{campo}",'
        else:
            cadena += f'{campo},'

    return f'{cadena[:-1]})'

    # -------------------------------------------------------------      

def preparar_creacion(nombre_tabla, cadena_campos):
    cadena = f"create table if not exists {nombre_tabla} ({cadena_campos});"
    return cadena

    # -------------------------------------------------------------        

def cadena_a_lista(cadena):
    return cadena.split(',')
        
""" 
tabla = 'Primera'
cadena_campos = 'cuerpo,tematica_id,dificultad_id'
cadena_valores = 'La capital de Francia es?,2,1' """

#print(preparar_consulta_ins(tabla,cadena_campos,cadena_valores))


# 'cuerpo,tematica_id,dificultad_id', 'La capital de Francia es?,2,1')
                        

# creamos pregunta con dos respuestas
#p1 = Pregunta(1, 'Es verano?')
#r1 = Respuesta(1, 'Sí', False)
#r2 = Respuesta(2, 'No', True)
# enganchamos la pregunta con sus respuestas
#p1.respuestas = [r1, r2]

#j = Jugador('Teo')              # creamos jugador
#m = Modo()                      # creamos el modo

#mi_partida = Partida(j,m,[p1])  # creamos la partida con la coleccion de preg.

#mi_partida.iniciar()

#for preg in mi_partida.col_preguntas:
 #   print(preg.cuerpo)
  #  for resp in preg.respuestas:
   #     print(resp.cuerpo)

# Llenar la tabla Respuesta



def main():
    ''' Motor del juego
    '''
    print('Hola Mundo')
    # primero hay que cargar un modo para confirmar por el usuario:
    modo = Modo()
    # Mostramos pantalla con menú del juego según los datos del modo actual:
    continuar = True
    while(continuar):
        eleccion_correcta = False
        while( not eleccion_correcta ):

            #print("==================== MENÚ PRINCIPAL ====================")
            #print("+{:-<20}+{:-<50}".format("", ""))
	        #print("|{:^20}|{:^50}|".format("  #  ", 'Opciones a elegir'))
	        #print("+{:-<20}+{:-<50}".format("", ""))
            #print("|{:^20}|{:^50}|".format(' 1.-', 'Seleccionar número de jugadores:'))




            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar cursos")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                eleccion_correcta = True
                ejecutar_seleccion(opcion)
 
def ejecutar_seleccion(sel):
    print(sel)


def select_all_tasks():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cnx = sqlite3.connect('trivial_sqlite.db')

    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM Jugador")

    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)


def select_all_mio():
    base_datos = Sqlite('trivial_sqlite.db')
    conexion = base_datos.conectar
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Jugador")

    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)


def select_all_mio2():
    base_datos = Sqlite('trivial_sqlite.db')

    rows = base_datos.leer_tabla('Jugador')



    """ conexion = base_datos.conectar
    cursor = conexion.cursor()
    consulta = "SELECT * FROM Jugador"
    cursor.execute(consulta) """

    #rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)


select_all_mio2()


def bloque_jugadores():
    bd = Sqlite('trivial_sqlite.db')
    lista_jugadores = bd.leer_tabla('Jugador')

    for jugador in lista_jugadores:
        nombre_jugador = jugador[1]
        if nombre_jugador.find(' '):
            nombre_jugador.replace(' ','_')

    dic_players = {}
        dic_players2 = {}
        plantilla = 'player_'
        num = 1
        for jugador in lista_jugadores:
            plantilla += str(num)
            dic_players[plantilla] = jugador[1]
            num += 1


def tomar_preguntas_aleatorias_de_la_bd(modo):
    num_preguntas = modo.num_preguntas
    bd = Sqlite('trivial_sqlite.db')
    rows = bd.leer_tabla('Pregunta', 1, limit=num_preguntas)
    print(rows)
       
def tomar_preguntas_aleatorias_de_la_bd(modo):
    num_preguntas = modo.num_preguntas
    bd = Sqlite('trivial_sqlite.db')
    filas = bd.leer_tabla('Pregunta', 1, limit=num_preguntas)
    return filas


def tomar_preguntas_aleatorias_de_la_bd(modo):
    lista_preguntas_con_resp = []
    
    num_preguntas = modo.num_preguntas
    bd = Sqlite('trivial_sqlite.db')
    filas_preg = bd.leer_tabla('Pregunta', 1, limit=num_preguntas)
    for fila in filas_preg:
        resp = bd.leer_tabla_condicion('Respuesta', 'pregunta_id', fila[0])     # lista con 4 tuplas respuesta
        lista_respuestas_de_preg = []
        for t in resp:
            tmp = Respuesta(t[0], t[1], t[2])
            lista_respuestas_de_preg.append(tmp)
        lista_preguntas_con_resp.append(Pregunta(fila[0], fila[1], fila[2], fila[3], lista_respuestas_de_preg))
    
    for elem in lista_preguntas_con_resp:
        print(elem.cuerpo)
        for res in elem.l_obj_respuestas:
            print(res.cuerpo)
    
    #return lista_preguntas_con_resp


def comprobar_respuesta(self, indice_preg, indice_resp_contestada):
        # necesitmaos el id de la pregunta y el id de la respuesta
        p.preguntas[cont-1].id
        for r in self.preguntas[indice_preg].l_obj_respuestas:
            if r.id == id_resp_contestada.correcta:
                return True
        if self.preguntas[indice_preg].l_obj_respuestas[indice_resp_contestada].correcta == 1
