from inspection import Inspection
from inspector import Inspector
from flask import Flask, jsonify, request


x = Inspector.get_inspections()

app = Flask (__name__)
app.config ["DEBUG"] = True

@app.route ('/')
def home():
    return ''' <h1> API testing phase </h1>
                <p> This api is to search restaurant's info based on some parameters </p>'''


@app.route ('/search', methods = ["GET"])
def search ():
    query_params = request.args
    stack = []

    for i in range (len (x)):
        flag = False
        for key in query_params.keys():
            if query_params[key] == x[i].to_json()[key]:
                flag = True
            else:
                flag = False
                break
        if flag:
            stack.append(x[i].to_json())

    if len (stack) == 0:
        return jsonify("No results found")

    return jsonify(stack)

app.run()
