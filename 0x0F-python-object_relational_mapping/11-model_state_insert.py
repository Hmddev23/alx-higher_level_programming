#!/usr/bin/python3
"""
add the State object `Louisiana` to `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    get access to the database and
    the state from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = State(name="Louisiana")
    session.add(n_state)
    session.commit()

    print('{0}'.format(n_state.id))
    session.close()
