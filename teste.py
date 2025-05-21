from models.database import Database

with Database() as db:
    sql = "select * from serie limit 1"
    resultado = db.executar(sql)
    print(resultado)