# MFk-M Clustering

It is very difficult to get insights from raw data for which one generally approaches the K means mehod but clustering is challenging while dealing with Categorical dataset of Multidimenions to get raw insights before moving forward to analysis and gauge understanding out of it.
we have got different approach to solve the problem through K-Modes or K-Means++ for Categorical dataset and Mixed type dataset respectively

The Solution focuses on solving the Problem to get into root of it by converting categorical column values to continuous value using Frequency of occurence method and then using high performance of K-Means to get desired result

# Problem Statement 
To do clustering on Multidimensional Categorical dataset and generate insigt from the Data


# Reference
I referred research Paper Titled: 
"A fast and effective partitional clustering algorithm for largecategorical datasets using a k-means based approach"

# Abstract of paper:
"Partitional clustering algorithms represent an interesting issue in pattern recognition due to their high scalability and efficiency. The k-means, proposed since 1965, had shown great efficiency for numeric clustering but is unfortunately inadequate for categorical clustering. In 1998, the kmodes was proposed as an extension of the k-means to cluster categorical datasets. In this paper,a new categorical method based on partitions called Manhattan Frequency k-Means (MFk-M) is detailed. It aims to convert the initial categorical data into numeric values using the relative frequency of each modality in the attributes. The L1 Norm (Manhattan distance) was also used as an evaluation distance measure to compute the distance between the observations and the centroids. Finally, an approximation is defined to evaluate each resulting partition during the execution of the algorithm to avoid trivial clusterings such as cluster death. Experimental analysis performed on real life datasets highlights the reduced complexity costs and high efficiency
of our proposal when compared to the standard k-means and k-modes algorithms."

# Guide
-----> Transform_data.py file converts the values of categorical columns of dataset as per relative frequency of it's occurence
        in the dataset making it's value continuous and converting the data in range of (0,1]
        
-----> mfk_means_implementation.py file is scratch implementation of K-Means Clustering using L1 Norm as distance Measure instead 
       of Euclidean Distance, (answer to this is from Research Paper)

-----> Elbow test is also added to find Optimal K for Partitional Clustering
