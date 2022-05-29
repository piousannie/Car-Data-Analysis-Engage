# Car Data Analysis Project for Engage

## Technology Stack Used-
<p align="left">

<a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a>
<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" width="36" height="36" alt="MySQL" /></a>
<a href="[https://powerbi.microsoft.com/en-au/]" target="_blank" rel="noreferrer"><img src="![image](https://user-images.githubusercontent.com/78022265/170844442-0e434d35-1820-4876-9c3e-cef720f222c4.png)" width="36" height="36" alt="PowerBI" /></a>
</p>

## Introduction-

HTML-CSS is used at frontend for the purpose of our web-based application project. Jupyter Notebook is used at the backend to generate the data analytics using Pythonic libraries such as Numpy, Pandas, Matplotlib, SeaBorn and Plotly to execute Exploratory Data Analysis(EDA) and deliver useful graphs and insights. The report follows a mathematical approach using k-means clustering to acheive the objective of identifying clusters of correlation. MySQL is used for identifying relationships and queries among the various variables. Python codes are used for cleaning data. PowerBI is used for  interactive data visualization which makes the analysis of data easier.

## Challenge-

The automotive industry is one of the largest industries out there it's a 2.6 trillion dollar industry! India's Automotive Industry is worth more that USD 100 billion and contributes 8% of country's total export. The industry accounts for 2.3% of India's GDP and is set to become the 3rd largest in the world by 2025. The industry consists of many categories and subcategories which are thereby constructed by many variables that it can be said that every category is an industry in itself. 

For instance the car body type variable is a vital one, here is a list of the car body types used by our data-

1. SUV(Sport Utility Vehicle)
2. Sedan
3. Hatchback
4. Coupe
5. MPV(Multi-Purpose Vehicle)
6. MUV(Multi Utility Vehicle)
7. Covertible
8. Crossover
9. Pick-Up
10. Sports

And all of the variety above is only regarding the car body type which is only one variable! Similarly, 40+ car manufacterers can be identified in the given dataset. Not to mention the grey areas where some car body types can be irrelevant to customer decision.

## Data-

The dataset used in this report contains cars with their variants with 1200+ model/variants to study over 150+ features. Cleaning of data is done by running a series of python codes for removal of units, irregularities, etc. For example- Power and torque are equalised at 1000rpm each for the sake of comparision and the mode of the variables/ features has been used to fill in the empty cells where the data was unavailable. 

Additional data was used from the internet to support the analysis and gather an approach for query solution.

## Exploratory Data Analysis-

## Cars Count by Make-

![image](https://user-images.githubusercontent.com/78022265/170819855-c3952572-c2ed-450b-8b74-2280c351cfe5.png)

### Key Findings-
1. The Top 5 companies with more than car variants in India are Maruti Suzuki, Hyundai, Mahindra, Tata, and Toyota.
2. Sports car variants are low.

## Cars Count by Car Body Type-

![image](https://user-images.githubusercontent.com/78022265/170820122-2f0b873e-028c-42f3-81f3-b1d5da170333.png)

### Key Findings-
1. The Top 3 body types in India are Hatchbacks, SUVs and Sedans.

## Cars by Cylinders-

![image](https://user-images.githubusercontent.com/78022265/170819968-a3767411-c241-4e9c-9599-e3d491d311a0.png)

### Key Findings-
1. Most cars use 4 cylinders followed by 3 and 6 cylinders.

## Cars by Seating Capacity-

![image](https://user-images.githubusercontent.com/78022265/170820026-94d3c006-70ef-4794-bffc-54f52a4218aa.png)

### Key Findings-
1. Most cars are 5 seaters followed by 7 seaters.

## Cars Count by Engine Fuel Type-

![image](https://user-images.githubusercontent.com/78022265/170820657-cb6bda27-9d66-4110-8579-a8009c73aadd.png)

![image](https://user-images.githubusercontent.com/78022265/170820084-110175d3-9b3b-4059-9f26-02a3690c44c6.png)

### Key Findings-
1. Most cars use Petrol and Diesel.

## Cars count by Engine Size w.r.t Displacement-

![image](https://user-images.githubusercontent.com/78022265/170820696-690bf936-9c99-4e5f-8068-4b520b54ed72.png)

## Cars count by Engine Size w.r.t Power-

![image](https://user-images.githubusercontent.com/78022265/170820702-de123cc4-0bbe-4ad9-a188-951aa5385807.png)

## Relationship between Displacement and Price-

![image](https://user-images.githubusercontent.com/78022265/170820184-7ec5f3d5-ac07-4013-b92b-906a5822ea02.png)

### Key Findings-
1. Displacement is directly proportional to Price; Higher the price, higher the displacement.

## Relationship between power and price-

![image](https://user-images.githubusercontent.com/78022265/170874377-ec91fe12-2690-4689-b80b-4597ed6712a1.png)

### Key Findings-
1. Horsepower of car is related to car price.
2. Hatchbacks are the body type with the least horsepower and price.

# Relationship between price and mileage-

![image](https://user-images.githubusercontent.com/78022265/170875407-23f8159c-c13d-4ca2-ab48-e4791dae4952.png)

### Key Findings-
1. Expensive cars tend to have worse mileage and vice versa.

## Checking Ex-Showroom Price distribution using normal and log scales due to the huge difference in prices-

![image](https://user-images.githubusercontent.com/78022265/170820380-a92a84e0-f009-4e1d-831c-9b2bbc9c5b07.png)

### Key Findings-
1. There is a lot of variance in price that can be checked by plotting a box plot

## Box Plot for Ex-Showroom price-

![image](https://user-images.githubusercontent.com/78022265/170820422-1c4abe88-3747-4a52-a3bc-5c03bff79449.png)

### Key Findings-
1. There are a lot of outliers.
2. Outliers are mostly from the Sports and Coupe category as shown in the box plot below.

## Box Plot of price vs. body type-

![image](https://user-images.githubusercontent.com/78022265/170820535-6c0f0ada-c311-4e88-addb-2076ca09e19f.png)

### Key Findings-
1. Car body type affects the price.

## Plotting an extensive scatter plot grid of more numerical variable to investigate the relation in more data-

![image](https://user-images.githubusercontent.com/78022265/170837074-82d01442-55df-4dad-9d0a-318beb71545c.png)

### Key Findings-
1. There exists multicollinearity between variables.

Plotting pairwise relationships as pair plot visualization comes handy for Exploratory data analysis(EDA). Pairing plot visualizations from the given data helps find the relationship between them where the variables can be continuous or categorical.

![image](https://user-images.githubusercontent.com/78022265/170839214-8cd98e5b-f92e-4640-bda5-4a5b1c15c3f9.png)

### Key Findings-
1. Above graphs give a relationship between Displacement and Price with respect to the Fuel Type.

## Check for the overall correlation between variables using Pearson correlation matrix-

![image](https://user-images.githubusercontent.com/78022265/170838068-a25ca265-420d-46ad-ba5b-3a5c6fc9a4d9.png)

A correlation of -1.0 indicates a perfect negative correlation, and a correlation of 1.0 indicates a perfect positive correlation. If the correlation coefficient is greater than zero, it is a positive relationship. Conversely, if the value is less than zero, it is a negative relationship.

### Key Findings-
1. Price is positively related to Displacement
2. Price is positively related to Cylinders
3. Price is positively related to Power
4. Price is positively related to Torque
5. Displacement is positively related to Cylinders
6. Displacement is positively related to Power
7. Displacement is positively related to Torque
8. Displacement is positively related to Fuel Tank
9. Cylinders is positively related to Power
10. Cylinders is positively related to Torque
11. Cylinders is positively related to Fuel Tank
12. Power is positively related to Torque
13. Torque is positively related to Width
14. Torque is positively related to Length
15. Wheelbase is positively related to Power
16. Wheelbase is positively related to Torque
17. Wheelbase is positively related to Length
18. Doors is positively related to Seating Capacity
19. Fuel tank is positively related to Displacement.

## Other Challenges-

As shown in previous figures clustering the market needs a lot of effort as the separation of clusters is not that obvious. It's now clear that we have to look for many dimensions in order to cluster the automotive market. Since the more features we explore, the harder it is to cluster. These dimensions affect the decision of the buyers and is also preceived as totally different due to the various different mental models of buyers, in other words, price, horsepower and mileage are not everything and some buyers would like to have a long wheel base car, some would like to have wider car all of the previous features, and more, strongly affect the buyer' decisions.

This means that two cars can have a very similar price and milage but one is a van with lots of space and the other is just a four doors sedan, these two cars are precieved as two different categories in the automotive industry so space "length, width and height of the car" can also be a vital factor. So, a three dimensional representation won't tell everything, so thats why we will try to consider clustering to use the very different features associated with each car.

## Graphs and conclusions for the most sold car models

Now we can check for the most popular car specifications and combinations from the models with the most units sold, which are stated in order as below-

1. WagonR
2. Swift
3. Dzire
4. Nexon
5. Alto
6. Ertiga
7. Seltos
8. Venue
9. Eeco
10. Punch
11. Creta
12. Vitara Brezza
13. Celerio
14. Sonet
15. Grand i10
16. Baleno
17. i20
18. S-Presso
19. Amaze
20. Tiago

## Most sold cars count by car body type-

![image](https://user-images.githubusercontent.com/78022265/170864342-040a6a2d-7f31-4b76-8d42-f8b69b021ae5.png)

### Key Findings-
1. SUVs are the most sold car body type.

## Most sold cars count by make-

![image](https://user-images.githubusercontent.com/78022265/170864653-4f705e30-c59b-4c4b-a10e-b88fda7d6d51.png)

### Key Findings-
1. Maruti Suzuki is the most sold car manufacturer.

## Checking Ex-Showroom Price distribution using normal and log scales due to the huge difference in prices

![image](https://user-images.githubusercontent.com/78022265/170864357-e2b1aa2a-4930-4ce5-a659-f56bb177ced3.png)

## Most sold cars count by engine fuel capacity-

![image](https://user-images.githubusercontent.com/78022265/170864370-14d78689-61ac-4458-aa52-6a996490bcc2.png)

## Most sold cars count by power-

![image](https://user-images.githubusercontent.com/78022265/170864382-a012c0fd-1dea-4dfb-9ef3-895484bffeb6.png)

## Most sold cars count by torque-

![image](https://user-images.githubusercontent.com/78022265/170864609-f5ba5520-6842-46f0-940a-fc4244e0fc49.png)

## Most sold cars count by car type-

![image](https://user-images.githubusercontent.com/78022265/170864832-d9273b9d-455a-4fef-98e1-a4810ceb1ae4.png)

### Key Findings-
1. Manual cars are the most sold car type followed by automatic cars.

## Most sold cars count by minimum turning radius-

![image](https://user-images.githubusercontent.com/78022265/170864630-c5a15786-993a-4b09-b8b5-790b9766ea93.png)

## Conclusion-
1. 78.6% of the most sold cars had 4 cylinders
2. BS 6 accounted for 67.93% of most sold cars
3. 5 seaters consist of 91.83% of most sold cars
4. Maruti Suzuki is the most popular car manufacturer
5. SUV accounted for 38.59% of most sold cars.
6. Petrol cars accounted for 61.41% most sold cars.
7. 79% of most sold cars have 2 airbags.
8. 68.63% of most sold cars have 5 gears.

## Clustering

Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters). Clustering divides the data points into a number of groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups. It is basically a collection of objects on the basis of similarity and dissimilarity between them. It is the main task of an exploratory data analysis, and a common technique for statistical data analysis, used in many fields, including pattern recognition, image analysis, information retrieval, bioinformatics, data compression, computer graphics and machine learning. 

The appropriate clustering algorithm and parameter settings (including parameters such as the distance function to use, a density threshold or the number of expected clusters) depend on the individual data set and intended use of the results. Cluster analysis as such is not an automatic task, but an iterative process of knowledge discovery or interactive multi-objective optimization that involves trial and failure. It is often necessary to modify data preprocessing and model parameters until the result achieves the desired properties.

![image](https://user-images.githubusercontent.com/78022265/170839666-c916725a-d005-4060-8601-0ca3c1a004a4.png)

The type of clustering we are using here is K-Means clustering
K-Means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. K-means clustering minimizes within-cluster variances (squared Euclidean distances). 

Now we can check some scatter plots but by adding clusters.

## Plotting a 3D scatter plot to check for power, mileage and the car manufacturer-

![newplot](https://user-images.githubusercontent.com/78022265/170841793-cb105d25-bb88-454c-aef6-444a8fbe967a.jpg)

## Plotting a 3D scatter plot to check for price, power and the mileage-

![image](https://user-images.githubusercontent.com/78022265/170875137-cc0ea9aa-a408-4945-9971-42d24c93bf60.png)

## Average prices of each cluster are as follows-

![image](https://user-images.githubusercontent.com/78022265/170875293-d44494c0-4877-4310-8e93-478599d49f11.png)

## Number of cars existing in each cluster-

![image](https://user-images.githubusercontent.com/78022265/170875335-66f8be6e-2c3d-471b-8fe2-bb089e5e33a2.png)

# Car body types in each cluster-

![image](https://user-images.githubusercontent.com/78022265/170875511-326fc561-9c9a-4676-8b6c-6b7e478e1447.png)

## Price vs Power-

![image](https://user-images.githubusercontent.com/78022265/170863261-9142daba-1e02-49b8-8646-6374c5282e3a.png)

### Key Findings-
1. Clusters are strongly affected by the price with clear speration between clusters.
2. No clusters can be separated for displacement.
3. Expensive cares tend to have higher power and vice versa.

## Price vs Displacement

![image](https://user-images.githubusercontent.com/78022265/170863154-e6200d16-21b7-430b-a808-9a8a50192964.png)

### Key Findings-
1. Cluter separation can be performed on price.
2. No clusters can be formed for displacement.
3. Expensive cares tend to have higher displacement and vice versa.

## Price vs Cylinders

![image](https://user-images.githubusercontent.com/78022265/170863208-a073b387-d4f9-4849-96ed-ee4ef4649ab1.png)

### Key Findings-
1. Cluter separation can be performed on price.
2. No clusters can be formed for cylinders.
3. Expensive cares tend to have higher number of cylinders and vice versa.

## Price vs Torque

![image](https://user-images.githubusercontent.com/78022265/170863322-1a729cef-f13b-4db2-8db1-e60a759ef557.png)

### Key Findings-
1. Cluter separation can be performed on price.
2. No clusters can be formed for torque.
3. Expensive cares tend to have higher torque and vice versa.

## Cylinders vs Displacement

![image](https://user-images.githubusercontent.com/78022265/170863414-6acef260-4183-4078-aa95-e065fc9f5403.png)

### Key Findings-
1. Clusters are too sparse and blurry to be identified hence no conclusions can be made.

## Power vs Displacement

![image](https://user-images.githubusercontent.com/78022265/170863629-dbe522ab-7d42-43a7-bcec-97d0219e68dd.png)

### Key Findings-
1. Clusters are too sparse and blurry to be identified hence no conclusions can be made.

## Torque vs Displacement

![image](https://user-images.githubusercontent.com/78022265/170863679-8d585abd-653d-4c2d-9993-33e4f04f39ac.png)

### Key Findings-
1. Clusters are too sparse and blurry to be identified hence no conclusions can be made.

## Fuel Tank vs Displacement

![image](https://user-images.githubusercontent.com/78022265/170863689-842079cf-5b83-4ca4-bc44-5e4a2d53818f.png)

### Key Findings-
1. Clusters are too sparse and blurry to be identified hence no conclusions can be made.

## Power vs Cylinders

![image](https://user-images.githubusercontent.com/78022265/170863738-93259b0d-dd67-4a9f-8d06-8fdc86283e09.png)

### Key Findings-
1. Cluster separation can be performed on cylinders.
2. No clusters can be formed for Power.
3. High power cars tend to use a higher number of cylinders in them and vice-versa.

## Torque vs Cylinders

![image](https://user-images.githubusercontent.com/78022265/170863819-1fb6cbc8-d02f-4257-b518-28a770bce03e.png)

### Key Findings-
1. Cluter separation can be performed on cylinders.
2. No clusters can be formed for Torque.
3. High torque cars tend to use a higher number of cylinders in them and vice-versa.

## Fuel Tank Capacity vs Cylinders

![image](https://user-images.githubusercontent.com/78022265/170863862-b8b459c6-508d-45d3-ba41-5cca83a8f4c8.png)

### Key Findings-
1. Cluter separation can be performed on cylinders.
2. No clusters can be formed for fuel tank capacity.
3. Cars with a higher number of cylinders used in them tend to have a higher fuel tank capacity and vice-versa.

## Power vs Mileage

![image](https://user-images.githubusercontent.com/78022265/170863903-a2ff86e6-a2e5-440d-9e1b-29f72723070e.png)

### Key Findings-
1. Clusters are too close to each other and blurry to be identified hence no conclusions can be made.

## Mileage vs ex-showroom price

![image](https://user-images.githubusercontent.com/78022265/170864750-4804a741-0563-48a1-81ed-ab532c1f7ef7.png)

### Key Findings-
1. Cluster separation can be performed on mileage.
2. No clusters can be formed for ex-showroom price.
3. Mileage decreases as price increases and vice-versa.

## Power vs Fuel Tank-

![dsdcd](https://user-images.githubusercontent.com/78022265/170843570-bd32001e-dff4-4948-bede-3c7ac7363ba3.png)

### Key Findings-
1. Cluster separation can be performed on horsepower.
2. No clusters can be formed for fuel tank capacity.
3. Power decreases as fuel tank capacity increases and vice-versa.

## Why Clustering?

With clustering there are too many variables taken into consideration which are hard to be traced by other normal methods. The clusters generated by the K-Means model can be used to identify strategic groups that form a strong competition to the company products in the market and it also shows the close clusters for this group which also can be put into consideration in some cases. 

### Advantages of k-means include the following-
1. Relatively simple to implement.
2. Scales to large data sets.
3. Guarantees convergence.
4. Can warm-start the positions of centroids.
5. Easily adapts to new examples.
6. Generalizes to clusters of different shapes and sizes, such as elliptical clusters.

## Problems with clustering

As tempting as it's to use clustering to produce strategic groups it is worth mentioning that the clustering process itself is a little bit ambigous and contribution of features to the clustering process can't be easily explained so the overall interpretability of the model forms a challenge.

### Disadvantages of k-means includes the following-

1. Choosing value of k manually to find the optimal k.

2. Being dependent on initial values- For a low , you can mitigate this dependence by running k-means several times with different initial values and picking the best result. As  increases, you need advanced versions of k-means to pick better values of the initial centroids (called k-means seeding).

3. Clustering data of varying sizes and density- k-means has trouble clustering data where clusters are of varying sizes and density.

4. Clustering outliers- Centroids can be dragged by outliers, or outliers might get their own cluster instead of being ignored. Consider removing or clipping outliers before clustering.

5. Scaling with number of dimensions- As the number of dimensions increases, a distance-based similarity measure converges to a constant value between any given examples. Reduce dimensionality either by using PCA on the feature data, or by using “spectral clustering” to modify the clustering algorithm as explained below.

## Conclusion-
Data Analysis is the process of systematically applying statistical and/or logical techniques to describe and illustrate, condense and recap, and evaluate data. The dataset used in this report contained cars with their variants with 1200+ model/variants to study over 150+ features upon which Exploratory Data Analysis was performed to gain useful insights about the automative industry in India. Along with using clustering there were too many variables which were taken into consideration which are hard to be traced by other normal methods. The clusters generated by the K-Means model can be used to identify solutions for queries given in the problem statement. Clustering may be not determinant but it can be used to augment the management decision by using it alongside with human intuition to form the right strategic groups.

This is the end of the report. Thankyou!
