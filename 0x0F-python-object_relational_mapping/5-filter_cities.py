#!/usr/bin/python3
"""
task 4
"""

if __name__ == "__main__":
    import MySQLdb as mysql
    from sys import argv as args

    # assign args to variables
    mysql_username = args[1]
    mysql_password = args[2]
    db_name = args[3]
    state_name = args[4]
    # connect to Mysql server
    database = mysql.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=db_name)

    cursor = database.cursor()
    cursor.execute("""
        SELECT
            cities.name
        FROM
            cities
        WHERE
            cities.state_id = (
                            SELECT
                                states.id
                            FROM
                                states
                            WHERE
                                states.name = %(state_name)s)
        ORDER BY
            'cities.id'
        """, {'state_name': state_name})

    result = cursor.fetchall()
    for x, i in enumerate(result):
        print(i[0], end="")
        if x + 1 < len(result):
            print(",", end=" ")
    print()
