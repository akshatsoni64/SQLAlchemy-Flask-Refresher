import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

con_string = "mysql://root:12345678@localhost:3306/student"
engine = sqlalchemy.create_engine(con_string, pool_size=10)
session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False,
                                                                    bind=engine))
base = sqlalchemy.ext.declarative.declarative_base()
base.query = session.query_property()


def initialize_database():
    base.metadata.create_all(engine)
