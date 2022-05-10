# instanciamos una conexión
bd = Sqlite('trivial_sqlite.db')
#print(bd.nombre)
#conexion = bd.conectar
cadena = 'id integer primary key, nombre text not null unique, resultado integer default 0, total_puntos integer default 0'
bd.crear_tabla('Jugador', cadena)

cadena1 = 'id integer primary key, nombre text not null unique' 
bd.crear_tabla('Tematica', cadena1)

cadena2 = 'id integer primary key, nombre text not null unique' 
bd.crear_tabla('Dificultad', cadena2)

cadena3 = '''id integer primary key, 
            cuerpo text not null unique, 
            tematica_id integer not null, 
            dificultad_id integer not null,
            foreign key (tematica_id) references Tematica (tematica_id),
            foreign key (dificultad_id) references Dificultad (dificultad_id)'''
bd.crear_tabla('Pregunta', cadena3)

cadena4 = '''id integer primary key, 
            cuerpo text not null, 
            correcta integer default 0, 
            pregunta_id integer not null,
            foreign key (pregunta_id) references Pregunta (pregunta_id)'''
bd.crear_tabla('Respuesta', cadena4)


# Llenar la tabla Dificultad
bd = Sqlite('trivial_sqlite.db')

bd.insertar_registro('Dificultad', 'nombre','elemental')
bd.insertar_registro('Dificultad', 'nombre', 'básica')
bd.insertar_registro('Dificultad', 'nombre', 'media')
bd.insertar_registro('Dificultad', 'nombre', 'alta')
bd.insertar_registro('Dificultad', 'nombre', 'muy alta')
bd.insertar_registro('Dificultad', 'nombre', 'extrema')


# Llenar la tabla Tematica
bd = Sqlite('trivial_sqlite.db')

bd.insertar_registro('Tematica', 'nombre','General')
bd.insertar_registro('Tematica', 'nombre', 'Geografía')
bd.insertar_registro('Tematica', 'nombre', 'Historia')
bd.insertar_registro('Tematica', 'nombre', 'Deportes')


# Llenar la tabla Pregunta
bd = Sqlite('trivial_sqlite.db')



bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La capital de Francia es?,2,1')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'El rio Ebro desemboca en?,2,1')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'España se unió a la Comunidad Europea en el año?,3,3')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'España ganó su primer mundial de fútbol en el año?,4,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Los árabes invadieron la península ibérica en el año?,3,3')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'El hombre pisó la Luna por primera vez en el año?,3,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Río navegable de la península ibérica?,2,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'En la marathón se corre una distancia de?,4,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La capital de Ucrania es?,2,1')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La capital de Alemania es?,2,1')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La capital de Paises Bajos es?,2,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Equipo que ganó la copa del Rey en la temporada 2021-2022?,4,3')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La altura de Sevilla sobre el nivel del mar es de?,2,4')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'El continente americano se descubrió en el año?,3,2')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La referencia del nivel del mar en España se toma en?,2,4')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Nuestra campeona Carolina Marín nació en?,4,4')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'La gripe española de 1918 disminuyó la población mundial en?,3,5')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Cuántos años tardó el juego del Trivial en popularizarse?,1,4')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'Qué probabilidad habrá de contagarse de COVID en la feria de Sevilla?,1,1')
bd.insertar_registro('Pregunta', 'cuerpo,tematica_id,dificultad_id',
                                'En el famoso motín de la Bounty qué valiosa carga se tiró por la borda?,3,5')

#  ---------  para la de Trivial 20 ---------

bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '3,España se unió a la Comunidad Europea en el año?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '4,España ganó su primer mundial de fútbol en el año?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '3,Los árabes invadieron la península ibérica en el año?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '3,El hombre pisó la Luna por primera vez en el año?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,Río navegable de la península ibérica?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '4,En la marathón se corre una distancia de?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,La capital de Ucrania es?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,La capital de Alemania es?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,La capital de Paises Bajos es?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '4,Equipo que ganó la copa del Rey en la temporada 2021-2022?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,La altura de Sevilla sobre el nivel del mar es de?')

bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '2,La referencia del nivel del mar en España se toma en?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '4,Nuestra campeona Carolina Marín nació en?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '3,La gripe española de 1918 disminuyó la población mundial en?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '1,Cuántos años tardó el juego del Trivial en popularizarse?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '1,Qué probabilidad habrá de contagarse de COVID en la feria de Sevilla?')
bd.insertar_registro('juego_pregunta', 'tematica_id,texto',
                                '3,En el famoso motín de la Bounty qué valiosa carga se tiró por la borda?')



# Llenar la tabla Respuesta
bd = Sqlite('trivial_sqlite.db')



# Cargando la tabla Respuesta
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Roma,0,1')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Bruselas,0,1')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'París,1,1')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Lyon,0,1')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Mar Cantábrico,0,2')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Mar Mediterraneo,1,2')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Oceano Atlántico,0,2')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Mar del Norte,0,2')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1985,0,3')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1992,0,3')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '2000,0,3')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1986,1,3')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '2006,0,4')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '2008,0,4')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '2010,1,4')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '2014,0,4')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '711,1,5')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '911,0,5')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1212,0,5')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1024,0,5')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1963,0,6')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1965,0,6')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1969,1,6')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1970,0,6')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Ebro,0,7')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Tajo,0,7')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Duero,0,7')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Guadalquivir,1,7')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '40 kilómetros,0,8')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '41 kilómetros,0,8')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '42 kilómetros,1,8')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '44 kilómetros,0,8')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Estambul,0,9')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Kiev,1,9')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Varsovia,0,9')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Moscú,0,9')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Berlín,1,10')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Munich,0,10')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Bohn,0,10')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Dusseldorf,0,10')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Bruselas,0,11')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Brujas,0,11')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Amsterdam,1,11')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'La Haya,0,11')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Barcelona,0,12')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Betis,1,12')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Villarreal,0,12')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Valencia,0,12')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '7 metros,1,13')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '9 metros,0,13')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '14 metros,0,13')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '82 metros,0,13')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1490,0,14')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1492,1,14')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1592,0,14')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '1522,0,14')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Albacete,0,15')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Alicante,1,15')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Almería,0,15')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Elche,0,15')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Huelva,1,16')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Badajoz,0,16')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Córdoba,0,16')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Cádiz,0,16')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'un 1%,0,17')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'un 3%,0,17')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'un 6%,0,17')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'un 2%,1,17')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '4,0,18')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '5,0,18')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '6,1,18')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '8,0,18')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '20%,0,19')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '40%,0,19')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '30%,1,19')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                '50%,0,19')

bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'Oro,0,20')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'plantas de café,0,20')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'especias,0,20')
bd.insertar_registro('Respuesta', 'cuerpo,correcta,pregunta_id',
                                'plantas del árbol del pan,1,20')

