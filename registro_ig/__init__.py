from flask import Flask #importar flask

app = Flask(__name__) # definir la app que en init definimos en main 

from registro_ig.routes import *