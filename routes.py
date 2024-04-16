from flask import Blueprint, request
from myfilter.myfilter import Myfilter

bp = Blueprint("home", __name__)

myfilter = Myfilter()

@bp.route("/", methods = ['GET'])
def home():
    message = myfilter.home()
    return message

@bp.route("/gentleman", methods = ['GET'])
def gentleman():
    content = request.get_json()
    if "message" in content:
        message = myfilter.gentleman(content["message"])
        return message
    raise Exception("add message to request")

@bp.route("/sage", methods = ['GET'])
def sage():
    content = request.get_json()
    if "message" in content:
        message = myfilter.sage(content["message"])
        return message
    raise Exception("add message to request")
