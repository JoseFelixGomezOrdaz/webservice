import web

db_host = 'localhost'
db_name = 'ferreteria_jfgo'
db_user = 'ferreteria'
db_pw = 'ferre.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )