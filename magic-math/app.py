
from flask import Flask
from flask.json import jsonify
import sys
from classes.efficientMagicMath import EfficientMagicMath

# set a limit of amount of recursion to prevent stackoverflow 
sys.setrecursionlimit(15000)
server = Flask(__name__)

def initEfficientMagicMathClass():
    return EfficientMagicMath()

@server.route("/specialmath/<int:magicNumber>", methods=["GET"])
def mathSolution(magicNumber):
    if magicNumber is None or type(magicNumber) is not int: 
        return jsonify({"message": "unknown value please add a positive value"})
    
    func = initEfficientMagicMathClass()
    
    return jsonify({"answer": func.magicNumber(magicNumber, {})})

if __name__ == '__main__':
    server.run()
    server.run()