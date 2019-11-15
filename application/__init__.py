from flask import Flask

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] =  1024 * 1024

from application import views
