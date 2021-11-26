import matplotlib.pyplot as plt
import pandas as pd
from flask import *
import numpy as np
from __init__ import *
import os
app = Flask(__name__)
funcList = [fill_empty_with_nan,drop_missing_data,replace_missing_data,remove_outliers,normalize,preprocess_data,delete_constant_columns,combine_first_last_name,drop_useless_columns, check_if_dateTime,one_hot_encode,]
UPLOAD_FOLDER = './static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
@app.route('/', methods=['GET','POST'])
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
        # checkbox.append(request.form.get("checkbox1"))
        # checkbox.append(request.form.get("checkbox2"))
        # checkbox.append(request.form.get("checkbox3"))
        # checkbox.append(request.form.get("checkbox4"))
        # checkbox.append(request.form.get("checkbox5"))
        # checkbox.append(request.form.get("checkbox6"))
        print(checkbox)
        # if you want to convert to json:
        # import json
        # with open('/home/ubuntu/test.json', 'w') as fout:
        # json.dump(list , fout)
        uploaded_file = request.files['dataset']
        if uploaded_file.filename != '':
            # file_path = os.path.join(app.config['UPLOAD_FOLDER'], "data.csv")
            # set the file path
            df = pd.read_csv(uploaded_file)
            for func in funcList:
                if checkbox[funcList.index(func)]['checked']==True:
                    df = func(df)
            df.to_csv('data.csv',index=False)
            filePath = 'data.csv'
            fileName = uploaded_file.filename
            text = request.form.get("comment")
            print(text)
            return send_file("../data.csv")
    return render_template("index.html", checkboxes = funcList)
    
# @app.route('/plot')
# def plot_png(df):
#    fig = Figure()
#    axis = fig.add_subplot(1, 1, 1)
#    xs = np.random.rand(100)
#    ys = np.random.rand(100)
#    axis.plot(xs, ys)
#    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
#    fig = CorrelationMatrixPlot(df)
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True)

