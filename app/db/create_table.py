from app.db.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(100) NOT NULL,
            amount FLOAT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table ready!")