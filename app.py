
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from tensorflow import keras


with open('tokenizer_v4.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('CatMap_v4.pickle', 'rb') as f:
    category_to_name = pickle.load(f)
model = keras.models.load_model('my_model_v4.h5')


def predict(name):
    obj = tokenizer.texts_to_sequences([name])
    obj = pad_sequences(obj, maxlen=100)
    x = model.predict(obj)
    ans = np.argsort(x*-1)
    return ans[0]


# create the Flask app
app = Flask(__name__)
cors = CORS(app)


@app.route('/Predict', methods=['GET', 'POST'])
def API():

    name = request.args.get('name')
    if(name):
        pred = predict(name)
        a = category_to_name[pred[0]]
        b = category_to_name[pred[1]]
        c = category_to_name[pred[2]]
        print(a, b, c)
        new_dict = {
            'pred1': a,
            'pred2': b,
            'pred3': c
        }
        resp = jsonify(new_dict)
        resp.status_code = 200
        print(resp)
        return resp
    # return '''<h1>The language value is: {}</h1>'''.format(name)
    return jsonify(
        {'pred1': "No Data",
         'pred2': "No Data",
         'pred3': "No Data"}
    )


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
