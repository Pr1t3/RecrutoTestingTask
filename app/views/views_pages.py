from flask import Blueprint, render_template, request

views_pages = Blueprint('views_pages', __name__)

@views_pages.route('/', methods=['GET', 'POST'])
def create_post():

    name = request.args.get('name')
    message = request.args.get('message')
    if name is None:
        name = 'Default user'
    if message is None:
        message = 'Default message'
    return render_template('index.html', name=name, message=message)
