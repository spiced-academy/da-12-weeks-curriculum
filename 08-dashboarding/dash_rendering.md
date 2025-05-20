---
title: "Rendering"
weight: 70
---

![rendering](/images/render.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/de/@cdd20?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">愚木混株 cdd20</a> on <a href="https://unsplash.com/de/fotos/MDBojqzl7Mg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}


## Rendering
Now we are ready with our web app. However, it runs on our local server. What if we would like to share our app with other people? For this reason we are going to deploy our  dash app.

For making our app online, we are going to use Render. "Render is a unified cloud to build and run all your apps and websites with free SSL, global CDN, private networks and automatic deploys from Git." 

For deploying your dash app to the web with Render, you need to have:
- `Github` Account
- `Render.com` Account
- your dash app as `.py` file
- `requirements.txt` file


## Deploying our dash app

#### 1. Create a .py file 
We are going to deploy the app we created in the jupyter notebook. Copy all the code from the jupyter notebook into a python file and run the file in the terminal to check in browser which runs on your server. After that we need to  add the command below after defining the `app`. 

`server = app.server`

#### 2. Create a public repository
Render is using github to deploy. Therefore we are going to need to create a public repository on github. On your github account repositories page click on new, give it a name and do not forget to select `public` option. After creating the repository, push your python file into this repository.


#### 3. Create a requirements.txt file
In your terminal check your dash version with `pip show dash` command.(you can also do itfor all the packages you used for your app) Open the `requirements.txt` file you created and add the information inside. It should look similar to this:

```python
dash==2.14.2
gunicorn
plotly==5.9
dash-tools
pandas==2.1.4
sqlalchemy==2.0.25
dash_bootstrap_components
python-dotenv
psycopg2==2.9.9
```

{{% notice warning "Requirements" %}}

If you are using any other libraries like numpy, scipy etc, please add those libraries also inside of your requirements text file. However, do not add the libraries you imported in your python file but maybe did not use(please consider importing pandas, since some versions of the plotly may not be working without importing pandas). Otherwise you will get an error during the deployment

{{% /notice %}}


After preparing the file, drag it into your public repository.


#### 4. Create a Render account
Go to [https://dashboard.render.com/](https://dashboard.render.com/) and create an account with using your email address or github account. You cannot use the same github account for different render accounts. After creating your account, in your home page click on the new and select the webservice from the dropdown menu.

![web_service](/images/webservice.png)


#### 5. Deploy
From the opening window, you need to select `Build and deploy from a Git repository` option and click on the `next`. On the next page, scroll down and find `Public Git Repository` part. 

![git build](/images/gitbuild.png)

Get back to your github page for your public repo, click on the `code` and copy the `https` link. 

![git code](/images/git_code.png)

Go to your render page again and paste that link and click on continue. 

![git paste](/images/git_paste.png)

Now you need to give a name to your web service. We are going to name it `gapminder_app`. The environment should be python 3, you can also select your region. We are going to select Frankfurt. Build command appears automatically. 
![git editor](/images/git_frankfurt.png)

In the start command part please put the name of your python file name **without** `.py` before the `:`
After the `:` please write `server`
![dash app](/images/dash_app.png)


Select the free trial below. 

If you are getting the data from GCP, you are going to need the .env credentials. Scroll down and find the environmental credentials and pass your credentials without " " and save them. DO NOT push the .env file to your repo! If you forgot to save them, you can click on dashboards, find your project and click on the environments button on the left side. (Do not forget that your env credentials cannot be named only as "HOST" and "PORT" since it will give you an error while building your app)

![dash app](/images/environment.png)

And you are ready to go! After that it is going to take a couple of minutes to deploy. If the deployment fails, go to the manuel deployment button after making the necessary changes in your python and txt filesand pushing them to the repo. If you would like to change settings or delete the web service, you need to click on the `dashboard` to list your services. 



{{% notice challenge "Deploy your dash app with Render" %}}

- Create an account in [https://dashboard.render.com/](https://dashboard.render.com/).
- Create a public repository in github. 
- Create a `requirements.txt` file as explained during the session.
- Create an `.py` file out of your dash app.
- Push your work into the github.
- Deploy your web app
- Share the link with your colleagues.

{{% /notice %}}

<br>

{{% notice copyright "copyright Hilal Işık" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}