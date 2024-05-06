from faker import Faker

class Seed:
    def __init__(self, cur):
        self.fake = Faker()
        self.cur = cur

    def users(self):
        list = []
        for i in range(9):
            list.append(
                (
                    self.fake.name(), 
                    f"test{i}@gmail.com" if i > 4 else self.fake.email()
                )
            )

        res = str(list).strip('[]')

        self.cur.execute(f"INSERT INTO users (`fullname`,`email`) VALUES {res}")
        self.cur.commit()


    def status(self):
        self.cur.execute("""INSERT INTO status (`name`) VALUES ('new'), ('in_progress'), ('completed')""")
        self.cur.commit()


    def tasks(self, count):
        list = []
        for i in range(count):
            list.append(
                (
                    self.fake.text(), 
                    self.fake.text(),
                    self.fake.random_int(1,3),
                    self.fake.random_int(1,6)
                )
            )

        res = str(list).strip('[]')

        self.cur.execute(f"INSERT INTO tasks (`title`, `description`, `status_id`, `user_id`) VALUES {res}")
        self.cur.commit()
