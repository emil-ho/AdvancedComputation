/*
 * PRÁCTICA 2.
 * SELECT, UPDATE y DELETE.
 */

-- 7. Instrucción SELECT
-- a. Obtener todos los datos de la tabla "Peliculas"
SELECT * FROM Peliculas;

-- b. Obtener todos los datos de la tabla "Valoraciones"
SELECT * FROM Valoraciones;

-- c. Obtener todos los datos de la tabla "Actores"
SELECT * FROM Actores;

-- d. Realizar una consulta que muestre toda la información de las Peliculas junto a sus Valoraciones (VARIAS FORMAS)
SELECT * FROM Peliculas, Valoraciones
	WHERE Peliculas.CodPelicula = Valoraciones.Pelicula;

SELECT Peliculas.*, Valoraciones.* FROM Peliculas, Valoraciones
	WHERE Peliculas.CodPelicula = Valoraciones.Pelicula;

SELECT * FROM Peliculas
	INNER JOIN Valoraciones ON Peliculas.CodPelicula = Valoraciones.Pelicula;

SELECT Peliculas.*, Valoraciones.* FROM Peliculas
	INNER JOIN Valoraciones ON Peliculas.CodPelicula = Valoraciones.Pelicula;

-- e. Realizar de nuevo la consulta anterior pero mostrando solo el Titulo de la Pelicula y la Puntuacion y Comentario de las Valoraciones (VARIAS FORMAS)
SELECT p.Titulo, v.Comentario, v.Puntuacion FROM Peliculas AS p, Valoraciones AS v
	WHERE p.CodPelicula = v.Pelicula;

SELECT p.Titulo, v.Comentario, v.Puntuacion FROM Peliculas p
	INNER JOIN Valoraciones v ON p.CodPelicula = v.Pelicula;

-- f. Realizar una consulta que muestre toda la información de las Peliculas junto a sus Actores (VARIAS FORMAS)
SELECT p.*, a.*, r.* FROM Peliculas p
	INNER JOIN Reparto r ON p.CodPelicula = r.CodPelicula
	INNER JOIN Actores a ON r.CodActor = a.CodActor;

SELECT p.*, a.*, r.* FROM Peliculas p, Reparto r, Actores a
	WHERE r.CodPelicula = p.CodPelicula AND r.CodActor = a.CodActor;

-- g. Realizar la consulta anterior pero mostrando solo el Titulo de las Peliculas, el NombreArtistico de los Actores
-- y el Personaje que interpretan (VARIAS FORMAS)
SELECT p.Titulo, a.NombreArtistico, r.Personaje FROM Peliculas p
	INNER JOIN Reparto r ON p.CodPelicula = r.CodPelicula
	INNER JOIN Actores a ON r.CodActor = a.CodActor;

SELECT p.Titulo, a.NombreArtistico, r.Personaje FROM Peliculas p, Reparto r, Actores a
	WHERE r.CodPelicula = p.CodPelicula AND r.CodActor = a.CodActor;


-- 8. Instrucción UPDATE
-- a. Intentar actualizar el código  de un país de la tabla Países que aparezca en alguna fila de Peliculas
UPDATE Paises SET CodPais = 100
	WHERE CodPais = 1;

-- b. Intentar actualizar el código de un actor de la tabla Actores que aparezca en alguna fila de la tabla Reparto
UPDATE Actores SET CodActor = 100
	WHERE CodActor = 1;

-- c. Intentar actualizar el personaje de una fila cualquiera de la tabla Reparto
UPDATE Reparto SET Personaje = 'Katniss Everdeen "La chica en llamas"'
	WHERE Personaje LIKE 'Katniss Everdeen';
SELECT * FROM Reparto;


-- 9. Instrucción DELETE
-- a. Intentar borrar todas las Peliculas
DELETE FROM Peliculas;

-- b. Intentar borrar todos los Actores
DELETE FROM Actores;

-- c. Borrar un actor que no actúe en ninguna película
DELETE FROM Actores
	WHERE NombreArtistico LIKE 'Johnny Depp';
SELECT * FROM Actores;