import quandl
import pandas as pd
import datetime as dt
from bokeh.plotting import figure, output_file, show, save
import os

def load_file_as_list(CURR_FILENAME):
    """
    returns file contents as a list where each line is a element of the list
    """
    inFile = open(CURR_FILENAME)
    lines = inFile.readlines()
    inFile.close()
    return lines

def write_string_to_file(CURR_FILENAME, string_to_write):
    """
    Writes a string (string_to_write) to CURR_FILENAME
    """
    inFile=open(CURR_FILENAME,'w')
    inFile.write(string_to_write)
    inFile.close()
    return None

def get_stock_price(stock_symbol):
    quandl.ApiConfig.api_key = 'YOUR QUANDL API CONFIG KEY HERE' 
    data = quandl.get("WIKI/" + stock_symbol)

    col_names=list(data)

    date = dt.date.today(
    last_mo_data=data.ix[pd.datetime(date.year,date.month-1,1) : pd.datetime(date.year,date.month-1,data.index.days_in_month[-2])]

    output_file(os.path.join("templates","lines.html"))

    p = figure(title="Interactive stock chart", x_axis_label='Date', x_axis_type="datetime", y_axis_label='Close price, USD')
    p.line(last_mo_data['Close'].index, last_mo_data['Close'], legend=stock_symbol, line_width=2)

    save(p)
    return None

def insert_plot_into_html(orig_template, bare_plot_file, output_html):
    lines=load_file_as_list(orig_template)
    headerlines=lines[0:6]
    lines=lines[6:]
    
    #### after <title>:
    templines=[]
    templines.append('<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.1.min.css" type="text/css" />\n')
    templines.append('\n')        
    templines.append('<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.1.min.js"></script>')
    templines.append('<script type="text/javascript">')
    templines.append('    Bokeh.set_log_level("info");')    
    
    lines=lines[:-2] #remove closing body and html tags

    #### after </form>
    templines2=load_file_as_list(bare_plot_file) 
    templines2=templines2[27:]
    lines = headerlines + templines + lines + templines2

    write_string_to_file(output_html, "".join(lines))
    return None

if __name__ == "__main__":
    stock_symbol = raw_input("enter stock: ")
    get_stock_price(stock_symbol)
    insert_plot_into_html(os.path.join("templates","index.html"), os.path.join("templates","lines.html"), os.path.join("templates","plot.html"))

