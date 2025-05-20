---
title: "Multiple Data Sources"
weight: 80
---

![interactive](/images/blender.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@badgerblack?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kaur Kristjan</a> on <a href="https://unsplash.com/s/photos/blender?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

## Inspiration / goal
We will make all of the dashboards more interesting using a customized color palette.

## Palettes
Tableau has a set of default settings which includes colors and styles, etc. It is also customizable and you can always change the settings according to your needs and preferences. However, if you have a preferable set of colors you could set up a [customized color palette](https://help.tableau.com/current/pro/desktop/en-us/formatting_create_custom_colors.htm) to make it consistent. 

In order to do it, you have to modify your `Preferences.tps` file which is located in your `My Tableau Repository` directory. To add Spiced color palette, append this code to the end of the file (don't remove the previous content!):
```
<workbook>
  <preferences>
    <color-palette name="Spiced" type = "regular">
      <color>#FB8314</color>
      <color>#D46C4C</color>
      <color>#3F0097</color>
      <color>#844AD4</color>
      <color>#3F0097</color>
      <color>#FB0404</color>
      <color>#E6E6E6</color>
      <color>#FFADB9</color>
    </color-palette>
   </preferences>
</workbook>
```


## Data Blending

### **Working with multiple data sources**

**Relationship** - Does not merge data together to create a new, fixed table. During analysis, queries the relevant tables automatically using the contextually-appropriate joins to generate a custom table of data for that analysis. Maintains the native level of detail, does not lose data, keeps appropriate aggregations, and handles nulls. Read more [here](https://help.tableau.com/current/pro/desktop/en-us/datasource_relationships_learnmorepage.htm)

**Union** - The data is appended (add new rows of) across the same basic column structure to form a new fixed table

**Join** - Two tables of data based on a join clause and join type are merged to form a new, fixed table of data. Often used to add new columns of data across the same basic row structure. May cause data loss or duplication

**Data blending** - Data across two or more Tableau data sources remains separate. Tableau queries the data sources independently and visualizes the results together in the view, based on the linking fields established for that sheet. Mimics the behavior of a left join and may filter data from secondary data sources

### **Data blending recommendations**

- Data blending happens within the worksheet, not the datasource
- Blend on the least granular level 
- Ensure that the connections are activated
- Be aware which datasource is primary. It is not possible to change the primary and secondary data sources order later. The order of blending will influence the structure of the results (watch this [example](https://www.youtube.com/watch?v=dC10teRrv-k&ab_channel=sqlbelle))
- The data source containing the filter fields should be set as primary. It’s not always possible to filter from the secondary datasource to the primary, as the merging mimics the left join
- If you join on a string field, remember that joins are case sensitive

<br>

{{% notice copyright "Katerina Arsh, Agnieszka Kaczmarczyk" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
