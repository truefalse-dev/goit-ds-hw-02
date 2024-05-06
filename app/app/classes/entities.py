class User:
    def __init__(self, row):
        self.row = row

    def result(self):
        return f"id: {self.row[0]} / fullname: {self.row[1]}... / email: {self.row[2]}"


class Task:
    def __init__(self, row):
        self.row = row

    def result(self):
        return f"id: {self.row[0]} / title: {"{0}".format(str(self.row[1])[:20])}... / user: {self.row[3]} / status: {self.row[2]}"
