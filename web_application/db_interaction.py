import pymysql
import os

def check_user_password(u,p):
    sql="""SELECT * FROM users 
    WHERE username=%s AND password=%s
     """
    conn=pymysql.connect(user = 'root', password='purti97',host='localhost',database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,p))
    result=cursor.fetchone()
    conn.close()
    return result

def check_user(u):
    sql="""SELECT username FROM users 
    WHERE username=%s
     """
    conn=pymysql.connect(user = 'root', password='purti97',host='localhost',database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,))
    result=cursor.fetchone()
    conn.close()
    return result

def add_user(u,p):
    sql="""INSERT INTO users(username, password) 
    VALUES (%s,%s)
     """
    conn=pymysql.connect(user = 'root', password='purti97',host='localhost',database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,p))
    conn.commit()
    conn.close()

def add_song(song, feeling):

    if get_song(song) is None:
        sql="""INSERT INTO songs(title, feeling)
        VALUES (%s,%s)
        """
        conn = pymysql.connect(user='root', password='purti97', host='localhost', database='feel&drive')
        cursor = conn.cursor()
        cursor.execute(sql, (song, feeling))
        conn.commit()
        conn.close()

def get_song(song):
    sql="""SELECT * FROM songs 
    WHERE title=%s
    """
    conn = pymysql.connect(user='root', password='purti97', host='localhost', database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (song,))
    result = cursor.fetchone()
    conn.close()
    return result


def add_relation(username,song, liked, feeling):
    sql="""INSERT INTO relations(username, title, liked, feeling) 
    VALUES (%s,%s,%s,%s)
     """
    conn=pymysql.connect(user = 'root', password='purti97',host='localhost',database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(username,song,liked, feeling))
    conn.commit()
    conn.close()


def get_liked_songs_by_feeling(username, feeling):
    sql="""SELECT song_title FROM relations
    WHERE feeling=%s AND username=%s
    """
    conn = pymysql.connect(user='root', password='purti97', host='localhost', database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (feeling,username))
    result = cursor.fetchall()
    conn.close()
    return result

def get_songs_by_feeling( feeling):
    sql="""SELECT title FROM songs
    WHERE feeling=%s
    """
    conn = pymysql.connect(user='root', password='purti97', host='localhost', database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (feeling,))
    result = cursor.fetchall()
    conn.close()
    return result


def load_db():
   dir='C:/Users/Pietro/Desktop/Feel & Drive/music/Sadness'
   os.chdir(dir)
   for file in os.listdir(dir):
       if file.endswith('.mp3'):
            add_song(file,'Sadness')



if __name__ == '__main__':
    load_db()