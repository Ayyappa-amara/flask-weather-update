from flask import Flask, render_template, request
from weather import get_current_weather
import requests
# from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    return render_template("index.html")

@app.route("/weather")
def weather():
    # return request.args.get("city")
    city = request.args.get('city')
    
    # check for empty strings and string with empty spaces
    if not bool(city.strip()):
        city = "vizianagaram"
    
    wheather_data = get_current_weather(city)
    # return wheather_data
    if not wheather_data['cod'] == 200:
        return render_template("city-not-found.html", message = wheather_data['message'].capitalize())
    
    return render_template(
        "wheather.html",
        title = wheather_data['name'],
        status = wheather_data["weather"][0]["description"].title(),
        temp = f"{wheather_data['main']['temp']:.1f}",
        feels_like = f"{wheather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.debug = True
    app.run()
    # serve(app, host="0.0.0.0", port=8000)