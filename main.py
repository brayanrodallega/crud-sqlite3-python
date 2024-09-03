import sqlite3

def sql_connection():
    try:
        conn = sqlite3.connect('estudiantes.db')
        return conn
    except Exception as e:
        print(e)
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ESTUDIANTES(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            IDENTIFICACION INTEGER NOT NULL,
            NOMBRE VARCHAR(20) NOT NULL,
            APELLIDO VARCHAR(30) NOT NULL,
            GENERO VARCHAR(1) NOT NULL,
            FECHA_NAC DATE NOT NULL,
            CORREO VARCHAR(50) NOT NULL,
            CALIFICACION INTEGER
        )
        ''')
        conn.commit()
        print('Tabla creada exitosamente')
    except Exception as e:
        print(e)

def insert_data(conn, identificacion, nombre, apellido, genero, fecha_nac, correo, calificacion):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO ESTUDIANTES (IDENTIFICACION, NOMBRE, APELLIDO, GENERO, FECHA_NAC, CORREO, CALIFICACION)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (identificacion, nombre, apellido, genero, fecha_nac, correo, calificacion))
        conn.commit()
        print('Datos insertados exitosamente')
    except Exception as e:
        print(e)

def select_all(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ESTUDIANTES')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

def update_data(conn, id, calificacion):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE ESTUDIANTES
        SET CALIFICACION = ?
        WHERE ID = ?
        ''', (calificacion, id))
        conn.commit()
        print('Datos actualizados exitosamente')
    except Exception as e:
        print(e)

def delete_data(conn, id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM ESTUDIANTES
        WHERE ID = ?
        ''', (id,))
        conn.commit()
        print('Datos eliminados exitosamente')
    except Exception as e:
        print(e)


def main():
    conn = sql_connection()
    create_table(conn)
    insert_data(conn, 123456, 'Juan', 'Perez', 'M', '1990-01-01', 'juanperez@example.com', 90)
    insert_data(conn, 654321, 'Maria', 'Lopez', 'F', '1995-05-05', 'marialopez@example.com', 85)
    insert_data(conn, 456789, 'Pedro', 'Gomez', 'M', '1992-10-10', 'pedrogomez@example.com', 95)
    select_all(conn)
    update_data(conn, 1, 100)
    select_all(conn)
    delete_data(conn, 2)
    select_all(conn)
    conn.close()

if __name__ == '__main__':
    main()