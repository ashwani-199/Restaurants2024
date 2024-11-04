from flask import Flask, request, json, Response, Blueprint, g, render_template

Usertemp = Blueprint('user templates', __name__)


@Usertemp.route('/', methods=['GET'])
def index():
    return render_template('index.html')