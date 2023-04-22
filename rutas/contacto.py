from flask import Blueprint

contactos=Blueprint("contacto",__name__)

@contactos.route('/')
def index():
    return 'consultando'

@contactos.route('/new')
def new():
    return 'guardando contacto'