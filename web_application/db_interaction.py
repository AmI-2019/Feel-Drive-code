import pymysql
import os

DB_USER = 'root'
DB_PASSWORD = 'purti97'
DB_HOST = 'localhost'

ANGER = 'Anger'
HAPPINESS = 'Happiness'
SADNESS = 'Sadness'
EMOTION_LABELS = (ANGER, HAPPINESS, SADNESS)


def check_user_password(u,p):
    sql="""SELECT * FROM users 
    WHERE username=%s AND password=%s
     """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,p))
    result=cursor.fetchone()
    conn.close()
    return result


def check_user(u):
    sql="""SELECT username FROM users 
    WHERE username=%s
     """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,))
    result=cursor.fetchone()
    conn.close()
    return result


def add_user(u,p):
    sql="""INSERT INTO users(username, password) 
    VALUES (%s,%s)
     """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(u,p))
    conn.commit()
    conn.close()


def add_song(song, feeling):

    if get_song(song) is None:
        sql="""INSERT INTO songs(title, feeling)
        VALUES (%s,%s)
        """
        conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
        cursor = conn.cursor()
        cursor.execute(sql, (song, feeling))
        conn.commit()
        conn.close()


def get_song(song):
    sql="""SELECT * FROM songs 
    WHERE title=%s
    """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (song,))
    result = cursor.fetchone()
    conn.close()
    return result


def add_relation(username,song, liked, feeling):
    sql="""INSERT INTO relations(username, title, liked, feeling) 
    VALUES (%s,%s,%s,%s)
     """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor=conn.cursor()
    cursor.execute(sql,(username,song,liked, feeling))
    conn.commit()
    conn.close()


def get_liked_songs_by_feeling(username, feeling):
    sql="""SELECT song_title FROM relations
    WHERE feeling=%s AND username=%s
    """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (feeling,username))
    result = cursor.fetchall()
    conn.close()
    return result


def get_liked_songs(username):
    sql="""SELECT title FROM relations
    WHERE username=%s
    """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    result = cursor.fetchall()
    conn.close()
    return result


def delete_relation(username,song):
    sql = """DELETE FROM relations
     WHERE title=%s AND username=%s
    """
    conn=pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor=conn.cursor();
    cursor.execute(sql, (song, username))
    conn.commit()
    conn.close()



def get_songs_by_feeling(feeling):
    sql="""SELECT title FROM songs
    WHERE feeling=%s
    """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql, (feeling,))
    result = cursor.fetchall()
    conn.close()
    return result



def load_db(music_directory_path):
    os.chdir(music_directory_path)
    for emotion in EMOTION_LABELS:
        for file in os.listdir(music_directory_path+emotion):
            if file.endswith('.mp3'):
                add_song(file, emotion)



def check_user_song_relation(song,username):
    sql="""SELECT * FROM relations WHERE title=%s AND username=%s
    """
    conn = pymysql.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='feel&drive')
    cursor = conn.cursor()
    cursor.execute(sql,(song,username))
    result = cursor.fetchone()
    return  result



if __name__ == '__main__':
    get_songs_by_feeling("Sadness")
