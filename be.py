from flask import Flask, render_template

app = Flask(__name__)

# Animal data
animals = [
    {
        "name": "Chinese Water Dragon",
        "habitat": "Southeast Asian rainforests",
        "fun_fact": "Can stay underwater for 25 minutes!"
    },
    {
        "name": "Bearded Dragon",
        "habitat": "Australian deserts and woodlands",
        "fun_fact": "Uses arm waves to say 'Hi!'"
    },
    {
        "name": "White-Bellied Caique",
        "habitat": "Amazon rainforest",
        "fun_fact": "Nicknamed “the clown of parrots” for playful flips"
    }
]

@app.route('/')
def home():
    return render_template('index.html', animals=animals)

if __name__ == '__main__':
    app.run(debug=True)
