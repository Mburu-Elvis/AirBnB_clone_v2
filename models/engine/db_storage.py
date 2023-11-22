from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
"""Module defining the DBStorage engine"""


class DBStorage:
    """Database storage engine definition"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage constructor."""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        db_type = os.getenv("HBNB_TYPE_STORAGE")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """queries the current db session."""
        session = self.__session
        if cls is None:
            objects = session.query(cls).all()
        else:
            objects = []
            for table in Base.metadata.table.keys():
                objects.extend(session.query(Base.metadata.tables[table]).all())
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        """adds the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current db session."""
        self.__session.commit()

    def delete(self, ob=None):
        """deletes object from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
