from flask import Flask, render_template, request
import requests

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

        # A module to make HTTP requests

    requests.post(
            "https://api.mailgun.net/v3/sandbox65f5fe854450466e9aa93f4422842a2c.mailgun.org",
            auth=("api", "13f8d365721a270e4795a3f0446dd867-acb0b40c-e16d050a"),
            data={"from": "Excited User <mailgun@sandbox65f5fe854450466e9aa93f4422842a2c.mailgun.org>",
                  "to": form_data["email"],
                  "subject": "Hello",
                  "text": form_data["food"]})
    return render_template ("thankyouinvite.html", food=food, name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)
