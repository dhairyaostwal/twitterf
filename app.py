from flask import Flask, render_template , request , abort
import pickle
import requests
import os
import json
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier           # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split      # FOR train_test_split function
from sklearn.metrics import confusion_matrix, accuracy_score

#print(twee.statuses_count,twee.followers_count,twee.friends_count,twee.favourites_count,twee.listed_count)


app=Flask(__name__)



# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAAU9UgEAAAAA4nxUc8ytyli45TIiDGEduvGLXLM%3DydT6bOgTeAy7mhxGyq2nyfQPyEIdpXqVvFmA1aM5vO3xbRPEVH'
bearer_token = os.environ.get('TOKEN')



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r





@app.route('/')
def index():
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
    
    return render_template("404error.html"),404


@app.route('/', methods=['POST'])
def my_form_post():
    global username
    username = request.form['username']
    search_url = "https://api.twitter.com/1.1/users/show.json?screen_name="+username
    def connect_to_endpoint(url):
        response = requests.request("GET", search_url, auth=bearer_oauth,)
        if response.status_code != 200:
            abort(404,description="Not found.")
        return response.json()
    
    url = search_url
    json_response = connect_to_endpoint(url)
    x=json.dumps(json_response, indent=4, sort_keys=True)
    global y,screen_name
    y=json.loads(x)
    global statuses_count
    statuses_count=int(y['statuses_count'])
    global followers_count 
    followers_count=int(y['followers_count'])
    global friends_count
    friends_count=int(y['friends_count'])
    global favourites_count 
    favourites_count=int(y['favourites_count'])
    global listed_count
    listed_count=int(y['listed_count'])
    global full_name
    full_name=y['name']+" "+y['screen_name']

    screen_name=y['screen_name']
    name=y['name']
    def maxSubsequence(screen_name, name): 
    # find the length of the strings
        global m,n 
        m = len(screen_name) 
        n = len(name) 
  
    # declaring the array for storing the dp values 
        global L
        L = [[None]*(n + 1) for i in range(m + 1)] 
  
        for i in range(m + 1): 
            for j in range(n + 1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif screen_name[i-1] == name[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
        return L[m][n]

    print(statuses_count,followers_count,friends_count,favourites_count,listed_count)


    def normaliseNameWeight(y):
        name = y['name']
        subseq = maxSubsequence(screen_name,name)
        return (subseq/len(name))

    name_wt=normaliseNameWeight(y)

    arr = np.array([[name_wt,statuses_count,followers_count,friends_count,favourites_count,listed_count]])
    global z
    z=pd.DataFrame(arr)
    print(z)
    with open('pickleOutput', 'rb') as f:
        mp = pickle.load(f)
    
    pickleTest = mp.predict(z)
    if  pickleTest==1:
        print("YES")
    else:
        print("NO")
    return 'ok'
    


@app.route('/predict')
def predict():
    return "<h1>{{pickleTest}}</h1>"





if __name__ == "__main__":
    app.run(debug=True)