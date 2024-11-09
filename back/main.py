import requests
def download_image(prompt, width=768, height=768, model='flux'):
    url = f"https://image.pollinations.ai/prompt/{prompt}?width={width}&height={height}&model={model}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('tamagotchi.jpg', 'wb') as file:
            file.write(response.content)
        print('Image downloaded as tamagotchi.jpg!')
    else:
        print('Error:', response.status_code)

# Example usage
# download_image("a singular, 16 bit, pixelated, simple, black tamagotchi cat in a very sad expression with a white background")
# download_image("a singular, 16 bit, pixelated, black and white, simple, tamagotchi penguin in an idle expression with eyes open with a white background, no shadows or colours")
download_image("a singular, 16 bit, pixelated, simple, tamagotchi lion in a smily expression with a white background")