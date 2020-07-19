<p align="center">
  <img src="https://github.com/akbloodadarsh/Twitter-Sentimental-Analysis/blob/master/Twitterlogo.png?raw=true">
</p>
<h1 align="center">Twitter-Sentimental-Analysis</h1>

#### ABOUT

A GUI software for sentimental analysis using python. I have used multiple algorithms and based on those shown independent outputs of every algorithm. On the CLI we can see the respective accuracy of each algorithm and we can analyze which performed the best. **The user will input a twitter username and the select number of tweets he wants to analyze. Then he/she will run the program and the output will be shown in a separate window for every tweet!**

#### Instruction to use
1. **Open [_`test.py`_](https://github.com/akbloodadarsh/Twitter-Sentimental-Analysis/blob/master/test.py)**
2. **Run**
3. **When the UI will show up, enter the username of the profile without using @**
4. **Use the slider to set the number of tweets you wanted to fetch**
5. **The result will show up.**

**Multinomial Naive Bayes, Random Trees Embedding, Random Forest Regressor, Random Forest Classifier, Multinomial Logistic Regression, Linear Support Vector Classifier, Linear Regression, Linear Classifier, Extra Tree Regressor, Extra Tree Classifier, Decision Tree Classifier, Binary Logistic Regression** get training data, testing data with features for which we have to predict our sentiment then we calculate accuracy score, confusion matrix and ROC(Receiver Operating Characteristic) and AUC(Area Under Curve) and return positive or negative emotions.

# File Details

<a href="https://github.com/akbloodadarsh/Negative-Tweet-Reporter-Automatic/blob/master/PreProcess.py">Preprocess.py</a>: It contains preprocessing function which performs following steps:- 
- It is getting the tweet  
- Removes URL using a regular expression.
- Removes emoticons using a regular expression.
- Removes username using a regular expression.
- Removes digit using a regular expression.
- Convert more than 2 letter repetitions to 2 letters.
- Removes symbols.
- Removes extra white spaces.
- Return preprocessed tweet.

<a href="https://github.com/akbloodadarsh/Negative-Tweet-Reporter-Automatic/blob/master/twitter_credentials.py">twitter_credentials.py</a>: 
In this file, we store our access token, access token secret, consumer key, and consumer secret.

<a href="https://github.com/akbloodadarsh/Twitter-Sentimental-Analysis/blob/master/test.py">test.py</a>: 
- The TwitterAuthenticator class inherits the OAuthHandler class and passes in the credentials to allow access to Twitter’s API features.
- The TwitterClient class contains all the methods to interact with Twitter API and parsing tweets. Use __init__ function to handle the authentication of the API client.
- Create a object of class TwitterClient() and use the object to get twitter client API using get_twitter_client_api() function.
- create a window using Tkinter and let the user input the hashtag.
- Use API to search for the tweets of the inputted hashtag and store the tweets.
- Extract the labels and sentences and store the outcomes in y and after preprocessing the tweets store them in x.
- Then used count Vectorizer to lowercases text, performed tokenization (converts raw text to smaller units of text), used word-level tokenization (meaning each word is treated as a separate token), ignored single characters during tokenization.
- Now one iterate the tweets and one by one preprocess and transform the tweets and do predictions.

<a href="https://github.com/akbloodadarsh/Twitter-Sentimental-Analysis/blob/master/twitter_credentials.py">twitter_credentials.py</a>: In this file we store our access token,access token secret, consumer key and consumer secret.

<a href="https://github.com/akbloodadarsh/Twitter-Sentimental-Analysis/blob/master/AllImport.py">AllImport.py</a>: This contains all the imported modules in one place so that we don't have to include it in every file, thus reducing the redundancy.

#### Future Improvements
* **Maybe we are gonna add a module that will analyze the image which is attached to a tweet. (If available by tweepy or other API)** 
* **A hashtag analysis section which analysis** **N** ** several tweets and based on the tweets will give sentiments of people in %.Ex:-**  
  1. **Angry n% Sad n% Happy n%**
  2. **Positive n% Negative n%**

<ul>
  
 #### Prerequisite(Personally found these links most helpful)
<li> <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#:~:text=sklearn.metrics.,set%20of%20labels%20in%20y_true.">accuracy score</a></li>
<li>	<a href="https://muthu.co/understanding-the-classification-report-in-sklearn/#:~:text=A%20Classification%20report%20is%20used,predictions%20from%20a%20classification%20algorithm.&text=The%20report%20shows%20the%20main,positives%2C%20true%20and%20false%20negatives.">Classification report </a></li>
<li>	<a href="https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62">Confusion Matrix</a></li>
<li>	<a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">TfidVectorizer</a></li>
<li>	<a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html">TfidTransformer</a></li>
<li>	<a href="http://kavita-ganesan.com/tfidftransformer-tfidfvectorizer-usage-differences/#.Xu9xuXUzaT_">Difference fidftransformer-tfidfvectorizer</a></li>
<li>	<a href="https://kavita-ganesan.com/what-are-n-grams/">N-Grams</a></li>
<li>	<a href="https://kavita-ganesan.com/how-to-use-countvectorizer/#.Xu9m0HUzaT8">CountVectorizer</a></li>
<li>	<a href="https://www.nltk.org/_modules/nltk/stem/wordnet.html">lemmatization</a></li>
<li>	<a href="https://textblob.readthedocs.io/en/dev/">TextBlob</a></li>
<li>	<a href="https://stackoverflow.com/questions/33091376/python-what-is-exactly-sklearn-pipeline-pipeline">Pipleline</a></li>
<li>	<a href="https://www.geeksforgeeks.org/naive-bayes-classifiers/">naive bayes classifier</a></li>
<li>	<a href="https://towardsdatascience.com/fit-vs-transform-in-scikit-libraries-for-machine-learning-3c70e6300ded">fit and transform</a></li>
  </ul>
