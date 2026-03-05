from flask import Flask, render_template, request
import os
from enhancer import enhance_image

app = Flask(__name__)
UPLOAD_FOLDER = "static/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], "input.png")
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], "output.png")
        chart_path = os.path.join(app.config["UPLOAD_FOLDER"], "diff_chart.png")

        file.save(input_path)

        results = enhance_image(input_path, output_path, chart_path)

        return render_template("index.html",
                               enhanced_image="output.png",
                               chart_image="diff_chart.png",
                               original_stats=results["original"],
                               enhanced_stats=results["enhanced"])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
