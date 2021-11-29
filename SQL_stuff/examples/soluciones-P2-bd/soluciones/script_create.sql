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
	CodPais INT NOT NULL CONSTRAINT pk_paises PRIMARY KEY,
	NombrePais VARCHAR(50) NOT NULL UNIQUE
	);

-- 4.2. Tabla "Peliculas"
CREATE TABLE Peliculas
	(
	CodPelicula INT NOT NULL IDENTITY (1,1) CONSTRAINT pk_peliculas PRIMARY KEY,
	Titulo VARCHAR(200) NOT NULL,
	TituloOriginal VARCHAR(200),
	Pais INT NOT NULL,
	Anyo CHAR(4) CHECK(Anyo LIKE '[0-9][0-9][0-9][0-9]'),
	Presupuesto DECIMAL(6,2) NOT NULL,
	CONSTRAINT fk_Peliculas_Paises FOREIGN KEY (Pais) REFERENCES Paises(CodPais)
	);

-- 5. Resto de tablas
-- 5.1. Tabla "Valoraciones"
CREATE TABLE Valoraciones
	(
	CodValoracion INT NOT NULL IDENTITY(1,1) CONSTRAINT pk_valoraciones PRIMARY KEY,
	Comentario TEXT,
	Puntuacion INT NOT NULL CHECK (Puntuacion >=1 AND Puntuacion <=5),
	Pelicula INT NOT NULL,
	CONSTRAINT fk_Valoraciones_Peliculas FOREIGN KEY (Pelicula) REFERENCES Peliculas(CodPelicula)
	);

-- 5.2. Tabla "Actores"
CREATE TABLE Actores
	(
	CodActor INT NOT NULL IDENTITY(1,1) CONSTRAINT pk_actores PRIMARY KEY,
	NombreArtistico VARCHAR(100) NOT NULL
	);

-- 5.3. Tabla "Reparto"
CREATE TABLE Reparto
	(
	CodReparto INT NOT NULL IDENTITY(1,1) CONSTRAINT pk_reparto PRIMARY KEY,
	CodPelicula INT NOT NULL,
	CodActor INT NOT NULL,
	Personaje VARCHAR(100) NOT NULL,
	Papel CHAR(1) NOT NULL CHECK (Papel IN ('P','S')),
	CONSTRAINT fk_reparto_peliculas FOREIGN KEY (CodPelicula) REFERENCES Peliculas(CodPelicula),
	CONSTRAINT fk_reparto_actores FOREIGN KEY (CodActor) REFERENCES Actores(CodActor)
	);

