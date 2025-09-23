from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


@app.route('/whereami')
def whereami():
    return 'Ghana'

Items= {1:"banana",3:"oranges",4:"Bread",2:"yam",3:"eggs"}
@app.route('/items')
def getAllItem():
    return Items
@app.route('/last')
def getLastItem():
    last_Item = list(Items.items())[-1]
    return last_Item
@app.route('/First')
def getFirst():
    # first_Item = list(Items.items())[0]
    return Items[1]
# @app.route('/addBegin')
# def AddBegin():
#     new_Key="Rice"
#     new_value=6
#     Adding = {new_Key:new_value **Items}
#     return Adding

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')