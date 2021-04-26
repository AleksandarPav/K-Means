# K Means
 
KMeans Clustering is used to cluster Universities into two groups, Private and Public. Despite having the labels for this data set, they are not used for the KMeans clustering algorithm, since that is an unsupervised learning algorithm. They are used only for evaluation. Data contains 777 observations on the following 18 variables:

Private A factor with levels No and Yes indicating private or public university

Apps Number of applications received

Accept Number of applications accepted

Enroll Number of new students enrolled

Top10perc Pct. new students from top 10% of H.S. class

Top25perc Pct. new students from top 25% of H.S. class

F.Undergrad Number of fulltime undergraduates

P.Undergrad Number of parttime undergraduates

Outstate Out-of-state tuition

Room.Board Room and board costs

Books Estimated book costs

Personal Estimated personal spending

PhD Pct. of faculty with Ph.D.’s

Terminal Pct. of faculty with terminal degree

S.F.Ratio Student/faculty ratio

perc.alumni Pct. alumni who donate

Expend Instructional expenditure per student

Grad.Rate Graduation rate

Grad.Rate versus Room.Board are compared, where the points are colored by the Private feature, as well as F.Undergrad versus Outstate. Histogram is drawn for Out-of-state tuition and for F.Undergrad features, both separated by the value of Private feature. Percentage greater than 100 is set to 100. Data is fitted to a KMeans model and evaluated with confusion matrix and classification report.
