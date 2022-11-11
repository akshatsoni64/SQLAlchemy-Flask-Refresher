from db import session, initialize_database
from models import Student, Subject

import time

if __name__ == "__main__":
    initialize_database()
    student_ob = Student(
        id=int(time.time()),
        name="Akshat"
    )

    session.add(student_ob)
    print(*list(map(lambda x: x.__dict__, session.query(Student).all())), sep="\n")
    session.commit()