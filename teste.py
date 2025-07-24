from sqlalchemy import inspect, create_engine

engine = create_engine('sqlite:///magno_bot.db')
inspetor = inspect(engine)

tabelas = inspetor.get_table_names()
print("Tabelas no banco:", tabelas)