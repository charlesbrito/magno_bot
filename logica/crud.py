from database.conexao import SessionLocal
from database.models import Usuario, Aposta

# Cadastrar Cliente
def criar_cliente(nome, email, banca, telegram_id):
    session = SessionLocal()
    if session.query(Usuario).filter_by(telegram_id=telegram_id).first():
        raise Exception("Usuário já cadastrado.")
    novo = Usuario(nome=nome, email=email, banca=banca, telegram_id=telegram_id)
    session.add(novo)
    session.commit()
    session.refresh(novo)
    session.close()
    return novo

# Mensagem de bom dia:
def bom_dia(telegram_id):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(telegram_id=telegram_id).first()
    if not usuario:
        session.close()
        raise Exception("Usuário não encontrado.")
    
    nome_user = usuario.nome
    session.commit()
    session.close()
    return nome_user

# Cadastrar Aposta
def criar_aposta(evento, data_evento, tipo_aposta, valor_apostado, odd, possivel_retorno, resultado, telegram_id):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(telegram_id=telegram_id).first()
    if not usuario:
        session.close()
        raise Exception("Usuário não encontrado.")
    
   
    nova_aposta = Aposta(evento=evento,data_evento=data_evento,tipo_aposta=tipo_aposta,valor_apostado=valor_apostado,odd=odd,possivel_retorno=possivel_retorno,resultado=resultado, usuario_id=usuario.id)
    session.add(nova_aposta)
    session.commit()
    session.refresh(nova_aposta)
    session.close()
    return nova_aposta

# Listar apostas
def listar_apostas(telegram_id):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(telegram_id=telegram_id).first()
    if not usuario:
        session.close()
        raise Exception("Usuário não encontrado.")
    
    apostas = list(usuario.apostas)
    session.close()
    return apostas

def listar_por_time(telegram_id, time):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(telegram_id=telegram_id).first()
    if not usuario:
        session.close()
        raise Exception("Usuário não encontrado.")
    
    aposta_time = session.query(Aposta).filter(Aposta.usuario_id == usuario.id, Aposta.evento.ilike(f"%{time}%")).all()
    session.close()
    return aposta_time

def listar_por_resultado(telegram_id, resultado_busca):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(telegram_id=telegram_id).first()
    if not usuario:
        session.close()
        raise Exception("Usuário não encontrado.")
    
    aposta = session.query(Aposta).filter(Aposta.usuario_id == usuario.id, Aposta.resultado.ilike(f"%{resultado_busca}%")).all()
    session.close()
    return aposta