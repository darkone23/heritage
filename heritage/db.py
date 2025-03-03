import sqlite3
import time


from pathlib import Path


class SQLiteCache:

    @staticmethod
    def get_cache_dir():
        p = Path.home() / ".cache/sanskrit-heritage"
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
        return p

    def __init__(self, db_path=":memory:"):  # Use a file or in-memory database
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Creates the cache table with an optional expiration column."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT,
                expires_at INTEGER
            )
        """
        )
        self.conn.commit()

    def set(self, key, value, ttl=None):
        """Insert or update a key-value pair with optional TTL (time-to-live in seconds)."""
        expires_at = int(time.time()) + ttl if ttl else None
        self.cursor.execute(
            """
            INSERT INTO cache (key, value, expires_at) 
            VALUES (?, ?, ?) 
            ON CONFLICT(key) DO UPDATE SET value=excluded.value, expires_at=excluded.expires_at
        """,
            (key, value, expires_at),
        )
        self.conn.commit()

    def get(self, key):
        """Retrieve a value by key, ensuring it has not expired."""
        self.cursor.execute("SELECT value, expires_at FROM cache WHERE key = ?", (key,))
        row = self.cursor.fetchone()
        if row:
            value, expires_at = row
            if expires_at and expires_at < int(time.time()):  # Check if expired
                self.delete(key)
                return None
            return value
        return None

    def delete(self, key):
        """Remove a key from the cache."""
        self.cursor.execute("DELETE FROM cache WHERE key = ?", (key,))
        self.conn.commit()

    def clear(self):
        """Clear the entire cache."""
        self.cursor.execute("DELETE FROM cache")
        self.conn.commit()

    def __del__(self):
        """Close the connection on destruction."""
        self.conn.close()


if __name__ == "__main__":
    # Usage example
    cache = SQLiteCache(
        SQLiteCache.get_cache_dir() / "example.db"
    )  # Persistent file-based DB
    cache.set("username", "sanskrit_enthusiast", ttl=5)
    print(cache.get("username"))  # Output: "sanskrit_enthusiast"
    t = 7
    print(f"sleeping: {t}s")
    time.sleep(t)
    print(cache.get("username"))  # Output: None (expired)

    from sh import rm
    import sys

    rm(*["-rf", SQLiteCache.get_cache_dir()], _out=sys.stdout, _err=sys.stderr)
