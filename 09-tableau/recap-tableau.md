---
title: "Recap: Tableau"
weight: 90
---

![interactive](/images/presentation.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@campaign_creators?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Campaign Creators</a> on <a href="https://unsplash.com/s/photos/presentation?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
{{< /credits >}}

All the tools that you have learned so far have their own use case. Even though there are plenty of orvelaps between them, very often they coexist together. It is very common to use all SQL, python and Tableau (and/or other tools) for a single project. 

## Get inspired
As Tableau gives you a lot of opportunities to customize your work, but sometimes it's really hard to decide on what should be done and you might feel overwhelmed. Feel free to get inspired by others.

{{% notice reading "Reading" %}}
- [a data story showing development over time and different story types](https://public.tableau.com/app/profile/ben.jones/viz/WorldPopulationDay/1_ChangeOverTime?:embed=y&amp;:display_count=yes)
- [a powerful story using outliers](https://public.tableau.com/app/profile/steph.baranya/viz/AdultVersion_final/SOSChildrensVillagesX-MasCampaignSantaGetInvolvedDonate)
- [a data story showing contrast](https://public.tableau.com/app/profile/robertrouse/viz/Pyramids_1/EgyptianPyramids)
- [a zoom out data story](https://public.tableau.com/app/profile/peacockworks/viz/VancouverCyclists/VancouverCyclists)
- [a drill down data story](https://public.tableau.com/app/profile/david.newman/viz/TheSimpsonsVizipedia/VisualizingTheSimpsons)
- [a development in time data story](https://public.tableau.com/app/profile/andy.kriebel/viz/EPLInjuries/InjuryCrisis)
{{% /notice %}}

### Viz of the Day
Tableau highlights new interesting dashboards every weekday with [Viz of the Day](https://public.tableau.com/app/discover/viz-of-the-day). If you are interested in how some Viz of the Days were implemented you can download the workbook and study it.


## Practise
The best way to learn Tableau is just to practise. Fortunately, besides all amazing documentations (including the [official Tableau website](https://www.tableau.com/resources/reference-materials)), there are also a lot of youtube video tutorials and other resources like [Workout Wednesday](https://www.workout-wednesday.com/wow-essentials-tableau/) where a new Tableau challenge is posted every week (together with a solution later on).


## Git and big files
During this week you were working with bigger data files. Normally, with git repositories you are able to push the files that are only up to 100MB big. That means that before comitting your data files you would like to check their size, and in case they are bigger than 100MB you can compress them first or not include them at all (e.g. when a compressed file is still exceeding this limit or you don't want to expose the whole dataset publicly). 

### Version controlling big files - Git LFS 
If you really want to store bif files in your git repository you can use [Git LFS](https://git-lfs.github.com/) which is an open source git extension that helps administrating this process.


### Reverting commited changes on git
If you did commit a huge file locally and realizing when trying to push it that you exceeded the limit of the file size you can still revert the history of your changes. The `--amend` flag used with `git commit` command is able to update the files in your local commits. Study this [article](https://www.atlassian.com/git/tutorials/rewriting-history) to see the examples of the usage of this flag.

 <br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katerina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}