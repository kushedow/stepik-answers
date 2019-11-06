from flask import *
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

sheetdb_id = "ropn4xlz2e32m"

@app.route('/')

def main():

  output = render_template("main.html")  # рендерим шаблон
  return output  # возвращаем то, что отрендерилось

@app.route('/solution/')

def solution():

  lessonid = request.values.get("lessonid")
  stepid = request.values.get("stepid")

  if len(stepid)<1:
    return render_template("404.html")  # рендерим шаблон

  query = "https://sheetdb.io/api/v1/"+sheetdb_id+"/search?lessonid="+lessonid+"&stepid="+stepid

  session = requests.Session()
  session.trust_env = False
  r = session.get(query)

  data = r.json()

  if len(data)>0:

    solution = data[0]

    output = render_template("solution.html",solution=solution)  # рендерим шаблон
    return output  # возвращаем то, что отрендерилось

  else:

    return render_template("404.html")  # рендерим шаблон

if __name__ == '__main__':
    app.run()