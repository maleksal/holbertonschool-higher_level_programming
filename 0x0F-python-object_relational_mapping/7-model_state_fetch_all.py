#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import text, create_engine
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, passwd, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    for state in session.query(State).order_by(State.id).all():
        print("{}:{}".format(state.id, state.name))
    session.close()
