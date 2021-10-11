# twitterf
Identification of Fake Twitter Users

<h1 align="center"><img width="200px" height="auto" src="https://user-images.githubusercontent.com/50984984/129434228-e72ed30e-cda9-4781-b4cb-ba0a07c21252.png"/></h1>

Link to dataset: [Efficient detection of fake Twitter followers](http://mib.projects.iit.cnr.it/dataset.html)

## Approach

1. Data preprocessing removing NaN etc.
2. Model Training and Accuracy = Decision Tree Classfication 
3. Creation of pickle file

## Features to be passed as Parameters

['name_wt',
 'statuses_count',
 'followers_count',
 'friends_count',
 'favourites_count',
 'listed_count']
 
 and will return `label` value which would indicate fake or genuine/true Twitter user.
 
<h1 align="center"><img src="https://user-images.githubusercontent.com/50984984/129464986-95e8459c-c2e2-4e48-b277-a8a8a1fe2cab.png"/></h1>


| parameters | in Twitter terms |
|--|--|
| status_count | number of tweets |
|followers_count|followers|
| friends_count | following |
|favourite_count|no. of likes|
|listed_count |no. of list |


## Requirements:

1. Function to calc `name_wt` to be passed in as parameter
2. Frontend
3. Server Flask
