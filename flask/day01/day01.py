
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print()
    return 'Hello, World!\n'

if __name__ =="__main__":
    app.run(debug=True,port=8080)