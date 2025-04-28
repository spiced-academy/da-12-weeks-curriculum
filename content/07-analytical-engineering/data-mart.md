---
title: "Data Mart"
weight: 80
---

![](/images/mart.jpg)

{{< credits >}}
Photo by <a href="https://unsplash.com/@fwwzali?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Fawwaz Ali</a> on <a href="https://unsplash.com/photos/h2qKi_FYfzo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

### Data Marts


A data mart is a subset of a data warehouse focused on a particular line of business, department, or subject area:
- they make specific data available to a defined group of users, which allows those users to quickly access critical insights without wasting time searching through an entire data warehouse
- for example, many companies may have a data mart that aligns with a specific department in the business, such as finance, sales, or marketing
- also allows more fine grained access control: users see only relevant information and no data that they shouldn't be able to see
- many times a data mart will directly refer to company's KPIs
- a Data Mart is the last step in the data modeling 
- as Data Marts are the information that will be shared with the stakeholders, many times we will make this part of our databases / data warehouses accessible to other people in the company (through dashboards, GUIs, etc.)

![data_mart](/images/data_marts.png)

{{% notice challenge "Setup your Data Marts" %}}

1. In your `mart` directory create a file `mart_conditions_week.sql` that will create your first Data Mart.
   
   **Goal:** A table showing weekly averages and total counts, including location and geo information.
   
   **CTE steps:**
   - join `prep_forecast_day` and `staging_location` (use Jinja Syntax like in prep models)
   - select relevant fields for grouping and aggregation (no group bu yet)
   - add buckets for **sunny_days**, **rainy_days**, **snowy_days** and **other_days** and aggregate metrics per week per location using `GROUP BY` 

      Hints:  
       - first find all unique values of condition_text in order to define buckets
       - use `CASE WHEN ... THEN ... ELSE ... END` statements. 
       - depending on which dimension columns you want to keep, it will require 6-9 fields for the `GROUP BY`

{{% expand "Spoler Alert: Solution" %}} 
```sql
WITH joining_day_location AS (
        SELECT * FROM {{ref('prep_forecast_day')}}
        LEFT JOIN {{ref('staging_location')}}
        USING(city,region,country)
),
filtering_features AS (
        SELECT 
            year_and_week
            ,week_of_year
            ,year
            ,city
            ,region
            ,country
            ,lat
            ,lon
            ,timezone_id
            ,max_temp_c
            ,min_temp_c
            ,avg_temp_c
            ,total_precip_mm
            ,total_snow_cm
            ,avg_humidity
            ,daily_will_it_rain
            ,daily_chance_of_rain
            ,daily_will_it_snow
            ,daily_chance_of_snow
            ,condition_text
            -- ,condition_icon
            -- ,condition_code
            -- ,max_wind_kph
            -- ,avg_vis_km
            -- ,uv
            -- ,sunrise
            -- ,sunset
            -- ,moonrise
            -- ,moonset
            -- ,moon_phase
            -- ,moon_illumination
            -- ,day_of_month
            -- ,month_of_year
            -- ,day_of_week
        FROM joining_day_location
),          
aggregations_adding_features AS (
        SELECT 
            year_and_week  -- grouping on
            ,week_of_year   -- grouping on
            ,year           -- grouping on
            ,city           -- grouping on
            ,region         -- grouping on
            ,country        -- grouping on
            ,lat            -- grouping on
            ,lon            -- grouping on
            ,timezone_id    -- grouping on
            ,MAX(max_temp_c) AS max_temp_c
            ,MIN(min_temp_c) AS min_temp_c
            ,AVG(avg_temp_c) AS avg_temp_c
            ,SUM(total_precip_mm) AS total_precip_mm
            ,SUM(total_snow_cm) AS total_snow_cm
            ,AVG(avg_humidity) AS avg_humidity
            ,SUM(daily_will_it_rain) AS will_it_rain_days
            ,AVG(daily_chance_of_rain) AS daily_chance_of_rain_avg
            ,SUM(daily_will_it_snow) AS will_it_snow_days
            ,AVG(daily_chance_of_snow) AS daily_chance_of_snow_avg
            ,SUM(CASE WHEN condition_text = 'Sunny' THEN 1 ELSE 0 END) AS sunny_days
            ,SUM(CASE WHEN condition_text in 
                            ('Overcast', 'Partly cloudy', 'Cloudy', 'Freezing fog') 
                            THEN 1 ELSE 0 END) AS other_days
            ,SUM(CASE WHEN condition_text in 
                            ('Patchy rain possible','Moderate or heavy rain shower', 'Light rain shower',
                            'Mist', 'Moderate rain at times', 'Patchy light rain with thunder',
                            'Patchy light drizzle', 'Thundery outbreaks possible', 'Heavy rain at times', 
                            'Fog', 'Moderate or heavy rain with thunder',  'Light drizzle', 'Light rain', 
                            'Patchy light rain', 'Heavy rain', 'Moderate rain', 'Torrential rain shower', 
                            'Light snow showers', 'Moderate or heavy snow showers', 'Light freezing rain',
                            'Moderate or heavy freezing rain', 'Heavy freezing drizzle') 
                            THEN 1 ELSE 0 END) AS rainy_days
            ,SUM(CASE WHEN condition_text in 
                            ('Patchy light snow', 'Heavy snow', 'Light sleet', 'Light snow', 
                            'Moderate snow', 'Light sleet showers', 'Patchy heavy snow',
                            'Patchy moderate snow', 'Moderate or heavy snow with thunder',
                            'Moderate or heavy sleet', 'Blizzard', 'Blowing snow', 'Patchy snow possible', 
                            'Moderate or heavy showers of ice pellets', 'Patchy light snow with thunder',
                            'Patchy sleet possible', 'Ice pellets') 
                            THEN 1 ELSE 0 END) AS snowy_days
    FROM filtering_features
    GROUP BY (year_and_week, week_of_year, year, city, region, country, lat, lon, timezone_id)
    ORDER BY city
)
SELECT * 
FROM aggregations_adding_features
```
{{% / expand %}}

2. In your `mart` directory create a file `mart_forecast_day.sql`
   
   **Goal:** A table showing daily metrics, including location and geo information. For urls in `condition_icon` column we need a markdown version as a new column.  Example:
    ```markdown
    ![weather_icon](//cdn.weatherapi.com/weather/64x64/day/353.png?width=35)
    ```
    The type of the columns sun/moon/set/rise should be TIME.  
      - values like "No moonrise" can be updated as NULL using  `CASE WHEN ... THEN ... ELSE ... END` statements

   **CTE steps:**
   - join `prep_forecast_day` and `staging_location` (use Jinja Syntax like in prep models)
   - add `condition_icon_md` column with markdown for showing icons (use CONCAT function)
   - order relevant fields 


{{% expand "Spoler Alert: Solution" %}} 
```sql
WITH joining_day_location AS (
        SELECT * FROM {{ref('prep_forecast_day')}}
        LEFT JOIN {{ref('staging_location')}}
        USING(city,region,country)
),
adding_features AS (
        SELECT 
            *
            ,CONCAT('&nbsp;&nbsp;&nbsp;&nbsp;![weather_icon](',condition_icon,'?width=35)') AS condition_icon_md
            ,(CASE WHEN moonrise = 'No moonrise' THEN null ELSE moonrise END)::TIME AS moonrise_n
            ,(CASE WHEN moonset = 'No moonset' THEN null ELSE moonset END)::TIME AS moonset_n
            ,(CASE WHEN sunrise = 'No sunrise' THEN null ELSE sunrise END)::TIME AS sunrise_n
            ,(CASE WHEN sunset = 'No sunset' THEN null ELSE sunset END)::TIME AS sunset_n
        FROM joining_day_location
),
filtering_ordering_features AS (
        SELECT 
            date
            ,day_of_month
            ,month_of_year
            ,year
            ,day_of_week
            ,week_of_year
            ,year_and_week
            ,city
            ,region
            ,country
            ,lat
            ,lon
            ,timezone_id
            ,max_temp_c
            ,min_temp_c
            ,avg_temp_c
            ,total_precip_mm
            ,total_snow_cm
            ,avg_humidity
            ,daily_will_it_rain
            ,daily_chance_of_rain
            ,daily_will_it_snow
            ,daily_chance_of_snow
            ,condition_text
            ,condition_icon
            ,condition_icon_md
            ,condition_code
            ,max_wind_kph
            ,avg_vis_km
            ,uv
            ,sunrise_n
            ,sunset_n
            ,moonrise_n
            ,moonset_n
            ,moon_phase
            ,moon_illumination
        FROM adding_features
)
SELECT * 
FROM filtering_ordering_features
```
{{% / expand %}}

3. In your `mart` directory create a file `mart_forecast_hour.sql`
   
   **Goal:** A table showing hourly metrics, including location and geo information. For urls in `condition_icon` column we need a markdown version as a new column.  
   
   **CTE steps:**
   - join `prep_forecast_day` and `staging_location` (use Jinja Syntax like in prep models)
   - add `condition_icon_md` column with markdown for showing icons (use CONCAT function)
   - order relevant fields 


{{% expand "Spoler Alert: Solution" %}} 
```sql
WITH joining_hour_location AS (
        SELECT * FROM {{ref('prep_forecast_hour')}}
        LEFT JOIN {{ref('staging_location')}}
        USING(city,region,country)
),
adding_features AS (
        SELECT 
            *,
            CONCAT('&nbsp;&nbsp;&nbsp;&nbsp;![weather_icon](',condition_icon,'?width=35)') AS condition_icon_md
        FROM joining_hour_location
),
filtering_ordering_features AS (
        SELECT 
            date
            ,city
            ,region
            ,country
            ,time_epoch
            ,date_time
            ,is_day
            ,time
            ,hour
            ,month_of_year
            ,day_of_week
            ,condition_text
            ,condition_icon
            ,condition_icon_md
            ,condition_code
            ,temp_c
            ,wind_kph
            ,wind_degree
            ,wind_dir
            ,pressure_mb
            ,precip_mm
            ,snow_cm
            ,humidity
            ,cloud
            ,feelslike_c
            ,windchill_c
            ,heatindex_c
            ,dewpoint_c
            ,will_it_rain
            ,chance_of_rain
            ,will_it_snow
            ,chance_of_snow
            ,vis_km
            ,gust_kph
            ,uv
            FROM adding_features
)
SELECT * 
FROM filtering_ordering_features
```
{{% / expand %}}

4. Go to `dbt cloud` and run `dbt run`. When this is done connect to your database and check if you can find newly created tables there.

5. What other aggregations, features or KPIs would you like to add to your database? Think about more and maybe create other sql files with your models.
   - monthly?
   - other location information?
   - ...

{{% /notice %}}


{{% notice reading "Reading" %}}

- Learn more about `dbt` [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](http://community.getbdt.com/) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on `dbt`'s development and best practic

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Samuel McGuire, Alex Schirokow" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). It is a derivative of 

{{% /notice %}}