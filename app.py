# -*- coding: utf-8 -*-
import os

from bottle import Bottle, run
from bottle import route, template, request
from bottle import jinja2_template as template

from settings import DEBUG


app = Bottle()


coins = [1, 5, 7, 9, 11]

def CoinDeterminer(num):
    index = 4
    result = 0
    while True:
        if num == 0:
            return result
        if (num - coins[index]) < 0:
            index -= 1
            continue
        num = num - coins[index]
        result += 1


@app.route("/")
@app.route("/", method='POST')
def index():
    file = request.files.get("file")
    
    if file:
        content_type = file.content_type
        prefix = os.path.splitext(file.filename)[1]

        if content_type == "text/plain" and prefix == ".txt":
            try:
                datas = map(int, file.file.read().splitlines())
                
                if all(type(item)==int for item in datas):
                    result = []
                    for num in datas:
                        result.append(CoinDeterminer(num))

                    return template("index", result=result)
            except:
                return template("index", info="invalid input data file!")
        
        return template("index",
                            info="invalid file, the "
                                "file must be a text file!")

    return template("index")


def main():
    run(app=app, host="127.0.0.1", port=8888, 
                    debug=DEBUG, reloader=True)


if __name__ == "__main__":
    main()