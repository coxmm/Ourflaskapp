from flask import Flask, render_template, request

app = Flask(__name__)

# Display the form
@app.route("/")
def hello_world():
    return render_template ("a.html")

# Handle form submission
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    # Print out all the form data
    print(form_data)
    food = form_data["food"]
    name = form_data["name"]
    email = form_data["email"]
    # TODO: send email with mailgun
    return render_template ("thankyouinvite.html", food=food, name=name, email=email)

app.run(debug=True)
