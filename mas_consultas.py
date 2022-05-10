from sql import Sqlite

bd = Sqlite('trivial.sqlite3')
a = bd.leer_tabla('juego_tematica')
print(a)




# Cargando la tabla juego_respuesta


bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1985,0,3')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1992,0,3')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '2000,0,3')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1986,1,3')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '2006,0,4')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '2008,0,4')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '2010,1,4')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '2014,0,4')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '711,1,5')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '911,0,5')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1212,0,5')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1024,0,5')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1963,0,6')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1965,0,6')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1969,1,6')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '1970,0,6')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Ebro,0,7')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Tajo,0,7')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Duero,0,7')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Guadalquivir,1,7')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '40 kilómetros,0,8')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '41 kilómetros,0,8')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '42 kilómetros,1,8')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '44 kilómetros,0,8')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Estambul,0,9')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Kiev,1,9')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Varsovia,0,9')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Moscú,0,9')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Berlín,1,10')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Munich,0,10')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Bohn,0,10')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Dusseldorf,0,10')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Bruselas,0,11')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Brujas,0,11')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Amsterdam,1,11')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'La Haya,0,11')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Barcelona,0,12')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Betis,1,12')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Villarreal,0,12')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Valencia,0,12')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '7 metros,1,13')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '9 metros,0,13')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '14 metros,0,13')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '82 metros,0,13')



bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Albacete,0,15')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Alicante,1,15')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Almería,0,15')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Elche,0,15')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Huelva,1,16')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Badajoz,0,16')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Córdoba,0,16')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Cádiz,0,16')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'un 1%,0,17')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'un 3%,0,17')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'un 6%,0,17')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'un 2%,1,17')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '4,0,18')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '5,0,18')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '6,1,18')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '8,0,18')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '20%,0,19')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '40%,0,19')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '30%,1,19')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                '50%,0,19')

bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'Oro,0,20')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'plantas de café,0,20')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'especias,0,20')
bd.insertar_registro('juego_respuesta', 'texto,correcta,pregunta_id',
                                'plantas del árbol del pan,1,20')