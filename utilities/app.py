# from matplotlib.pyplot import plot
# import pandas as pd
# from flask import *
# import numpy as np
# import io
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import os
# from werkzeug.utils import secure_filename

# from visuals import CorrelationMatrixPlot

# app = Flask(__name__)

# UPLOAD_FOLDER = 'static/files'
# app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
# @app.route('/', methods=['GET','POST'])
# def index():
#     return render_template('index.html')
# # Get the uploaded files
# @app.route("/", methods=['POST'])
# def uploadFiles():
#     # get the uploaded file
#     uploaded_file = request.files['file']
#     if uploaded_file.filename != '':
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], "data.csv")
#         # set the file path
#         uploaded_file.save(file_path)

#         # save the file
#         df = pd.read_csv(file_path)
#     return redirect(plot_png())

#     # df.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
# @app.route('/plot')
# def plot_png(df):
# #    fig = Figure()
# #    axis = fig.add_subplot(1, 1, 1)
# #    xs = np.random.rand(100)
# #    ys = np.random.rand(100)
# #    axis.plot(xs, ys)
#    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
#    fig = CorrelationMatrixPlot(df)
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')
# if __name__ == '__main__':
#     app.run(debug=True)

