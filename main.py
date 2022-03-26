from flask import Flask, render_template, request
import funcs as F
import settings as S


app = Flask( # Create a flask app
	__name__,
	template_folder='templates',
	static_folder='static' )






@app.route(S.sessionURLin,methods = ["GET","POST"])
def setM():
  param = {"message":request.form.get("message"),"index":request.form.get("key")}
  if param["message"] != None and param["index"] != None:
    F.setMessage(param["index"],param["message"])
    return str(F.getAllKeysPrefix(param["index"]))
  else:
    return str(param["message"])
  return "0"




@app.route(S.sessionURLout,methods = ["GET","POST"])
def getM():
  param = {"index":request.form.get("key")}
  if param["index"] != None:
    return F.getMessage(param["index"])
  else:
    return str(param["index"])
  return "0"


@app.route(S.sessionURLkeyin,methods = ["GET","POST"])
def setUser():
  param = {"index":request.form.get("index"),"key":request.form.get("key")}
  if param["index"] != None:
    F.saveKey(param["key"],param["index"])
    return "1"
  else:
    return str(param["index"])
  return "0"

@app.route(S.sessionURLkeyout,methods = ["GET","POST"])
def getUser():
  param = {"index":request.form.get("index")}
  if param["index"] != None:
    return F.getKey(param["index"])
  else:
    return str(param["index"])
  return "0"



if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)