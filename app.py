from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    
    return render_template('homepage.html')

@app.route("/history")
def history():

    text_example = [

        "The Pentagon denied providing 'specific targeting information' to Ukraine to sink the Moskva, a Russian guided-missile cruiser that was the flagship of Moscow's fleet in the Black Sea.",
        "In Mora County, population 4,500, around 60 percent of residents in evacuation areas have remained in centuries-old farming and ranching communities where electric power has been lost, said Undersheriff Americk Padilla.",
        "Former employees, backed by the Whistleblower Aid charity, say the company intentionally 'over-blocked' Australian pages at a critical time to gain leverage over the Australian government."
    ]
    return render_template('history.html', texts = text_example)

