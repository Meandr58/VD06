from flask import Flask

#создаем экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-name'

from app import routes