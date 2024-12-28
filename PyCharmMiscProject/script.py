# Author: Sam M.
# Date  : 27 Dec 2024
# Purpose: Testing POC (proof of concept)


# imports

from flask import Flask, render_template, request


# server deployment (will give the link in output to view server/ site created)
app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('character_form.html')

# route to process form data
@app.route('/create_character', methods=['POST'])
def create_character():
    # get form data
    name = request.form.get('name')
    strength = request.form.get('strength')
    intelligence = request.form.get('intelligence')

    # process and return a response
    return render_template('character_sheet.html', name=name, strength=strength, intelligence=intelligence)



if __name__ == '__main__':
    app.run(debug=True)


