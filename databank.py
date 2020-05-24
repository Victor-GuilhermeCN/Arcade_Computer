import sqlite3
from Functions import line, title, menu_game
from main import chosen_option

connection = sqlite3.connect('users.db')
cursor = connection.cursor()


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL, name TEXT, email TEXT, '
                   'password TEXT)')


def register():
    id_user = int(input('Insert your ID: '))
    name = str(input('Insert your name: '))
    email = str(input('Insert your e-mail: '))
    password = str(input('Insert your password: '))

    cursor.execute('INSERT INTO users (id, name, email, password) VALUES (?,?,?,?)', (id_user, name, email, password))
    line()
    print('Registration completed successfully!')

    connection.commit()
    return show_menu()


def consult_all_recors():
    sql = 'SELECT * FROM users ORDER BY ID'
    cursor.execute(sql)

    for line in cursor.fetchall():
        print(line)

def uptade_record():
    id_user = 2
    new_name = 'Paul Lifter'
    new_email = 'paullifter@hotmail.com'
    new_password = '123432'

    cursor.execute("""
    UPDATE users
    SET name = ?, email = ?, password = ?
    WHERE id = ?""", (new_name, new_email, new_password, id_user))

    connection.commit()

    print('Data update successfully!')

    connection.close()

def delete_record():
    id_user = int(input("What's your id: "))
    cursor.execute("""
    DELETE FROM users
    WHERE id = ? 
    """, (id_user,))
    connection.commit()
    print('Registration deleted successfully.')

def consult():
    id_user = int(input('Insert your id: '))
    r = cursor.execute("""SELECT name FROM users where id = ?""", (id_user,))

    for cliente in r.fetchall():
        print(cliente)


def login():
    id_user = int(input('Insert your ID: '))
    password_user = str(input('Insert your PASSWORD:'))
    idt = cursor.execute("""
    SELECT * FROM users WHERE (id = ? and Password = ?)""", (id_user, password_user))
    verifylogin = idt.fetchone()
    taking_name = cursor.execute("""SELECT name FROM users WHERE id = ?""", (id_user,))
    try:
        if (id_user in verifylogin and password_user in verifylogin):
            for cliente in taking_name.fetchone():
                print(f'Access allowed!\nWelcome {cliente}')
                return title('ARCADE'), menu_game(), chosen_option()
    except:
        print('Access Denied! Try again!')
        return line(), login()

def show_menu():
    title('ACCESS PAINEL')
    print('[1] - Login\n'
          '[2] - Sign UP\n'
          '[3] - Exit')
    line()
    check_registration()

def check_registration():
    try:
        user = int(input('Wich option you chosed: '))
        if type(user) != int and user > 3:
            print('Enter only the chosen number!')
            return line(), check_registration()
    except:
        line()
        print('Enter only the chosen number!')
        return line(), check_registration()
    else:
        if user == 1:
            return login()
        elif user == 2:
            return register()
        elif user == 3:
            while True:
                print('See you soon!')
                line()
                break
        else:
            print("Wrong option! Try again.")
            return line(), check_registration()

show_menu()