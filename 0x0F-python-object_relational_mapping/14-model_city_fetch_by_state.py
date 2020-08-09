#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import text, create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state, city in session.query(State, City).\
            filter(City.state_id == State.id).all():
                print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
