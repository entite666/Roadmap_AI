from flask import Flask, render_template, request

from groq import Groq

app = Flask(__name__)

client =  Groq(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form["goal"]
    
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Create a step by step roadmap for: {goal}. Give 7 clear actionable steps."
            }
        ]
    )
  
    roadmap = response.choices[0].message.content
    
    
    
    return render_template("roadmap.html", goal=goal, roadmap=roadmap)

    
    
@app.route("/about")
def about():
      return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
    
@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    return render_template("about.html")
    
    
    
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
