#!/usr/bin/python3
"""
task 1
"""

if __name__ == "__main__":
    import MySQLdb as mysql
    from sys import argv as args

    # assign args to variables
    mysql_username = args[1]
    mysql_password = args[2]
    db_name = args[3]

    # connect to Mysql server
    database = mysql.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=db_name)

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%';\
                    ORDER BY state.id")

    result = cursor.fetchall()
    for i in result:
        if i[1][0] == "N":
            print(i)
