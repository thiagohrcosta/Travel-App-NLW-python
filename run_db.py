import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS trips (
                        id TEXT PRIMARY KEY,
                        destination TEXT NOT NULL,
                        start_date DATETIME,
                        end_date DATETIME,
                        owner_name TEXT NOT NULL,
                        owner_email TEXT NOT NULL,
                        status INTEGER
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS emails_to_invite (
                        id TEXT PRIMARY KEY,
                        trip_id TEXT,
                        email TEXT NOT NULL,
                        FOREIGN KEY (trip_id) REFERENCES trips(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS links (
                        id TEXT PRIMARY KEY,
                        trip_id TEXT,
                        link TEXT NOT NULL,
                        title TEXT NOT NULL,
                        FOREIGN KEY (trip_id) REFERENCES trips(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS participants (
                        id TEXT PRIMARY KEY,
                        trip_id TEXT NOT NULL,
                        emails_to_invite_id TEXT NOT NULL,
                        name TEXT NOT NULL,
                        is_confirmed INTEGER,
                        FOREIGN KEY (trip_id) REFERENCES trips(id),
                        FOREIGN KEY (emails_to_invite_id) REFERENCES emails_to_invite(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS activities (
                        id TEXT PRIMARY KEY,
                        trip_id TEXT NOT NULL,
                        title TEXT NOT NULL,
                        occurs_at DATETIME,
                        FOREIGN KEY (trip_id) REFERENCES trips(id)
                    )''')

    conn.commit()

    print("Tables successfully created.")

def main():
    try:
        # DB Connection
        conn = sqlite3.connect('storage.db')
        print("SQLite connection is active.")

        create_tables(conn)

    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        if conn:
            conn.close()
            print("SQLite connection closed.")

if __name__ == '__main__':
    main()
