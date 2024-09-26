import requests

def get_weather(city):
    API_key = '00d7150f9c506be1923599995c55ba00'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&lang=en"
    data = requests.get(url).json()

    if "main" in data:
        temp = round(data["main"]["temp"] - 273.15)  # Convert Kelvin to Celsius
        description = data["weather"][0]["description"]
        weather_data = {
            "city": city,
            "temp": temp,
            "description": description,
            "feels_like": round(data["main"]["feels_like"] - 273.15),
            "temp_min": round(data["main"]["temp_min"] - 273.15),
            "temp_max": round(data["main"]["temp_max"] - 273.15),
        }

        # Determine the image to display based on weather conditions
        if temp < 20:
            image_url = "https://media.giphy.com/media/wcmTjQoJVqMCOZpVLs/giphy.gif?cid=790b7611wid27iu16m7sa7xu6j9rethkklwpijl72t3a7hwe&ep=v1_gifs_search&rid=giphy.gif&ct=g"
        elif "rain" in description.lower():
            image_url = "https://media.giphy.com/media/tFGQ6gxWYADQXETBkK/giphy.gif?cid=790b7611z5f51er6d4arhxvwt3yd77awq75vlyte0vhrhq6v&ep=v1_gifs_search&rid=giphy.gif&ct=g"
        elif 20 <= temp < 30:
            image_url = "https://s3.ezgif.com/tmp/ezgif-3-a9a4c5f3de.gif"
        elif temp >= 30:
            image_url = "https://media.giphy.com/media/JjEnVX00VxuygLiafe/giphy.gif?cid=790b7611y2879htjxx4eb1vm5yx1xuycxqd9hh26u3pheaue&ep=v1_gifs_search&rid=giphy.gif&ct=g"
        # elif "rain" in description.lower():
        #     image_url = "https://media.giphy.com/media/tFGQ6gxWYADQXETBkK/giphy.gif?cid=790b7611z5f51er6d4arhxvwt3yd77awq75vlyte0vhrhq6v&ep=v1_gifs_search&rid=giphy.gif&ct=g"
        else:
            image_url = "https://media.giphy.com/media/8J5U69qF6D82dg8lHv/giphy.gif?cid=790b7611y2879htjxx4eb1vm5yx1xuycxqd9hh26u3pheaue&ep=v1_gifs_search&rid=giphy.gif&ct=g"
        
        return weather_data, image_url
    
    return None, None

