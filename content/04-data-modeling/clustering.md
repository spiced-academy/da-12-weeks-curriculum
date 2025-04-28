---
title: "Clustering"
weight: 80
---

![seasoning](/images/seasoning.jpg)

{{< credits >}}
Spices from <a href="https://www.freepik.com/free-photo/seasoning-ingredients-wooden-spoons_9095041.htm#query=spice&position=11&from_view=search">Freepik</a>

{{< /credits >}}

{{% notice warmup "Fossils" %}}

Look at the pictures available in this [google drive folder](https://drive.google.com/drive/folders/1TfJOg8hQFBRpkPQ1qqukV0Axh1XTm-K1?usp=sharing). How would you group the pictures? (You can create as many groups as you want.)

{{% /notice %}}


## What is Clustering?

**Clustering is an example of unsupervised learning.**

With clustering we find patterns of behavior in data, based on observed similarities. 
This approach can be used for example to cluster people into groups with similar genetics by using sequences of information from their DNA samples 
or to cluster some emails into spam box by using the features they have.

K-means is one of the most common clustering algorithms. The description of the K-means clustering algorithm is presented below. Bear in mind that even though the example below uses one dimensional example it could be easily extended into more dimensions.


## K-means Clustering algorithm
Follow the below steps - Step 1 and 2 are performed only once (the initiation of the algorithm) and the next steps are repeated over and over again until the finish conditions are met.

### 1. Select the number of clusters

First, we select the number of clusters we want to have. In this example we choose k equals two. 
The algorithm then randomly selects k points, in this case 2 points, on our axis, which we call our data centres or centroids. In our case, centroids are visualized as vertical lines.

![clustering_step1](/images/clustering_step1.jpg)


### 2. Calculate the distances

In the next step we calculate the distance from each data point to each of the centroids. 
In our example, distance is basically the difference between the value of a data point and the value of a centroid.

![clustering_step2](/images/clustering_step2.jpg)


###  3. Form the Clusters

Now, we can form the clusters by assigning each data point to one of the centroids, depending on which centroid is the closest to a data point.

![clustering_step3](/images/clustering_step3.jpg)


### 4. Update

In this step we are going to calculate the mean of each cluster. over the members of each cluster is then set as the new centroid. We ignore and dispense with the previous centroid value.

![clustering_step4](/images/clustering_step4.jpg)

### 5. Recursively run steps two to four
In this step we run steps from two to four recursively until the position of the centroids do not change and remain stable.

### Visualization of the algorithm
To see how K-Means clustering will work in a two dimensional space, run a visual simulation of this algorithm [here](http://alekseynp.com/viz/k-means.html).


## How do I choose the best k?

**The Elbow Method**

The elbow method is one of the most well-known methods in machine learning and could be also used for finding the optimal number of clusters. With calculating the **Within-Cluster-Sum of Squared Errors ([WSS](https://medium.com/analytics-vidhya/how-to-determine-the-optimal-k-for-k-means-708505d204eb))** for different values of k we can choose the k for which WSS first starts to decrease. In a plot this will show an elbow joint.

![clustering_elbow](/images/clustering_elbow.jpg)


## Reminder!! 

**Feature Scaling is an important technique that mostly comes to the picture during pre-processing step in Machine Learning.**
 
We use feature scaling when the variables in the data set have large differences in order of magnitude, or when they are similar in that sense but measured with different metrics such as meters vs kilometers, etc. 
These differences cause problems for many models. For example, if one of the features has a way higher order of magnitude, this particular feature will dominate over the other ones.

In order to avoid this issue, we will perform feature scaling which brings all of the measurements into a similar range of values.


## Project Challenges

{{% notice challenge "Cluster Analysis of Car Price and Fuel Consumption" %}}

To succeed in the highly competitive automotive industry, it is important to understand customer preferences and target specific market segments. It is crucial for a car business to identify and offer products to distinct groups of customers based on factors.

In this challenge, we try to cluster cars based on their price and fuel consumption attributes. By analyzing these clusters, we can gain a deeper understanding of the market landscape and identify target customer segments with similar preferences and needs. 

Follow the steps below in order to accomplish this:

1. Read in the cleaned and imputed dataset that you have saved in the impute missing values challenge

2. Subset the price and fuel consumption related information    

3. Check the distribution of data and standardize it if necessary

4. Use the elbow method to determine the number of clusters

5. Repeat k-means clustering using the appropriate number of clusters selected from the elbow method. Visualize the results.

6. What information can you provide regarding the various clusters?




{{% /notice %}}

{{% notice reading "Reading" %}}

- [How to Determine the Optimal K for K-Means?](https://medium.com/analytics-vidhya/how-to-determine-the-optimal-k-for-k-means-708505d204eb)

{{% /notice %}}

<br>

{{% notice copyright "Hilal Işık, Samuel McGuire, Agnieszka Kaczmarczyk, Milad Behrooz" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}