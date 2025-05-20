---
title: "Awesome Datasets"
weight: 12
---

![awesome](/images/awesome.jpg)

## Datasets

-  [Housing Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
-  [Gapminder Data](www.gapminder.org/data)
-  [World Bank Development Data](https://datacatalog.worldbank.org/)
-  [TED talk dataset](https://www.kaggle.com/rounakbanik/ted-talks)
-  [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/)
-  [MovieLens ratings](https://grouplens.org/datasets/movielens/)
-  [TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
-  [Text Analytics and Visualization](http://www.pybloggers.com/2017/10/text-analytics-and-visualization/)
-  [Move Review Sentiment in IMDBWS](https://datasets.imdbws.com/)
-  [Movie Dialog Dataset](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
-  [German Parliament text data](github.com/malexmave/pdok-mirror)
-  [Football Data](https://www.football-data.org/)
-  [Credit G](https://www.openml.org/d/31)
-  [Steelplate](https://www.openml.org/d/1504)
-  [Electricity Time Series](https://www.openml.org/d/151)
-  [Cylinders](https://www.openml.org/d/6332)
-  [Adult](https://www.openml.org/d/1590)
-  [Polizei­liche Kriminal­statistik](https://www.bka.de/DE/AktuelleInformationen/StatistikenLagebilder/PolizeilicheKriminalstatistik/PKS2017/pks2017_node.html)

APIs
----

-  [Spoonacular Food API](https://spoonacular.com/food-api)
-  [TV Series DB API](https://api.thetvdb.com/swagger)
-  [Programmable Web API catalog](https://www.programmableweb.com)

Quandl Financial API
--------------------

Quandl is a platform that provides various financial and economic data from
over 500 publishers [via their APIs), all accessible from a single module / library. With the [Quandl API in Python](https://www.quandl.com/tools/python>[_ you can access historical data from a number of categories --
equities, currencies, interest rates, real estate, agriculture, energy, metals, etc. -- as
long as you [create a free account](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp>[_ and get your own *API key*.

After you've signed up, you can already start using the library. Some steps to help
you get started:


**1. Install the python library**

```
pip install quandl
```


**2. In the beginning of your jupyter notebook / python script, import the library and establish
your API authentication, using your API key:**

```python
import quandl
quandl.ApiConfig.api_key = "..." #put your key here
```

**3. Take a look at the** [free tier datasets](https://www.quandl.com/search?filters=%5B%22Free%22%5D) **that are available to you.**

  - you can filter by asset class, data type, region, publisher


**4. Once you've found something that interests you, browse through the documentation to understand how the the syntax for the API works, and download some data:**

```python
#example: Frankfurt Stock Exchange / Deutsche Bank
data = quandl.get['FSE/DBK_X')
```

pandas-datareader
-----------------

The [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) library downloads stock data directly into a DataFrame.

If you want to use data from *Yahoo Finance*, you need to install a small update, see:

{{< youtube eSpH6fPd5Yw >}}


   German stocks have a `.DE` after the stock symbol, e.g. `SIE.DE` for Siemens.


Dataset Collections
+++++++++++++++++++

-  [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
-  [datasetlist.com](http://datasetlist.com)
-  [OpenML](https://www.openml.org/)
-  [Data.gov](http://www.data.gov/)
-  [Amazon Public Data Sets](http://aws.amazon.com/public-data-sets/)
-  [100 Interesting Data Sets](http://rs.io/100-interesting-data-sets-for-statistics/)
-  [Dreamtolearn 1001 Datasets](https://dreamtolearn.com/ryan/1001_datasets)
-  [ML Collections](https://github.com/collections/machine-learning)
-  [UFL Datasets](http://www.stat.ufl.edu/~winner/datasets.html)
-  [r/datasets](http://www.reddit.com/r/datasets)
-  [r/data](http://www.reddit.com/r/data)
-  [R reference datasets](https://r-dir.com/reference/datasets.html)
-  [Our World in Data](https://ourworldindata.org/)
-  [IMDBWS Datasets](https://datasets.imdbws.com/)
-  [Text and language datasets](https://lnkd.in/gFR9njn)
-  [NLP datasets](https://lnkd.in/gABJX4w)
-  [Google Dataset Search](https://datasetsearch.research.google.com)

<br>

{{% notice copyright "Samuel McGuire, Kristian Rother" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}