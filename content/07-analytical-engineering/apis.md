---
title: "APIs"
weight: 20
---

![temp gauge](/images/api_json.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/ko/@flowforfrank?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ferenc Almasi</a> on <a href="https://unsplash.com/photos/HfFoo4d061A?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


{{% notice warmup " Introduction to JSON" %}}

```python

import json

# Creating student records
student1 = {
    "name": "Alice",
    "age": 15,
    "grade": 10,
    "subjects": ["Math", "Science", "History"]
}

student2 = {
    "name": "Bob",
    "age": 16,
    "grade": 11,
    "subjects": ["English", "Physics", "Geography"]
}

student3 = {
    "name": "Carol",
    "age": 14,
    "grade": 9,
    "subjects": ["Art", "Music", "PE"]
}

# Creating a list of student records
student_database = [student1, student2, student3]

# Converting the student database to JSON format
json_data = json.dumps(student_database, indent=4)

# Printing the JSON data
print(json_data)
```

- What is JSON, and why is it used in programming?
- In the code, what data structure is used to represent an individual student's information?
- How are key-value pairs used in dictionaries, both in Python and in JSON?


{{% /notice %}}






## What is an API?

An API, short for Application Programming Interface, is a concept used to describe – essentially – a piece of intermediary software (the interface) that facilitates communication between 2 other pieces of software (the applications).
This very broad term is frequently used for web-based systems, database systems, operating systems, or even computer hardware.
In this chapter we will focus on web-based APIs.

## What is a Web API?
A Web API typically means some kind of special website or URL that we use as a channel to get data from some company or web based program. We can write a Python program to retrieve data from the API.
Put very bluntly, an API is a website providing data that is easy for a machine (e.g. python code) to understand (as opposed to a prettier, HTML-rendered, user interface for humans).


## API Acess Tokens - how do they work?

[![API Acess Tokens](https://img.youtube.com/vi/DanUVSlOSQQ/0.jpg)](https://www.youtube.com/watch?v=DanUVSlOSQQ)





## Examples of Web APIs

oncept  |  description
---|---|
   Google Maps  |  get map coordinates for an address
    Spotify    |   read and modify a playlist
    GitHub |   read statistics on your code repo
    WeatherAPI | get weather data for specific location
    Google Translate | translate texts directly from a Python script


## Python Requests Library

The Python [requests](https://requests.readthedocs.io/en/latest/) library is a popular third-party library that simplifies the process of making HTTP requests and working with HTTP responses. It provides a high-level interface for sending HTTP requests to web servers and receiving their responses. This library is widely used for tasks like fetching data from APIs, sending data to servers, and interacting with web resources.

The Python [requests](https://requests.readthedocs.io/en/latest/) library is a widely-used third-party module that simplifies the process of making HTTP requests and handling HTTP responses. It offers a high-level interface for sending requests to web servers and receiving their responses. Developers commonly use this library for tasks such as fetching data from APIs, sending data to servers, and interacting with web resources

1. Installation:  
   You can install the requests library using pip, a package installer for Python:
    ```python
    pip install requests
    ```

2. Importing:  
   After installation, you need to import the library in your Python code before you can use it:
    ```python
    import requests
    ```

3. HTTP Methods:  
   The library supports various HTTP methods, such as GET, POST, PUT, DELETE, etc. You can choose the appropriate method for your request.
   To make a GET request:
    ```python
    response = requests.request("GET", url)
    ```

4. Request Headers:  
   You can add custom headers to your requests, which can be useful for authentication or sending additional information:
    ```python
    headers = {'User-Agent': 'MyApp/1.0'}
    response = requests.request("GET", url, headers=headers)
    ```

5. Response Object:  
When you send a request using the requests library, you receive a response object that contains information about the server's response:


- `response.status_code`: HTTP status code of the response (`200` is a code meaning a successful operation)
- `response.content`: Raw content of the response
- `response.text`: Content of the response in text format
- `response.json()`: Parses the response content as JSON if applicable
- `response.headers`: Headers received from the server
- `response.url`: The URL that was accessed

6. Using the Contents of Response:  
   The response objects allow you to access the contents of the response. E.g. you can save the data as a json file 
    ```python
    with open('json_example.json', mode='w') as f:
        f.write(response.text)
    ```

## Project Challenges


{{% notice challenge "Getting data from the WeatherAPI - one day, one location" %}}


1. Make sure the `.env` file that you [**created in the previous encounter**](http://spiced-12-weeks-da.s3-website.eu-central-1.amazonaws.com/07-analytical-engineering/intro_analytical_eng.html#:~:text=Design%20your%20work) contains the API Key that you registered at [weatherapi.com](https://www.weatherapi.com/pricing.aspx)

2. Follow the steps and write a python script to get weather for **one day**: 
    - imports...
    - load your `.env` file and read the api key for weather api
    - make a single request to weather api to get data for one day and one location:
        - use the endpoint with following syntax<br><font size="4em">`http://api.weatherapi.com/v1/history.json?key=<yourapikey>&q=Berlin&dt=2023-05-24`</font>
        - you can modify the url parameters:   
          `key` is for your API Key  
          `q` is for the location  
          `dt` is for the date in yyyy-MM-dd format  
    - extract the result using the `.text` attribute
    - save the result as a `.json` file

3. Open the json file in an edtior. Copy/Paste the resulting json into https://jsonformatter.org/. Looking at the weather characteristics think about what weather data can be ananlyzed and what questions you would like to answer for your 'stakeholders'.

**BONUS:** Your code in the Jupyter Notebook is in the *development stage*. Once the script is functioning correctly, in real-live scenario, the code will be saved in a `.py` file for the *production stage*. This way, the entire script can be executed at once from a terminal.  

   - create a python file `extract_one_day.py`  
   - copy and save all the necessary code  
   - running the python file should create a json file from one api call  

{{% /notice %}}
{{% notice challenge "Getting data from the WeatherAPI - multiple api calls" %}}

In the initial EXTRACT step of our pipeline, we will retrieve raw data from the source as-is. For each location and date, we will make an API call and also collect the timestamp for each execution for the record. Tomorrow, we will LOAD the data to a database table. Each row in the table will capture both the raw API call and the timestamp when it was made.

<img src="/images/load_raw.png" style="zoom:60%;" />

Today we will collect the data in a dictionary of calls and corresponding timestamps. Back to the development stage.  

1. Create a list of 3-5 locations for which you would like to explore weather data. Calling more locations would take longer and it is not necessary for the development stage. (The API understands city names, but we could also use coordinates, zip codes, etc.)
   
2. How would you do the api calls for multiple days? ... and for multiple locatons? ... How would you collect it?
   One option is to create an emtpy dictionary. 

   And we will need two for-loops: one iterating over locations and a nested one iterating over dates within a given time period.  
   **NOTE:** Start with a small time period (like 7 days) to test your code! Else it will take forever.
   ```python
    weather_dict = {'extracted_at':[], 'extracted_data':[]}

    for city in locations:
        for day in pd.date_range(start='09/10/2023', end='09/13/2023'):
            requested_day = day.date()
            # print(city, requested_day) # check the values passed to the variables
    ```
3. As in one-api-call solution we can use the f-string ability and make the parameters in our endpoint url optional:
   <font size="4em">`f'http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={requested_day}'`</font>

4. for each nested iteration add the code for the api call 

5. for each nested iteration after making the api call append the timestamp (->[**example**](https://www.w3schools.com/python/python_datetime.asp)) and the response in json format to the `weather_dict`
   ```python
   weather_dict['extracted_at'].append(datetime.datetime.now())
   weather_dict['extracted_data'].append(json.loads(response.text))

6. *(optional)* for each nested iteration check the status_code
    ```python
    if response.status_code == 200:
        print(f'attempt for {day.date()} in {city} resulted in {response.status_code}', end='\r')
    else:
        print(f'for date: {day.date()} and city: {city} status code {response.status_code} -> research error')
    ```

7. save the `weather_dict` as a json file

Note: The API presented above will give you the access to one year of historical weather data (within your 2 weeks trial account). After this time, you will be able to get data for the previous day only.

**BONUS:**  
Copy your code from the Jupyter Notebook (*development*) to a `.py` file (*production*)  

   - create a python file `extract_multiple.py`  
   - copy and save all the necessary code  
   - running the python file should create a json file with all api calls  



{{% /notice %}}


{{% notice copyright "Samuel McGuire, Sara Maras" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}