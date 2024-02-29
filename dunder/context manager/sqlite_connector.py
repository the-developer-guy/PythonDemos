import sqlite3


class DBConnector:

    def __init__(self, filename="kvstorage.db") -> None:
        self.filename = filename

    def open(self):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS storage(id INTEGER PRIMARY KEY, key TEXT, value TEXT)")
        self.connection.commit()

    def close(self):
        self.connection.close()

    def get_id(self, key):
        self.cursor.execute("SELECT id FROM storage WHERE key=?", (key,))
        id = self.cursor.fetchone()
        return id

    def get(self, key):
        self.cursor.execute("SELECT value FROM storage WHERE key=?", (key,))
        return self.cursor.fetchone()

    def set(self, key, value):
        id = self.get_id(key)
        if id is None:
            self.cursor.execute("INSERT INTO storage(key, value) VALUES (?,?)",
                                (key, value))
        else:
            self.cursor.execute("UPDATE storage SET key=?, value=? WHERE id=?",
                                (key, value, id[0]))
        self.connection.commit()

    def dump(self):
        self.cursor.execute("SELECT * FROM storage")
        for item in self.cursor.fetchall():
            print(item)

    def faulty_command(self):
        self.cursor.execute("INSERT INTO storage(key, value, incorrect) VALUES ('whatever', 5, 9001)")
        print("Do we get this far?")
        self.connection.commit()

    def __enter__(self):
        print("Entering context manager")
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving context manager")
        if exc_type is not None:
            print(f"Context manager found an Excepion: {exc_type}")
            self.connection.rollback()
        self.close()
        return True


if __name__ == "__main__":
    connector = DBConnector()

    connector.open()
    connector.set("Joe", "banjoe")
    print(connector.get("Joe"))
    connector.dump()
    try:
        connector.faulty_command()
    except Exception as e:
        print(f"We got an error: {e}")
    connector.close()

    with connector as conn:
        conn.set("Joe", "bananajoe")
        conn.set("Billy", "guitar")
        print(conn.get("Billy"))
        conn.dump()
        conn.faulty_command()
        print("Last moves in connector context")
