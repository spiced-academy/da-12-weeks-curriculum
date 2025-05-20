---
title: "Dashboards and Stories"
weight: 40
---

![interactive](/images/manipulation.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@freewalkingtoursalzburg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Free Walking Tour Salzburg</a> on <a href="https://unsplash.com/s/photos/puppet?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Viz of the Day" %}}

Go to [Viz of the Day](https://public.tableau.com/app/discover/viz-of-the-day) and pick one of the highlighted visuals. Why did you choose it? What do you like about it and what would you change? Present your thoughts to the group.

{{% /notice %}}


## Inspiration / goal
We will two dashboards using the previously created visuals:

- **Sales vs Profit Discovery Dashboard**
![dashboard1](/images/discovery_dashboard1.png)

- **Sales vs Profit for Categories Discovery Dashboard**
![dashboard2](/images/discovery_dashboard2.png)

## Annotations
[Annotations](https://help.tableau.com/current/pro/desktop/en-us/annotations_annotations_add.htm) are a great way to mark something permanently on your visuals. 

## Analytics
[Analytics Pane](https://help.tableau.com/current/pro/desktop/en-us/environ_workspace_analytics_pane.htm) enables you to add analytical representation of your data. It could be a trend line, average line, distribution statistics, etc.

## Dashboards
[Dashboard](https://help.tableau.com/current/pro/desktop/en-us/dashboards_create.htm) is a collection of several views. 

Dashboards size is fixed by you (so you can customize it for different devices). 

The layout of the dashboard needs to be designed by us but it also gives us a lot of flexibility in terms of how to organize different elements. To do it, we can use objects that could represent containers for the visuals, and other additions - it would a fixed layout using tiled objects. Besides having a fixed layout we can also mark elements as floating objects. Your dashboard layout is also visible in the layout tab / item hierarchy section. You can learn about different possibilities of dashboard organization in [this tutorial](https://help.tableau.com/current/pro/desktop/en-us/dashboards_organize_floatingandtiled.htm). 

## Stories
[Story](https://help.tableau.com/current/pro/desktop/en-us/stories.htm) is a sequence of visualizations that is meant to create a narrative using the insights from the data.

**Key steps to build a data story**

1. Look at the data. Which fields contain quantitative/categorical/geo data? What is the deepest level of granularity? Which questions can be answered with this data? Which calculated fields shall be added?

2. Think again. Who is your target audience? Which questions could be of most interest for them? Which data insights may bring the greatest value? 

3. Having the target audience and the questions in mind, think of the most suitable chart types for each question and possibly the high level key numbers to put on top. Make a few dashboard sketches

**Note 1:** In reality, it might take several iterations and a lot of communication with end users before a clear and insightful visualization is ready. So, keep things simple. Choose 3 - 4 charts per dashboard at max.

**Note 2:** Remember that different types of filters on the dashboard will help to add new perspectives, and to show new insights. However, some questions might require an additional dashboard with completely different visualizations, e.g. the bird-eye view with the insights on the whole year or more granular insights for the month or even the day 

4. Create the chosen views one after another. Use the dashboard template. Place the views on the dashboard. Add filters. Add more sophisticated filters (as [action filters](https://help.tableau.com/current/pro/desktop/en-us/actions_filter.htm)) only as the very last step. Publish or export the dashboard.

**Note:** Using dashboard templates helps to significantly speed up the process, and to make them look professional. Those are especially useful if you are working on visualizations as a team.

## Tableau Public
You can download your work in different form (pdf, presentation, workbook, ...) or save it in your Tableau Public. In order to do it you might need to create an [extract of your data](https://help.tableau.com/current/pro/desktop/en-us/extracting_data.htm) first.


![tableau story](/images/tableau_story.jpg)
{{< credits >}}
An example of a <a href="http://localhost:1313/07-tableau/dashboards-stories.html">Tableau story</a>
{{< /credits >}}

{{% notice reading "Get inspired!" %}}

Tableau Stories:
- [Data story showing development over time](https://public.tableau.com/app/profile/andy.kriebel/viz/EPLInjuries/InjuryCrisis)<br>
- [A drill down data story](https://public.tableau.com/app/profile/david.newman/viz/TheSimpsonsVizipedia/VisualizingTheSimpsons)<br>
- [A zoom out data story](https://public.tableau.com/app/profile/peacockworks/viz/VancouverCyclists/VancouverCyclists)<br>
- [A data story showing contrast](https://public.tableau.com/app/profile/robertrouse/viz/Pyramids_1/EgyptianPyramids)<br>
- [A data story showing outliers](https://public.tableau.com/profile/steph.baranya#!/vizhome/AdultVersion_final/SOSChildrensVillagesX-MasCampaignSantaGetInvolvedDonate)<br>
- [Different story types on the same dataset](https://public.tableau.com/app/profile/ben.jones/viz/WorldPopulationDay/1_ChangeOverTime?:embed=y&amp;:display_count=yes)

Other materials:
- [Best Practices for Designing Accessible Views](https://help.tableau.com/current/pro/desktop/en-us/accessibility_best_practice.htm)
- [More about dashboard layouts](https://www.thedataschool.co.uk/joe-beaven/layout-containers-how-to-get-your-item-hierarchy-under-control)
- [Pages playback](https://help.tableau.com/current/reader/desktop/en-us/pages_shelf.htm)

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}