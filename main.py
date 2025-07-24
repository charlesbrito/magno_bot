from database.conexao import Base, engine
from database.models import Usuario

Base.metadata.create_all(bind=engine)