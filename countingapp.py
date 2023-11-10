from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/count/<int:n>")
def count(n):
    HTMLstring = "<ol>"
    for i in range(n):
        HTMLstring += "<li>" + str(i+1) + "</li>"
    HTMLstring += "</ol>"
    return HTMLstring

@app.route("/count-text/<int:n>")
def countText(n):
    l = []
    for i in range(n):
        l.append(str(i+1)+'\n')
    return Response(l, mimetype="text/plain")

@app.route("/count-pretty/<int:n>")
def countPretty(n):
    nums = []
    for i in range(n):
        nums.append(int(i+1))
    return render_template('count-pretty.html', nums=nums)
