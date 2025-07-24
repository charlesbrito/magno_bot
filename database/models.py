from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from database.conexao import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    banca = Column(Float, nullable=False, default=0.0)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)

    apostas = relationship("Aposta", back_populates="usuario")

class Aposta(Base):
    __tablename__ = "apostas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    evento = Column(String, nullable=False)
    data_evento = Column(DateTime, nullable=False)
    tipo_aposta = Column(String, nullable=False)
    valor_apostado = Column(Float, nullable=False)
    odd = Column(Float, nullable=False)
    possivel_retorno = Column(Float, nullable=False)
    resultado = Column(String, default="pendente", nullable=False)
    data_aposta = Column(DateTime, default=datetime.utcnow, nullable=False)

    usuario = relationship("Usuario", back_populates="apostas")