from flask import Flask

app = Flask(__name__)
#__name__ is a python variable which gives each file a unique name

print(input("enter something: "))
@app.route('/')
def home():
    return "Hello, world!"
 
app.run(port=5000)
