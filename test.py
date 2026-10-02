from gradio_client import Client

client = Client(
    "zerogpu-aoti/wan2-2-fp8da-aoti-faster",
    token=""
)
client.view_api()