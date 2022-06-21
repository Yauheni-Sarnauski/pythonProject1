import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

def table_exists(table_name):
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name))
    if cursor.fetchone()[0] == 1:
        return True
    return False

if not table_exists('movies'):
    cursor.execute(''' 
        CREATE TABLE movies(movie_id INTEGER, name TEXT, release_year INTEGER, genre TEXT ) ''')

movie_id= int(input('Введите id:  '))
name = str(input('Введите название фильма:  '))
release_year = int(input('Введите год релиза:  '))
genre = str(input('Введите жанр фильма:  '))
while True:
    def insert_movie(movie_id, name, release_year, genre):
        cursor.execute(''' INSERT INTO movies (movie_id, name, release_year, genre) VALUES(?, ?, ?, ?) ''', (movie_id, name, release_year, genre))
        conn.commit()

    def get_movies():
        cursor.execute('''SELECT * FROM movies''')
        data = []
        for row in cursor.fetchall():
            data.append(row)
        return data

    def get_movie(movie_id):
        cursor.execute('''SELECT * FROM movies WHERE movie_id = {}'''.format(movie_id))
        data = []
        for row in cursor.fetchall():
            data.append(row)
        return data



    def exit(movie_id):
        cursor.execute('''DELETE FROM movies WHERE movie_id = {}'''.format(movie_id))
        conn.commit()

    #
    insert_movie(1, 'Revealer', 2022, 'Horrors')
    insert_movie(2, 'Rush', 2013, 'Biography')
    insert_movie(3, 'Spider-Man', 2021, 'Fantastic')
    insert_movie(4, 'Knockdown', 2005, 'Biography')
    insert_movie(5, 'Adventures', 2006, 'Romance')

    print(get_movies())
    print(get_movie(6))

