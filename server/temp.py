import requests
import base64
import captchaSolver

def gif89a_url_to_base64(url):
    try:
        # Fetch the image from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Encode the binary data in base64
        base64_encoded = base64.b64encode(response.content)

        # Decode the bytes to string
        base64_string = base64_encoded.decode('utf-8')
        base64_image = f"data:image/gif;base64,{base64_string}"
        captchaSolver.displayBase64(base64_image)
        return base64_image
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage with a web URL
gif_url = "https://scholarshipportal.mp.nic.in/CaptchaH.ashx?query=0.1445203649070529"
base64_data = gif89a_url_to_base64(gif_url)

if base64_data:
    print("Base64 encoded GIF data:")
    print(base64_data)
