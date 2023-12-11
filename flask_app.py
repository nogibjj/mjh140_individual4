from flask import Flask, render_template, request
from transformers import pipeline, set_seed

app = Flask(__name__)

# Set up the text generation pipeline with GPT-2 model
text_generator = pipeline("text-generation")
set_seed(42)  # Optional: Set a seed for reproducibility


@app.route("/")
def index():
    return render_template("city.html")


@app.route("/generate", methods=["POST"])
def generate():
    if request.method == "POST":
        city = request.form["prompt"]

        prompt = f"What is it like living in {city}?"

        # Generate text using GPT-2 based on the constructed prompt
        generated_texts = text_generator(
            prompt,
            num_return_sequences=1,
            temperature=0.7,
            top_k=70,
            top_p=0.95,
        )

        # Extract the generated texts excluding the original prompt
        response = generated_texts[0]["generated_text"].replace(prompt, "")

        return render_template(
            "response.html", city_response=response
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)