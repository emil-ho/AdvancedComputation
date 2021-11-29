/*
 * PRÁCTICA 2
 * Script con instrucciones CREATE
 */

-- 2. Crear la base de datos "Filmoteca"
CREATE DATABASE Filmoteca;

-- 3. Conectarse a la BD "Filmoteca"
USE Filmoteca;

-- 4. Crear las tablas de la base de datos "Filmoteca"
-- 4.1. Tabla "Paises"
CREATE TABLE Paises 
	(
	CodPais INT NOT NULL,
	NombrePais VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (CodPais)
	);

-- 4.2. Tabla "Peliculas"
CREATE TABLE Peliculas
	(
	CodPelicula INT NOT NULL auto_increment ,
	Titulo VARCHAR(200) NOT NULL,
	TituloOriginal VARCHAR(200),
	Pais INT NOT NULL,
	Anyo CHAR(4) CHECK(Anyo LIKE '[0-9][0-9][0-9][0-9]'),
	Presupuesto DECIMAL(6,2) NOT NULL,
	CONSTRAINT fk_Peliculas_Paises FOREIGN KEY (Pais) REFERENCES Paises(CodPais),
    PRIMARY KEY (CodPelicula)
	);

-- 5. Resto de tablas
-- 5.1. Tabla "Valoraciones"
CREATE TABLE Valoraciones
	(
	CodValoracion INT NOT NULL auto_increment ,
	Comentario TEXT,
	Puntuacion INT NOT NULL CHECK (Puntuacion >=1 AND Puntuacion <=5),
	Pelicula INT NOT NULL,
	CONSTRAINT fk_Valoraciones_Peliculas FOREIGN KEY (Pelicula) REFERENCES Peliculas(CodPelicula),
    PRIMARY KEY (CodValoracion)
	);

-- 5.2. Tabla "Actores"
CREATE TABLE Actores
	(
	CodActor INT NOT NULL auto_increment ,
	NombreArtistico VARCHAR(100) NOT NULL,
    PRIMARY KEY (CodActor)
	);

-- 5.3. Tabla "Reparto"
CREATE TABLE Reparto
	(
	CodReparto INT NOT NULL auto_increment,
	CodPelicula INT NOT NULL,
	CodActor INT NOT NULL,
	Personaje VARCHAR(100) NOT NULL,
	Papel CHAR(1) NOT NULL CHECK (Papel IN ('P','S')),
	CONSTRAINT fk_reparto_peliculas FOREIGN KEY (CodPelicula) REFERENCES Peliculas(CodPelicula),
	CONSTRAINT fk_reparto_actores FOREIGN KEY (CodActor) REFERENCES Actores(CodActor),
    PRIMARY KEY (CodReparto)
	);

