---
title: "Visualization Best Practices"
weight: 80
---
 
![bad plot](/images/bad_plot.jpg)

---

![good plot](/images/good_plot.jpg)
{{< credits >}}
Photos taken from https://www.storytellingwithdata.com/blog/2016/1/26/connecting-the-dots
{{< /credits >}}

{{% notice warmup "Good and bad plots" %}}

Look at the two plots above

- What distinguish the lower from the upper plot?
- Describe the story of each plot!
- Which plot do you like most?


Read the full story [here](https://www.storytellingwithdata.com/blog/2016/1/26/connecting-the-dots).


{{% /notice %}}


## Visualisation Best Practices

When telling a story with data, visuals are a vital component to the bigger picture. They contribute to the ability to effectively communicate insights from a dataset. This is turn can inspire action and spawn amazing results depending on the application. 

Data Visualization refers to the techniques used to encode numbers to visual objects to communicate data.

While it’s easy to get carried away with the sheer amount of plotting options in python, it’s important to ground yourself first in the fundamentals of data visualization good practices.

You now know how (i.e. syntactically) to make lots of different kinds plots in python, but certain types of plots and visualization techniques work better in certain scenarios, depending on the story / narrative you’re trying to convey. Keep in mind that plotting is part of a greater workflow of reading, cleaning, understanding, and presenting data.

### Exploratory visualization

- Think about the type of data you are exploring in order to choose the most appropriate graph / chart for your data.
- Visualize the quality of your data, e.g. missing values.
- Understand the variables you are working with, e.g. distribution shape, correlation, other descriptive statistics.

### Explanatory visualization

- Design for your audience: “form follows function”. First think about what the audience wants to be able to do with the data (function) and then create a visualization (form) that will facilitate this easily. Choose the appropriate visual / chart based on the message you are trying to convey.
- Get rid of chart junk, i.e. elements that do not contribute to clarifying the message.
- Use color with intention.


## Project Challenges

{{% notice challenge "Challenge: Make an animated plot" %}}

First, improve your plot with the new features you learned during the encounter:

1. Rotate the x-ticks by 45 degrees
2. Color each point according to continent
3. Annotate 2 to 4 countries
4. Add grid-lines
5. Adjust the opacity of the points
6. Try out different plotting themes

To create an animated scatterplot showing the correlation between life expectancy and fertility, create one plot for each year between 1960 and 2015 (before that, the data contains too many gaps).

### Step 1

Write a for loop that goes through each year

### Step 2

In each iteration produce a scatterplot like the one you have made in the previous challenges

### Step 3

Save each scatterplot to a separate file containing the year in the filename, e.g. `plot_1999.png`.

### Step 4

After saving the plot call `plt.close()` to remove the plot before plotting the next year.


### Step 5

To generate a gif file from the individual pictures, adjust the following code example and execute it:

```python
import imageio

images = []

for year in range(___, ___):
    filename = f'___'
    images.append(imageio.imread(___))

imageio.mimsave(___, images, fps=20)
```


### Tips

- make the size of the plot larger
- set axis ranges for the complete story
- use `hue` to color the points according to a column
- use `size` to emphasize the difference in point dependent on a column value
- try other things to tell your story to the fullest
- use the function `plt.axis(xmin, xmax, ymin, ymax)` to fix the coordinates of the plot.


{{% /notice %}}




## Reading

{{% notice reading "Links" %}}

- [Storytelling with Data](https://www.storytellingwithdata.com) by Cole Nussbaumer Knaflic

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}

