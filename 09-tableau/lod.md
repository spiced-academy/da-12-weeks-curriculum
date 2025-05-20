---
title: "Level of Detail Expression"
weight: 60
---

![interactive](/images/detail.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@helloimnik?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Hello I'm Nik</a> on <a href="https://unsplash.com/s/photos/expressions?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

## Inspiration / goal
We will create the first of the KPI dashboards:

- **KPIs map dashboard**
![kpi_dashboard1_drawing](/images/kpi_dashboard1.png)
  

## **Calculated field types**

**Basic** - transform values or members at the data source level of detail (a row-level calculation) or at the visualization level of detail (an aggregate calculation)

**Table calculations** - happen at the level of detail of the visualization only

**Level of detail expressions** - give control on the custom level of granularity: at a more granular level (INCLUDE), a less granular level (EXCLUDE), or an entirely independent level (FIXED)


## Level of Detail (LoD) Expressions
[Level of Detail](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm) is a feature in Tableau that is enabling you to customize the level of detail or granularity of your analysis. LOD are implemented as calculated fields with a specified syntax.

### Level of Detail
What does level of detail mean? It refers to how many details we would like to see or on the contrary how much we want to generalize our insights. High level of detail will be less granular and more aggregated (summary style) and low level of detail will be more detailed and granulated.

### LoD syntax 

A calculated field representing an LoD would follow the syntax:

*{ type_of_lod [dimension_declaration]: aggregate_expression }*

where:
-  `type_of_lod` - type of LoD, could be either `fixed`, `include` or `exclude`
- `dimension declaration` - (optional) one or more dimension (or none) that the aggregation will be applied to
- `aggregate expression` - the calculation that will be applied to the new dimension (level of detail)

## **LoD types**

- **FIXED** - compute aggregates, broken down by specified dimensions. Without a reference to any dimensions in the view. Fixed calculations ignore all filters other than context filters, extract filters, and datasource filters

- **INCLUDE** -  compute aggregates using the specified dimensions, and the dimensions in filters or the view. Useful to include the dimension that isn’t in the view

- **EXCLUDE** -  explicitly remove the dimensions from the view level of detail


## Filters Hierarchy
### Order of operations
![order pic](/images/order_operations.png)

Tableau has a certain order of operations (query pipeline) in which it performs various actions.

As you build a view and add filters, those filters always execute in the order established by the order of operations. Some use cases might require converting a dimension filter to a context filter or using a table calculation instead of a dimension filter.



{{% notice reading "Reading" %}}
Additional materials:
- [cohort analysis in Tableau](https://www.rigordatasolutions.com/post/cohort-analysis-in-tableau)

{{% /notice %}}

<br>

{{% notice copyright "Agnieszka Kaczmarczyk, Katherina Arsh" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}