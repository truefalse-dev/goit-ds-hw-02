from app.core.db import DbConnection
from app.classes.tables import Tables
from app.classes.seed import Seed
from app.classes.entities import User, Task

def create_tables(cur):
    Tables(cur).create()   
    
def seed(cur):
    Seed(cur).users()
    Seed(cur).status()
    Seed(cur).tasks(20)

def init():
    cur = DbConnection().cursor()

    create_tables(cur)
    seed(cur)

    cur.close()

def main():
    cur = DbConnection().cursor()

    task_select_query = "SELECT t.id, title, name, fullname, email FROM tasks t INNER JOIN status s ON(t.status_id = s.id) INNER JOIN users u ON(t.user_id = u.id)"
    
    print("1. Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.\n")
    for row in cur.execute(f"{task_select_query} WHERE user_id = 3"):
        print(Task(row).result())

    print("\n2. Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.\n")
    for row in cur.execute(f"{task_select_query} WHERE s.name = 'new'"):
        print(Task(row).result())

    print("\n3. Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.\n")
    cur.execute("UPDATE tasks SET status_id = 1 WHERE id = 2")
    row = cur.execute(f"{task_select_query} WHERE t.id = 2").fetchone()
    print(Task(row).result())
    cur.execute("UPDATE tasks SET status_id = 2 WHERE id = 2")
    row = cur.execute(f"{task_select_query} WHERE t.id = 2").fetchone()
    print(Task(row).result())

    print("\n4. Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.\n")
    for row in cur.execute(f"SELECT id, fullname, email FROM users WHERE id NOT IN (SELECT user_id FROM tasks)"):
        print(User(row).result())

    print("\n5. Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.\n")
    cur.execute(f"INSERT INTO tasks (title, user_id, status_id) VALUES ('New task ro user 4', 4, 1)")
    for row in cur.execute(f"{task_select_query} WHERE user_id = 4"):
        print(Task(row).result())

    print("\n6. Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.\n")
    for row in cur.execute(f"{task_select_query} WHERE s.name <> 'completed'"): # or s.id IN(1,2)
        print(Task(row).result())

    print("\n7. Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.\n")
    cur.execute(f"DELETE FROM tasks WHERE id = 2")
    print("\ntask 2 - deleted.\n")
    for row in cur.execute(f"{task_select_query} WHERE s.name <> 'completed'"):
        print(Task(row).result())

    print("\n8. Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.\n")
    for row in cur.execute(f"SELECT id, fullname, email FROM users WHERE email LIKE 'test%'"):
        print(User(row).result())

    print("\n9. Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.\n")
    row = cur.execute("SELECT id, fullname, email FROM users WHERE id = 2").fetchone()
    print(User(row).result())
    cur.execute("UPDATE users SET fullname = 'John Doe' WHERE id = 2")
    row = cur.execute("SELECT id, fullname, email FROM users WHERE id = 2").fetchone()
    print(User(row).result())

    print("\n10. Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.\n")
    for row in cur.execute("SELECT COUNT(t.id) as count, s.name FROM tasks t LEFT JOIN status s ON(t.status_id = s.id) GROUP BY s.id"):
        print(f"status: {row[1]} / count: {row[0]}")

    print("\n11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').\n")
    for row in cur.execute(f"{task_select_query} WHERE email LIKE '%gmail.com'"):
        print(Task(row).result())

    print("\n12. Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.\n")
    for row in cur.execute(f"{task_select_query} WHERE description IS NULL"):
        print(Task(row).result())

    print("\n13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.\n")
    for row in cur.execute(f"{task_select_query} WHERE s.name = 'in_progress'"):
        print(Task(row).result())

    print("\n14. Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.\n")
    for row in cur.execute("SELECT COUNT(t.id) as count, fullname FROM tasks t LEFT JOIN users u ON(t.user_id = u.id) GROUP BY u.id"):
        print(f"user: {row[1]} / count: {row[0]}")


    cur.close()
    

if __name__ == '__main__':
    main()