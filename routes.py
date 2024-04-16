from flask import Blueprint, request
from myfilter.myfilter import Myfilter

bp = Blueprint("home", __name__)

myfilter = Myfilter()

@bp.route("/")
def home():
    message = myfilter.home()
    return message

@bp.route("/gentleman")
def gentleman():
    content = request.get_json()
    if "message" in content:
        message = myfilter.gentleman(content["message"])
        return message
    raise Exception("add message to request")

@bp.route("/haiku")
def haiku():
    content = request.get_json()
    if "message" in content:
        message = myfilter.haiku(content["message"])
        return message
    raise Exception("add message to request")