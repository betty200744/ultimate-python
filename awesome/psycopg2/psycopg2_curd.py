import psycopg2


# get connection
def get_connect():
    c = psycopg2.connect("dbname=employees user=betty")
    return c


# create_employee
def create_employee(conn, first_name, last_name, gender):
    cursor = conn.cursor()
    sql = "INSERT INTO employees(first_name, last_name, gender) VALUES (%s, %s, %s)"
    cursor.execute(sql, (first_name, last_name, gender))
    conn.commit()


# update_first_name_employee
def update_first_name_employee(conn, first_name, emp_no):
    sql = "update employees set first_name =%s WHERE emp_no=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (first_name, emp_no))
    conn.commit()


# detail_employee
def detail_employee(conn, emp_no):
    sql = "SELECT * FROM employees WHERE emp_no =%s"
    with conn.cursor() as cursor:
        cursor.execute(sql, (emp_no,))
        result = cursor.fetchone()
        print("detail:", result)


# list_employees
def list_employees(conn):
    cursor = conn.cursor()
    cursor.execute("select * from employees order by emp_no desc limit 2")
    for row in cursor.fetchall():
        print("list:", row)


if __name__ == '__main__':
    print('main')
    conn1 = get_connect()
    # create
    create_employee(conn1, 'betty', 'zhao', 1)
    # update
    update_first_name_employee(conn1, 'cc', 1100225)
    # detail
    detail_employee(conn1, 1)
    # list
    list_employees(conn1)
