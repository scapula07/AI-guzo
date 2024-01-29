#   Imports
from flask import Flask, request, jsonify
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from Guzo_NLP import final_nlp_model
# from flask import Flask, request, jsonify
import final_nlp_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")


#   initialize app with service account key
# cred = credentials.Certificate('path/to/serviceAccountKey.json') # Bart
# firebase_admin.initialize_app(cred, {'databaseURL': 'https://my-project.firebaseio.com'}) # Bart
# ref = db.reference()
print("Starting")
#   Listen for a Create JSON object from frontend of application 
@app.route('/', methods=['POST']) # Bart
def intake_process_text():
    #   retrieve text input from frontend and feeds it to NLP model
    input_text = request.json['text'] #this is the parameter that refers to 'text' property in the JSON data 
    print(input_text,"text")
    keywords = final_nlp_model.keywords(input_text)
    print(keywords,"text")

    #   takes extracted keywords and feeds it to Firebase database along with query
    # new_entry = {
    #     'original_text': input_text,
    #     'keywords': keywords
    # }

    # ref.push(new_entry)

    return jsonify({
        'status': "Saved query and keywords",
        'keywords':keywords
    })


keywords = [] # empty keywords list for next input

if __name__ == '__main__':
    app.run(port=8080)
