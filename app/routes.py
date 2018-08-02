#need to import app variable
from app import app
#if you want to render html
from flask import render_template
from app.tables import show_table
from app.graphs import plotPoints

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/graphs')
def graphs():
    x=[1,2,3,4]
    y=[2.2,3.4,2.6,4.8]
    xlabel='x label'
    ylabel='y label'
    title='flask graph'
    my_graph=plotPoints(x,y,xlabel,ylabel,title)
    return render_template('graphs.html',file=my_graph)

@app.route('/tables')
def tables():
    table = show_table()
    return render_template('tables.html',table=table)

# @app.route('/parse')
# def parse():
#     url='http://'
#     data=getData(url)
#     return render_template('parse.html',data=data)
