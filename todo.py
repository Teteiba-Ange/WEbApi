from flask import Flask

app= Flask(__name__)
print("*******The list of items on my grocery list**")

Items= {"banana":4,"oranges":3,"Bread":4,"yam":2,"eggs":3}
@route('/item')
def getAllItem():
    print("THis are the items {Items}")

if __name__=='__main__':
     app.run(debug=True,host='0.0.0.0')