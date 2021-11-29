/*
 * PRÁCTICA 2.
 * Script con instrucciones INSERT
 */

-- 6. Cargamos datos en las tablas mediante la sentencia INSERT
-- Tabla "Paises"
INSERT INTO Paises VALUES (1, 'España');
INSERT INTO Paises VALUES (2, 'Estados Unidos');
INSERT INTO Paises VALUES (3, 'Reino Unido');
INSERT INTO Paises VALUES (4, 'Alemania');
INSERT INTO Paises VALUES (5, 'Italia');

SELECT * FROM Paises;

-- Tabla "Peliculas"
-- Pelicula sin TituloOriginal
INSERT INTO Peliculas(Titulo, Pais, Anyo, Presupuesto) VALUES ('Ocho apellidos vascos', 1, '2014', 3.5);
INSERT INTO Peliculas(Titulo, TituloOriginal, Pais, Anyo, Presupuesto) 
	VALUES ('El lado bueno de las cosas', 'Silver Linings Playbook', 3, '2012', 21.0);
INSERT INTO Peliculas(Titulo, TituloOriginal, Pais, Anyo, Presupuesto) 
	VALUES ('Los juegos del hambre', 'The Hunger Games', 3, '2012', 78.0);
INSERT INTO Peliculas(Titulo, TituloOriginal, Pais, Anyo, Presupuesto) 
	VALUES ('Descifrando Enigma', 'The Imitation Game', 4, '2014', 15.0);
INSERT INTO Peliculas(Titulo, TituloOriginal, Pais, Anyo, Presupuesto) 
	VALUES ('La teoría del todo', 'The Theory of Everything', 4, '2014', 15.0);
-- Pelicula sin Presupuesto
INSERT INTO Peliculas(Titulo, TituloOriginal, Pais, Anyo) 
	VALUES ('Probando', 'Testing', 4, '2014');
SELECT * FROM Peliculas;

-- *** EJEMPLO DE INSERT QUE BUSCA EL VALOR DE LAS FKs ***
INSERT INTO Peliculas(Titulo, Pais, Anyo, Presupuesto) 
	SELECT 'Ocho apellidos vascos', CodPais, '2014', 3.5
		FROM Paises WHERE NombrePais LIKE 'España';

-- Tabla "Valoraciones"
INSERT INTO Valoraciones(Comentario, Puntuacion, Pelicula)
	VALUES ('Muchas risas', 4, 1);
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (3, 1);
INSERT INTO Valoraciones(Comentario, Puntuacion, Pelicula)
	VALUES ('No es para tanto', 2, 2);
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (3, 2);
INSERT INTO Valoraciones(Comentario, Puntuacion, Pelicula)
	VALUES ('100% recomendable', 5, 3);
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (4, 3);
INSERT INTO Valoraciones(Comentario, Puntuacion, Pelicula)
	VALUES ('Me gustó', 4, 4);
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (1, 4);
INSERT INTO Valoraciones(Comentario, Puntuacion, Pelicula)
	VALUES ('Ni fu ni fa', 3, 5);
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (2, 5);
-- Valoracion sin Pelicula que exista
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (2, 25);
SELECT * FROM Valoraciones;

-- Intentamos cargar la valoración de una película que no esté en la tabla "Peliculas"
INSERT INTO Valoraciones(Puntuacion, Pelicula)
	VALUES (2, 15);

-- Tabla "Actores"
INSERT INTO Actores(NombreArtistico) VALUES ('Dani Rovira');
INSERT INTO Actores(NombreArtistico) VALUES ('Carmen Machi');
INSERT INTO Actores(NombreArtistico) VALUES ('Jennifer Lawrence');
INSERT INTO Actores(NombreArtistico) VALUES ('Bradley Cooper');
INSERT INTO Actores(NombreArtistico) VALUES ('Josh Hutcherson');
INSERT INTO Actores(NombreArtistico) VALUES ('Lenny Kravitz');
INSERT INTO Actores(NombreArtistico) VALUES ('Benedict Cumberbatch');
INSERT INTO Actores(NombreArtistico) VALUES ('Keira Knightley');
INSERT INTO Actores(NombreArtistico) VALUES ('Eddie Redmayne');
INSERT INTO Actores(NombreArtistico) VALUES ('Felicity Jones');
-- Actor que no va a aparecer en ninguna película
INSERT INTO Actores(NombreArtistico) VALUES ('Johnny Depp');

SELECT * FROM Actores;

-- Tabla "Reparto"
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (1, 1, 'Rafael "Rafa" Quirós', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (1, 2, 'Mercedes "Merche"', 'S');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (2, 3, 'Tiffany Maxwell', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (2, 4, 'Patrizio "Pat Jr." Solitano', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (3, 3, 'Katniss Everdeen', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (3, 5, 'Peeta Mellark', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (3, 6, 'Cinna', 'S');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (4, 7, 'Alan Turing', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (4, 8, 'Joan Clarke', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (5, 9, 'Stephen Hawking', 'P');
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (5, 10, 'Jane Hawking', 'P');
-- Intentamos cargar un actor que no esté en la tabla Actores
INSERT INTO Reparto (CodPelicula, CodActor, Personaje, Papel)
	VALUES (5, 150, 'Probando', 'P');
SELECT * FROM Reparto;








