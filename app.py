from flask import Flask, render_template
from Topic_Selector import Topic, Company
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/topic")
def topic():
    index = random.randint(0, len(Topic)) % (len(Topic))
    topic = Topic[index]
    company = Company[random.randint(0, len(Company))%len(Company)]

    return render_template("topic.html", topic=topic, company=company)


if __name__ == "__main__":
    app.run(debug=True)
