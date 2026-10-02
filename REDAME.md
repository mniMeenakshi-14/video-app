# 🐼 VideoMood

A free web app that turns a photo into a short AI video. Upload an image, describe the movement, and download the result.

## How it works
- Flask backend
- Calls the Wan 2.2 image-to-video model on Hugging Face (ZeroGPU Space) using `gradio_client`
- Simple web page with image upload, a motion prompt, and a download button

## Run locally
1. Install the packages:
   pip install -r requirements.txt
2. Set your Hugging Face token (PowerShell):
   $env:HF_TOKEN="your_token_here"
3. Start the app:
   python app.py
4. Open http://127.0.0.1:5000

## Notes
- Free Hugging Face accounts have a small daily GPU quota, so only a few videos can be made per day.
- Clips are about 3 seconds long.
- Never commit your token. It is read from the `HF_TOKEN` environment variable.