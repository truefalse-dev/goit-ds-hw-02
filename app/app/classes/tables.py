class Tables:
    def __init__(self, cur):
        self.cur = cur

    def create(self):
        self.cur.execute("""DROP TABLE IF EXISTS users""")
        self.cur.execute("""CREATE TABLE users(
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `fullname` varchar(100) NOT NULL,
            `email` varchar(32) UNIQUE NOT NULL
            )""")
        
        self.cur.execute("""DROP TABLE IF EXISTS status""")
        self.cur.execute("""CREATE TABLE status(
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `name` varchar(50) NOT NULL
            )""")
        
        self.cur.execute("""DROP TABLE IF EXISTS tasks""")
        self.cur.execute("""CREATE TABLE tasks(
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `title` varchar(100) NOT NULL,
            `description` TEXT NULL,
            `status_id` INT,
            `user_id` INT,
            FOREIGN KEY(status_id) REFERENCES status(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            FOREIGN KEY(user_id) REFERENCES users(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            )""")
        
        self.cur.execute("""CREATE INDEX index_tasks ON tasks (status_id, user_id)""")
