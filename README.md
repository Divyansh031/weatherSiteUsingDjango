# weatherSiteUsingDjango

# 🌦 Weather Detection API (Django Backend)

This is a simple **Weather Detection using API** built using Django. It allows users to search for a city and retrieve its weather details, including:
- City Code
- Geographical Coordinates (Latitude & Longitude)
- Temperature
- Atmospheric Pressure
- Humidity

The project fetches real-time weather data using the **OpenWeather API** and provides responses in a structured format.

---

## 🚀 Features

- 🔍 **Search by City Name** – Enter a city name to get weather details.
- 🌍 **Real-Time Weather Data** – Uses OpenWeather API to fetch live updates.
- 📡 **REST API** – Can be integrated into web or mobile applications.
- ⚡ **Fast & Lightweight** – Optimized for quick responses.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **API Provider:** OpenWeather API
- **Database:** SQLite (Can be switched to PostgreSQL)
- **Tools:** Requests Library, JSON Processing

---

## 🔧 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Divyansh031/weatherSiteUsingDjango.git
cd weatherSiteUsingDjango
2️⃣ Create a Virtual Environment (Recommended)


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Set Up API Key


Sign up on OpenWeather API to get an API key.
Add the API key to your Django views.py file:

5️⃣ Run the Django Server

python manage.py runserver
Now, visit http://127.0.0.1:8000/ to test the API.

📡 API Endpoint Example
Request

GET /weather?city=London
Response

{
  "city": "London",
  "city_code": "2643743",
  "coordinates": { "latitude": 51.5085, "longitude": -0.1257 },
  "temperature": "15°C",
  "pressure": "1012 hPa",
  "humidity": "72%"
}
