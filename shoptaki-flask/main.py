from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pandas as pd
import os
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import *
from utilities.__init__ import *
from utilities.database import *

import os


app = Flask(__name__, static_folder='build')

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#SQLAlchemy integration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
db.create_all()

def parseCSV(filePath, fileName):
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath, header=0)
    csvData.to_sql(fileName, con=db.engine, if_exists='replace')

# # Root URL
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve(path):
#     if path != "" and os.path.exists(app.static_folder + '/' + path):
#         return send_from_directory(app.static_folder, path)
#     else:
#         return send_from_directory(app.static_folder, 'index.html')


# Get the uploaded files


funcList = [autoconverter,fill_empty_with_nan,drop_missing_data,replace_missing_data,remove_outliers, normalize , delete_constant_columns,combine_first_last_name,drop_useless_columns, check_if_dateTime,one_hot_encode,]

@app.route('/preprocess', methods=['GET','POST'])
# def index():
#     return render_template('index.html')
# Get the uploaded files
# @app.route('/post', methods=['POST'])
def recordSubmission():

    if request.method == 'POST':
        checkbox = []
        for i in range(len(funcList)):
            if request.form.get(funcList[i].__name__)=='on':
                checkbox.append({'name':funcList[i].__name__,'checked':True})
            else:
                checkbox.append({'name':funcList[i].__name__,'checked':False})
       
        uploaded_file = request.files['dataset']
        if uploaded_file.filename != '':
            fileName = uploaded_file.filename
            df = autoconverter(uploaded_file,fileName) #Currently supported files are xls, xlsx, csv, json, sql(doesnt work too well), and pickle
            try: 
                if df.empty:
                    return
            except:
                pass
            print(df.head())
            headers = df.columns.values.tolist()
            # target = request.form.get('target')
            
            for func in funcList:
                if checkbox[funcList.index(func)]['checked']==True:
                    df = func(df)
            # doesnt convert back to the file like json bc the realtional nature is usually lost
            # AKA not yet implemented
            df.to_csv('data.csv',index=False)
            fileName = uploaded_file.filename
            text = request.form.get("comment")
            # if target != '':
            #     # do visualizations with target
            #     matches = difflib.get_close_matches(target, headers)
            #     #  do visualizations with closest match
            #     if len(matches)>0:
            #         target = matches[0]
            key = add_documents(text, checkbox,headers)
            print(text)
            return send_file("../data.csv")
    return


@app.route("/uploads", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['data']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        parseCSV(file_path, uploaded_file.filename)
    # save the file
    return 'data'

if (__name__ == "__main__"):
    app.run(use_reloader=True, port=5000, threaded=True)