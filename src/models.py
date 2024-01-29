import os
import sys
# Exportamos table para poder crear una tabla auxiliar
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# es una función que se crea para hacer una base(plantilla) que se mete
# en el espacio de memoria Base para poder reutilizarla en los modelos.
# Usamos Base en todos los modelos y así no tenemos que poner db en cada columna.
Base = declarative_base()

# Sería la tabla padre
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    # Las foreing key se ponen en las bases secundarias 


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))

# Creamos esta base para coger el id del follower y meterlo en la tabla auxiliar
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)

# Relacion de muchos a muchos / many to many
# Tenemos que definir un modelo 
    # importar Table en: from sqlalchemy import Column, ForeignKey, Integer, String, Table
# En este caso, crearemos una tabla followers para relacionar followers y user (Ya que un user puede seguir a muchos followers,
# y followers puede ser seguido por muchos y a la vez seguir a muchos)
# También son foreign key porque ya existen esos id en sus respectivas tablas/modelos
# En la documentacion de sql aparece esta plantilla que tenemos que usar en las relaciones del many to many
    # Lo de Base.metadata no sale en la documentacion, lo ponemos para no tener que poner db, como hemos puesto 
        # Base = declarative_base() y la documentación lo hace poniendo db en cada columna
# necesitan ambos se las primary key de la tabla para que el usuario que siga al otro usuario no pueda hacerlo dos veces
followers = Table('followers', Base.metadata,
    Column('user_been_followed_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_following_id', Integer, ForeignKey('follower.id'), primary_key=True)                
)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
