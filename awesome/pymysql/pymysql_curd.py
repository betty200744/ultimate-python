from datetime import datetime
import pymysql


# connect
def get_connect():
    conn1 = pymysql.connect(host='localhost', user='root', password='!azxsw2', database='employees', charset='utf8')
    return conn1


# insert
def create_employee(conn, first_name, last_name, gender, birth_data, hire_date):
    # emp_no | birth_date | first_name | last_name   | gender | hire_date
    sql = "INSERT INTO `employees`(first_name, last_name, gender, birth_date, hire_date) VALUE (%s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, (first_name, last_name, gender, birth_data, hire_date))
    conn.commit()


# update
def update_first_name_employee(conn, first_name, emp_no):
    sql = "update employees set first_name =%s WHERE `emp_no`=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (first_name, emp_no))
    conn.commit()


# detail
def detail_employee(conn, emp_no):
    sql = "SELECT * FROM `employees` WHERE `emp_no`=%s"
    with conn.cursor() as cursor:
        cursor.execute(sql, (emp_no,))
        result = cursor.fetchone()
        print("detail:", result)


# query
def list_employees(conn):
    cursor = conn.cursor()
    cursor.execute("select * from employees order by emp_no desc limit 2")
    for row in cursor.fetchall():
        print("list:", row)


if __name__ == '__main__':
    conn1 = get_connect()
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    # create
    create_employee(conn1, 'betty', 'zhao', 'm', formatted_date, formatted_date)
    # update
    update_first_name_employee(conn1, 'cc', 1100225)
    # detail
    detail_employee(conn1, 1100225)
    # list
    list_employees(conn1)
