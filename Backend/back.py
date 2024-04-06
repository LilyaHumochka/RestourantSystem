from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
#from flask_sqlalchemy import select
#from flask_sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://(localdb)\MSSQLLocalDB/New Database'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False

#db.session.query(text('1')).from_statement(text("Select * from Tasks")).all()

# str_sql = db.sql.text("Select * from Tasks")
# #if you have some args:
# #then call the execute method from your connection
# results = db.execute(str_sql).fetchall()

#print(results)
#stmt = select(user_table).where(user_table.c.name == "spongebob")
#print(stmt)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"