from flask import Flask,jsonify

import requests

from datetime import datetime as dt

def get_weather(zip_code):#(city_name)(latitude,longitude)

    BASE_URL="https://api.openweathermap.org/data/2.5/forecast"

    API_KEY="d923628bd8aa2689b9ed4cf245eb9a59"

    params={
             # 'q':city_name,

             # 'lat':latitude,

             # 'long':longitude,

             'zip':zip_code,

             'appid':API_KEY,

             'units':'metric',

             #'lang':'hi'
    }

    response=requests.get(BASE_URL,params=params)

    if response.status_code==200:

        return response.json()

    else:
        return None

def main():
    
    #city_name=input("Enter name of city for which you want to fetch weather data : ")

    #latitude=input("Enter latitude of place for which you want to fetch weather data : ")

    #longitude=input("Enter longitude of place for which you want to fetch weather data : ")

    zip_code=input("Enter zip_code and country_code seperated by comma of city for which you want to fetch weather data : ")

    forecast_data=get_weather(zip_code)#city_name

    if forecast_data:

        for data in forecast_data["list"]:

            print("Time:", data['dt_txt'])
            print("Temperature:", data['main']['temp'], "°C")
            print("Weather:", data['weather'][0]['description'])
            print("temp_min",data['main']['temp_min'] , "°C")
            print("temp_max",data['main']['temp_max'] , "°C")

    else:
        print("Failed to fetch weather data. Please check your city name or API key.")

main()



"""
The params parameter in the requests.get() function is used to pass query parameters to the API endpoint. 
In the context of an HTTP GET request, query parameters are appended to the URL in the form of key-value pairs, typically separated by '&'. 
These parameters are used to specify additional information required by the API to process the request accurately.

Let's break down the syntax:

response: 
This is the variable name used to store the response object returned by the requests.get() function. 
It contains information about the HTTP response received from the server.

requests.get: This is a function provided by the requests library in Python for making HTTP GET requests to a specified URL.

(base_url, params=params): These are the arguments passed to the requests.get() function.

base_url: This is the base URL of the API endpoint to which the GET request will be made. It typically represents the root URL of the API.

params=params: This is the params argument, where params is a dictionary containing query parameters to be included in the request. 
The params dictionary contains key-value pairs where the keys represent the parameter names, and the values represent the parameter values.

So, in this line of code, the requests.get() function is used to make an HTTP GET request to the specified base_url, 
and the params dictionary is passed along with the request to include any necessary query parameters. 

These parameters might include things like API keys, search queries, filters, or any other information required by the API to fulfill the request accurately. Passing parameters in this way allows for dynamic customization of the request based on the specific needs of the API endpoint."""