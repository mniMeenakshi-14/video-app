import os, shutil, uuid
from flask import Flask, request, jsonify, render_template
from gradio_client import Client, handle_file

app = Flask(__name__)
os.makedirs("static/out", exist_ok=True)

SPACE = "zerogpu-aoti/wan2-2-fp8da-aoti-faster"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    path = f"tmp_{uuid.uuid4().hex}.png"
    try:
        request.files["image"].save(path)
        prompt = request.form["prompt"]
        client = Client(SPACE, token=os.getenv("HF_TOKEN"))
        result = client.predict(
            input_image=handle_file(path),
            prompt=prompt,
            steps=4,
            duration_seconds=3,
            api_name="/generate_video"
        )
        video = result[0] if isinstance(result, (list, tuple)) else result
        if isinstance(video, dict):
            video = video.get("video") or video.get("value")
        name = f"{uuid.uuid4().hex}.mp4"
        shutil.copy(video, f"static/out/{name}")
        return jsonify(url=f"/static/out/{name}")
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        if os.path.exists(path):
            os.remove(path)

if __name__ == "__main__":
    app.run(debug=True)