from flask import Flask, render_template, request
from transformers import pipeline, set_seed

app = Flask(__name__)

# Set up the text generation pipeline with GPT-2 model
text_generator = pipeline("text-generation")
set_seed(42)  # Optional: Set a seed for reproducibility


@app.route("/")
def index():
    return render_template("traits.html")


@app.route("/generate", methods=["POST"])
def generate():
    if request.method == "POST":
        input_traits = request.form["prompt"]

        # Construct the prompt sentence
        prompt = f"The best professions for someone with the following traits and/or skills {input_traits} are:"

        # Generate text using GPT-2 based on the constructed prompt
        generated_texts = text_generator(
            prompt,
            max_length=50,
            num_return_sequences=3,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )

        # Extract the generated texts excluding the original prompt
        generated_professions = [
            generated_text["generated_text"].replace(prompt, "")
            for generated_text in generated_texts
        ]

        return render_template(
            "professions.html", generated_professions=generated_professions
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)