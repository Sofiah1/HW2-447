from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
appData = SQLAlchemy()

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():
    title = "title"
    return render_template("index.html")
"""
class UsersInputted(appData.Model):
    Name = app.Column(appData.String())        
    ID = app.Column(appData.String())
    Points = app.Column(appData.Integer)
    def __init__(self,Name,ID,Points):
        self.Name = Name
        self.ID = ID
        self.Points = Points
"""

if __name__ == "__main__":
    app.run(debug=True)

