---
title: "dbt - stages"
weight: 70
---

![](/images/phases.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@tegethoff?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mark Tegethoff</a> on <a href="https://unsplash.com/photos/NbgQfUvKFE0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "KPIs for weather data" %}}

At this stage you should be also familiar with WeatherAPI data. Think about what kind of information could be valuable for an end user. If that helps, imagine that you're asked for preparing a dashboard presenting some insights about this data. 

What kind of data structure would be easy to present this information. What would be an ideal table that you would like to see in your database - what fields should it have? 

{{% /notice %}}

## `dbt` / modeling layers

Good model layers improve the usability and understandability of your `dbt` project and your data warehouse, and can make it easier to build off of and grow over time.

![stages](/images/dbt_stages.png)

To create the tables in all different layers we will use SQL (and CTE) that will be saved in the previously created repository. 

## More about particular layers:
### Base:
- the base layer is not always needed
- a good use case for using base models is when two sources must be joined to create a usable staging model (a situation where you wouldn't never use these components separately)

### Staging:
The staging layer is the first main model directory in a `dbt` project. 
Staging contains base models, and staging models. 
Both of these layers are 1:1 with their source data (raw data) and do very light transformations like: 
- casting
- renaming
- filtering of bad data or deleted records
- no joining should happen in this layer, except for the joining of base models in a staging model when necessary.  
  
Many times staging will be the most used model type in a directory. Every source should end up as a staging model which is either 1:1 with a source OR a combination of base models.

{{% notice info "Sidebar: JSON Operators" %}}
In our case, the result from fetching the weather data using an API is a large JSON from which we will extract three tables for:  
- location information
- daily weather
- hourly weather

To extract, flatten, or normalize JSON data from a column in PostgreSQL, we can employ JSON operators and choose individual fields as columns for our new table. We will only use operators `->` and `->>`. 

{{% expand "Show an Example" %}}

here is a snippet of a JSON from one cell

```json
{
    "location":{
        "name":"Berlin",
        "country":"Germany",
        "lat":52.52,
        "lon":13.4,
        "tz_id":"Europe/Berlin"
    },
    "forecast":{
        "forecastday":[
            {
                "date":"2023-10-01",
                "day":{
                    "avgtemp_c":16.4,
                    "maxwind_kph":13.0,
                    "avghumidity":59
                }
            }
        ]
    }
}
```

To extract the value of the `"location"` key (selecting a JSON object field by key), we can use the following query:

```sql
SELECT extracted_data -> 'location' FROM weather_raw;
```

but because we actually want to get the location name, we need to extract the field `"name"` from the nested structure:

```sql
SELECT extracted_data -> 'location' -> 'name' FROM weather_raw;
```

The `->` operator returns values in JSON format. When casting individual JSON values to `VARCHAR` or `TEXT` the double quotes from the JSON format will persist.

```sql
SELECT (extracted_data -> 'location' -> 'name')::VARCHAR(255) FROM weather_raw;
```

It is impossible to cast JSON values to some types, it's essential to first cast them as `TEXT` or `VARCHAR`. 

```sql
SELECT (extracted_data -> 'location' -> 'localtime')::TEXT::DATE FROM weather_raw;
```

Alternatively, we can use the `->>` operator. The output is already in text format, so it can easily be converted to a different data type.

```sql
SELECT (extracted_data -> 'location' ->> 'name')::VARCHAR(255) FROM weather_raw;

SELECT (extracted_data -> 'location' ->> 'localtime')::DATE FROM weather_raw;
```

Suppose we want to extract the value associated with the `"date"` key. Upon closer examination, we find that it is a key within a dictionary, which happens to be the first element in a list (at index position 0). This list itself is a value nested under the key `"forecast"`. To achieve this, we can select the JSON array element corresponding to the date and retrieve it as text.

```sql
SELECT (extracted_data -> 'forecast' - > 'forecastday' -> 0 ->> 'date')::DATE FROM weather_raw;
```
{{% / expand %}}

**For more information:**
- [PostgreSQL Documentation: JSON Functions and Operators](https://www.postgresql.org/docs/9.5/functions-json.html)
- [Tutorial: PostgreSQL JSON Operators/](https://www.postgresqltutorial.com/postgresql-json-functions/postgresql-jsonb-operators/)
- [Tutorial: PostgreSQL JSON](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-json/)

{{% /notice %}}

### Intermediate:
Intermediate models are where we start to apply business logic and join staging models. Intermediate models are also a great place to create reusable logic that can be applied elsewhere in the [DAG](https://docs.getdbt.com/terms/dag).

The transformations here might include:
- joining tables
- feature engineering 
- extracting or expanding features


### Dimension/Fact:
Dimension and Fact models are core business models, such as dim_users which would contain all core dimensions/details about users for the business:
- dimension models are “things” (nouns) like users, stores, products, and so on
- fact models are “events” (verbs) like orders or transactions. Facts are something that happened

Best pratice: put intermediate and dim/fact models into mart folders

## `yml` files
`yml` (or `yaml`) (Yet Another Markup Language) is a files extension that is often used for configuration files. We will use it in our `dbt` project to define the structure of your project and how your data will be modeled (e.g. if you're gonna create views or tables and in which locations).

## SQL and Jinja 

In `dbt` you can use SQL syntax to model your data. You could also combine SQL with Jinja which is a templating language. Jinja enables you to program with SQL in ways you
wouldn't be able to do with SQL alone like:
- if statements
- for loops
- use of environment variables


{{% notice challenge "Setup your staging models" %}}

1. Before you begin modeling, modify the `dbt_project.yml` file in you local Git repo. Ensure that the last part of the file looks like the one below:

    ```yml
    models:
      my_new_project:
        # Applies to all files under models/staging/
        staging:
            materialized: table
        prep:
            materialized: table
        mart:
            materialized: table
    ```

    This way we make sure that all the data we're modeling (for staging, prep and mart) will be represented as tables (by default they will be views).

2. In your new github repository `dbt-repo` create 3 new directories under `models` directory:
    - staging
    - prep
    - mart

3. In your new `staging` directory create 4 new files:
    - `staging_sources.yml`
    - `staging_location.sql`
    - `staging_forecast_day.sql`
    - `staging_forecast_hour.sql`  
    So it looks similar to this structure:
    ![stg_1](/images/dbt_staging_1.png)

4. Populate the `staging_sources.yml` file with the following code:

    ```yml
    version: 2
    sources:
    - name: staging
      schema: public
      tables:
        - name: weather_raw
    ```

    That will make sure that your source data is properly located. Transformation will be done based on the table "weather_raw" in the schema "public" in your database.

5. Populate the `staging_location.sql` file with the following code:

    ```sql
    WITH locations_data AS (
        SELECT DISTINCT
            (extracted_data -> 'location' ->> 'name')::VARCHAR(255) AS city
            ,(extracted_data -> 'location' ->> 'region')::VARCHAR(255) AS region
            ,(extracted_data -> 'location' ->> 'country')::VARCHAR(255) AS country
            ,(extracted_data -> 'location' ->> 'lat')::NUMERIC AS lat 
            ,(extracted_data -> 'location' ->> 'lon')::NUMERIC AS lon
            ,(extracted_data -> 'location' ->> 'tz_id') AS timezone_id
        FROM {{source("staging", "weather_raw")}})
    SELECT * 
    FROM locations_data
    ```

    Study the code:
    - check how the `JSON` file is being extracted to smaller chunks of information
    - feel free to modify the code to add more features if you find them useful. But maybe later.


6. **Commit the changes** in `staging_location.sql` and `dbt_project.yml` as "staging location" in your local Git repo. **An push it to GitHub.**

7. Go to `dbt cloud`. Open **Cloud IDE** from "Develop" in the navigation bar. `dbt` will identify the changes in GitHub repo and the button will turn yellow with text "Pull from Remote". Click it.
   
   **Hint:** If the button is still green with the text "Create branch" click the dropdown arrow on the button's right and select "Refresh git state"

8. At the bottom, in the command line (it is not prominent, just that white field) and execute `dbt run`. A successful run will give you a positive feedback message. Otherwise fix the bugs.

9. If it was successful, connect to your database using your tool of preference (e.g. `dbeaver`, `psql`, etc.) and check if you can find newly created table/s there. Hint: right-click on the Schema and "Refresh".

10. populate `staging_forecast_day.sql` file with the following code:

{{% expand "Click to expand Code" %}} 

```sql
WITH forecast_day_data AS (
    SELECT 
            (extracted_data -> 'forecast' -> 'forecastday' -> 0 ->> 'date')::DATE AS date
            ,(extracted_data ->'location'->>'name')::VARCHAR(255) AS city
            ,(extracted_data -> 'location' ->> 'region')::VARCHAR(255) AS region
            ,(extracted_data -> 'location' ->> 'country')::VARCHAR(255) AS country
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'maxtemp_c')::NUMERIC AS max_temp_c
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'mintemp_c')::NUMERIC AS min_temp_c
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'avgtemp_c')::NUMERIC AS avg_temp_c
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'maxwind_kph')::NUMERIC AS max_wind_kph
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'totalprecip_mm')::NUMERIC AS total_precip_mm
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'totalsnow_cm')::NUMERIC AS total_snow_cm
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'avgvis_km')::NUMERIC AS avg_vis_km
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'avghumidity')::NUMERIC AS avg_humidity
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'daily_will_it_rain')::INT AS daily_will_it_rain
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'daily_chance_of_rain')::INT AS daily_chance_of_rain
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'daily_will_it_snow')::INT AS daily_will_it_snow
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'daily_chance_of_snow')::INT AS daily_chance_of_snow
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' -> 'condition' ->> 'text')::VARCHAR(255) AS condition_text
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' -> 'condition' ->> 'icon')::VARCHAR(255) AS condition_icon
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' -> 'condition' ->> 'code')::VARCHAR(255) AS condition_code
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'day' ->> 'uv')::NUMERIC AS uv
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'sunrise') AS sunrise
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'sunset') AS sunset
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'moonrise') AS moonrise
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'moonset') AS moonset
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'moon_phase')::VARCHAR(255) AS moon_phase
            ,(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'astro' ->> 'moon_illumination')::NUMERIC AS moon_illumination
    FROM {{source("staging", "weather_raw")}})
SELECT * 
FROM forecast_day_data
``` 
{{% / expand %}}


11.  For the hourly weather data, a two-step Common Table Expression (CTE) process is required. Populate `staging_forecast_hour.sql` file with the code below.
   
{{% expand "Click to show code explanation" %}} 

**First Step:** a temporary table named `forecast_hour_raw` is created to collect general location information along with hourly data stored as JSON. Within our JSON structure, for each date, there is a JSON array containing hourly weather data. To handle this, we use the `JSON_ARRAY_ELEMENTS` function, which expands the array into a set of rows, allowing us to break down the hourly data for further analysis.

**Second Step:** another temporary table named `forecast_hour_data` extracts detailed weather information from the `hour_data` column with hourly JSON data extracted in the first step.

{{% / expand %}}
{{% expand "Click to expand Code" %}} 
    
```sql
WITH forecast_hour_raw AS (
    SELECT 
            (extracted_data -> 'forecast' -> 'forecastday' -> 0 ->> 'date')::DATE AS date
            ,(extracted_data ->'location'->>'name')::VARCHAR(255) AS city
            ,(extracted_data -> 'location' ->> 'region')::VARCHAR(255) AS region
            ,(extracted_data -> 'location' ->> 'country')::VARCHAR(255) AS country
            ,JSON_ARRAY_ELEMENTS(extracted_data -> 'forecast' -> 'forecastday' -> 0 -> 'hour') AS hour_data
    FROM {{source("staging", "weather_raw")}}
),
forecast_hour_data AS (
    SELECT 
            date
            ,city
            ,region
            ,country		
            ,(hour_data ->> 'time_epoch')::INTEGER AS time_epoch
            ,(hour_data ->> 'time')::TIMESTAMP AS date_time
            ,(hour_data ->> 'is_day')::INTEGER AS is_day			
            ,(hour_data -> 'condition' ->> 'text')::VARCHAR(255) AS condition_text
            ,(hour_data -> 'condition' ->> 'icon')::VARCHAR(255) AS condition_icon
            ,(hour_data -> 'condition' ->> 'code')::INTEGER AS condition_code
            ,(hour_data ->> 'temp_c')::NUMERIC AS temp_c
            ,(hour_data ->> 'wind_kph')::NUMERIC AS wind_kph
            ,(hour_data ->> 'wind_degree')::INTEGER AS wind_degree
            ,(hour_data ->> 'wind_dir')::VARCHAR(255) AS wind_dir
            ,(hour_data ->> 'pressure_mb')::NUMERIC AS pressure_mb
            ,(hour_data ->> 'precip_mm')::NUMERIC AS precip_mm
            ,(hour_data ->> 'snow_cm')::NUMERIC AS snow_cm
            ,(hour_data ->> 'humidity')::INTEGER AS humidity
            ,(hour_data ->> 'cloud')::INTEGER AS cloud
            ,(hour_data ->> 'feelslike_c')::NUMERIC AS feelslike_c
            ,(hour_data ->> 'windchill_c')::NUMERIC AS windchill_c
            ,(hour_data ->> 'heatindex_c')::NUMERIC AS heatindex_c
            ,(hour_data ->> 'dewpoint_c')::NUMERIC AS dewpoint_c
            ,(hour_data ->> 'will_it_rain')::INTEGER AS will_it_rain
            ,(hour_data ->> 'chance_of_rain')::NUMERIC AS chance_of_rain
            ,(hour_data ->> 'will_it_snow')::INTEGER AS will_it_snow
            ,(hour_data ->> 'chance_of_snow')::NUMERIC AS chance_of_snow
            ,(hour_data ->> 'vis_km')::NUMERIC AS vis_km
            ,(hour_data ->> 'gust_kph')::NUMERIC AS gust_kph
            ,(hour_data ->> 'uv')::NUMERIC AS uv
    FROM forecast_hour_raw
    )
SELECT * 
FROM forecast_hour_data
```
{{% / expand %}}


{{% notice challenge "Setup your prep models" %}}

1.  In your `prep` directory create a file `prep_forecast_day.sql` that will add some information to your table created in the staging layer.

    Our `prep_forecast_day` table wants to also include several informations derived from the "date" column.  

    Use this skeleton and fill in the two blanks `...` to make it work.  
    Hint: use the [`DATE_PART`](https://www.postgresqltutorial.com/postgresql-date-functions/postgresql-date_part/) and [`TO_CHAR`](https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-to_char/) functions.

    ```sql
    WITH forecast_day_data AS (
        SELECT * 
        FROM {{ref('staging_forecast_day')}}
    ),
    add_features AS (
        SELECT *
            ,...(...) AS day_of_month -- day of month as a number
            ,...(...) AS month_of_year -- month name as a text
            ,...(...) AS year -- year as a number
            ,...(...) AS day_of_week -- weekday name as text
            ,...(...) AS week_of_year -- calender week number as number
            ,...(...) AS year_and_week -- year-calenderweek as text like '2024-43'

        FROM forecast_day_data
    )
    SELECT *
    FROM add_features

2. **Commit the changes** in `prep_forecast_day.sql`. **An push it to GitHub.**

3. Go to `dbt cloud`. Open **Cloud IDE** from "Develop" in the navigation bar. `dbt` will identify the changes in GitHub repo and the button will turn yellow with text "Pull from Remote". Click it.
   
   **Hint:** If the button is still green with the text "Create branch" click the dropdown arrow on the button's right and select "Refresh git state"

4. Execute `dbt run` and check the content of the database. Fix bugs if any.

5. In your `prep` directory create a file `prep_forecast_hour.sql` that will add some information to your table created in the staging layer.

    Our `prep_forecast_hour` table wants to also include the information about weekday and the number of the day. Use this skeleton and fill in the two blanks `...` to make it work:

    ```sql
    WITH forecast_hour_data AS (
        SELECT * 
        FROM {{ref('staging_forecast_hour')}}
    ),
    add_features AS (
        SELECT *
            ,date_time::time AS time -- only time (hours:minutes:seconds) as TIME data type
            ,...(...,'HH24:MI') as hour -- time (hours:minutes) as TEXT data type
            ,...(...) AS month_of_year -- month name as a text
            ,...(...) AS day_of_week -- weekday name as text
        FROM forecast_hour_data
    )
    SELECT *
    FROM add_features

6. **Commit the changes** in `prep_forecast_hour.sql`. **An push it to GitHub.**

7. Go to `dbt cloud`. Open **Cloud IDE** from "Develop" in the navigation bar. `dbt` will identify the changes in GitHub repo and the button will turn yellow with text "Pull from Remote". Click it.
   
   **Hint:** If the button is still green with the text "Create branch" click the dropdown arrow on the button's right and select "Refresh git state"

8. Execute `dbt run` and check the content of the database. Fix bugs if any.


9. As for the weekly project submission, please copy the sql files to the student code repository.

{{% /notice %}}


{{% notice copyright "Agnieszka Kaczmarczyk, Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}