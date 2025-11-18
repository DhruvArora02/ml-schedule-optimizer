from flask import Flask, request, jsonify
from model import model
from optimizer import optimize_schedule

app = Flask(__name__)

@app.route("/optimize", methods=["POST"])
def optimize():
    tasks = request.json["tasks"]

    # compute stress for each task
    for t in tasks:
        t["stress"] = model.predict(t)

    order = optimize_schedule(tasks)

    sorted_tasks = [tasks[i] for i in order]
    return jsonify(sorted_tasks)

if __name__ == "__main__":
    app.run(debug=True)
