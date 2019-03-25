from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

# Display the form
@app.route("/")
def hello():
    return render_template("invite.html")

# Handle form submission
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    # Print out all the form data
    print(form_data)

    return render_template("thankyouinvite.html")

app.run(debug=True)
