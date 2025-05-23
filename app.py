from flask import Flask, render_template
import random
from collections import Counter

app = Flask(__name__)

def generate_lotto6():
    return sorted(random.sample(range(1, 44), 6))

def generate_lotto7():
    return sorted(random.sample(range(1, 38), 7))

past_lotto6 = [
    [3, 12, 19, 22, 33, 41],
    [1, 7, 14, 22, 33, 35],
    [2, 12, 19, 23, 28, 41],
]

past_lotto7 = [
    [2, 5, 11, 17, 21, 28, 33],
    [3, 6, 13, 18, 22, 27, 34],
    [1, 8, 11, 19, 25, 30, 35],
]

def get_hot_cold(draws, total_numbers, top_n=5):
    flat = [num for draw in draws for num in draw]
    counter = Counter(flat)
    hot = counter.most_common(top_n)
    cold = counter.most_common()[:-top_n-1:-1]
    return hot, cold

@app.route("/")
def index():
    lotto6 = generate_lotto6()
    lotto7 = generate_lotto7()

    hot6, cold6 = get_hot_cold(past_lotto6, 43)
    hot7, cold7 = get_hot_cold(past_lotto7, 37)

    return render_template("index.html", 
        lotto6=lotto6, lotto7=lotto7, 
        hot6=hot6, cold6=cold6,
        hot7=hot7, cold7=cold7)

if __name__ == "__main__":
    app.run(debug=True)
