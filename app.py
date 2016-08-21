from flask import Flask, render_template, request, redirect

from quandl_py_direct import get_stock_price, insert_plot_into_html

import os

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    stock_symbol = request.form['myvar'].upper()
    get_stock_price(stock_symbol)
    
    orig_template="index.html"
    output_html="plot.html"
    insert_plot_into_html(os.path.join("templates","index.html"), os.path.join("templates","lines.html"), os.path.join("templates","plot.html")) #must be called after get_stock_price()

    return render_template('plot.html')

if __name__ == '__main__':
  #app.debug = True #uncomment when done debugging
  app.config.update(TEMPLATES_AUTO_RELOAD=True)
  app.run(port=33507)
