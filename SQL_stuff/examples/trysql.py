import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password='alumnos',
            db='filmoteca'
        )

        self.cursor = self.connection.cursor()

        print("Connection stablished")


    def select_film(self, codFilm):
        sql = 'SELECT CodPelicula, Titulo, Pais FROM Peliculas WHERE codPelicula = {}'.format(codFilm)

        try:
            self.cursor.execute(sql)
            peli = self.cursor.fetchone()

            print("CodPeli:", peli[0])
            print("Titulo:", peli[1])
            print("Pais:", peli[2])
            
        except Exception as e:
            raise

    def select_all_films(self):
        sql = 'SELECT CodPelicula, Titulo, Pais FROM Peliculas'

        try:
            self.cursor.execute(sql)
            pelis = self.cursor.fetchall()

            for peli in pelis:
                
                print("CodPeli:", peli[0])
                print("Titulo:", peli[1])
                print("Pais:", peli[2])
                print("_________\n")

        except Exception as e:
            raise


    def update_film(self, codFilm, filmTitle):
        sql = "UPDATE Peliculas SET Titulo='{}' WHERE CodPelicula={}".format(filmTitle, codFilm)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        
        except Exception as e:
            raise


    def close(self):
        self.connection.close()
        
database = DataBase()

database.select_film(2)

#database.select_all_films()

database.update_film(2, 'El lado bueno de las cosasss')

database.select_film(2)

database.close()
