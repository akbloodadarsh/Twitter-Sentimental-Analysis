# It will import all the modules stored in AllImport module
from AllImport import *
# Use hashtag and classify in % how many sentiments are +ve and -ve based on fetched tweets
from tkinter import *
import time


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# To authenticate and access the twitter
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# get all the data of the tweets and,pass only tweets text to preprocess and finally returns only the processed tweets
def process(data):
    temp = []
    for text in data['sentence']:
        text = pp.pre_processing(text)
        temp.append(text)
    data['sentence'] = temp
    return data['sentence']


def execute():
    try:
        user = Entry1.get()
        num_tweets = w.get()
        twitter_client = TwitterClient()
        api = twitter_client.get_twitter_client_api()
        tweets = api.user_timeline(screen_name=user, count=num_tweets)
        tweets_text = []
        for tweet in tweets:
            tweets_text.append(pp.pre_processing(tweet.text))
        datafile = pd.read_csv('Train.csv', sep=',', encoding="utf-8")
        x = process(datafile)
        y = datafile['label']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        vector = CountVectorizer()
        vector.fit(x_train)
        x_train_vft = vector.transform(x_train)
        x_test_vft = vector.transform(x_test)

        count = 1
        for tweet in tweets_text:
            mainwindow = Tk()
            Label(mainwindow, text=str(count)+":- "+tweet, bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            # print(count, tweet)
            count += 1
            tweet = [tweet]
            vec = vector.transform(tweet)

        # Multinomial Naive Bayes-Every feature is independent,probability is cal and highest one will be o/p,fastest
            Label(mainwindow, text="Multinomial Naive Bayes", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = mnb.MultinomialNBAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            """
        Regression analysis is an important tool for modelling and analyzing data. Here, we fit a curve/line to the data
        Points,in such a manner that the differences b/w the distances of data points from the curve/line is minimized.
            a topic of some context.Ex:context:-road accident,topic:-car accident,it can happen or not happen
            """

            """
            Logistic Regression-It can give a binary or multi result(positive/negative/neutral),has a range 0 to 1
            # used for category data.Its has a curve.3 Types
            # lbgfs or lmbgfs is Limited memory Broyden–Fletcher–Goldfarb–Shanno Algo.Memory optimization algo
            # newton-cg:- newton's method for Large Bound-Constrained Optimization
            # multi-calss tells which logistic regression is being used
            """

            # 1:-OrdinalLogisticRegression not used because it takes at lest 3 categories but we have 2,+ve and -ve

            # 2:-Multinomial Logistic Regression-Used for 2 or more category,vision-shortsight,longsight,perfect
            Label(mainwindow, text="Multinomial Logistic Regression", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = mlr.MultinomialLRAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # 3:-Binary logistic regression-Used for 2 category,good,bad
            Label(mainwindow, text="Binary logistic regression", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = blr.BinomialLRAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

        # LinearRegression-find optimal line b/w the 2 data,where one data is independent(text),and other is dependent
            # (type-pos/neg) on another
            # lr.LinearRegressionAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            """
        SVM(support vector machine)-takes data as i/p and o/p a line that separates those classes[pos/neg] if possible
        we find the points closest to the line from both the classes.These points are called support vectors.we compute 
            the distance between the line and the support vectors. This distance is called the margin. Our goal is to 
        maximize the margin. The hyperplane for which the margin is maximum is the optimal hyperplane.Thus SVM tries to
        make a decision boundary in such a way that the separation between the two classes(that street) is as wide as 
            possible
            """

            # Linear Classifier
            Label(mainwindow, text="Linear Classifier", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = lc.LinearClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # LinearSupportVectorClassifier-LinearSeparationOfDataHappensOptimalLineIsDrawn using margins b/w both data
            Label(mainwindow, text="LinearSupportVectorClassifier", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = lsvc.LinearSupportVectorClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # Decision Tree Classifier
            Label(mainwindow, text="Decision Tree Classifier", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = dtc.DecisionTreeClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # Random Forest classifier
            Label(mainwindow, text="Random Forest classifier", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = rfc.RandomForestClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # Extra Trees Classifier
            Label(mainwindow, text="Extra Trees Classifier", bg="black", fg="white").pack(side=TOP, fill=X, padx=2)
            temp = etc.ExtraTreesClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            Label(mainwindow, text=temp, bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)

            # Random Trees Embedding
            # Label(mainwindow, text="Random Trees Embedding").pack(side=TOP)
            # rte.RandomTreesEmbeddingAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            # Label(mainwindow, text=temp).pack(side=TOP)

            # Random Forest Regressor
            # Label(mainwindow, text="Random Forest Regressor").pack(side=TOP)
            # rfr.RandomForestRegressorAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            # Label(mainwindow, text=temp).pack(side=TOP)

            # Extra Trees Regressor
            # Label(mainwindow, text="Extra Trees Regressor").pack(side=TOP)
            # etr.ExtraTreesRegressorAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
            # Label(mainwindow, text=temp).pack(side=TOP)
    except Exception as e:
        # Print the error
        print(e)

        # When reach the rate limit
        def on_limit(self, track):
            # Print rate limiting error
            print("Rate limited, continuing")
            # Continue mining tweets
            return True
        # When timed out

        def on_timeout(self):
            # Print timeout message
            print(sys.stderr, 'Timeout')
            # Wait 10 seconds
            time.sleep(10)
            # Return nothing
            return


if __name__ == "__main__":
    mainwindow = Tk()
    mainwindow.title("Twitter Sentimental Analysis Engine")
    Label(mainwindow, text="TWITTER SENTIMENTAL ANALYSIS ENGINE", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
    photo = PhotoImage(file="Twitterlogo.png")
    Label(mainwindow, image=photo, bg="black", fg="white").pack(side=TOP, fill=X)
    Label(mainwindow, text="USERNAME", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
    Entry1 = Entry(mainwindow)
    Entry1.pack(side=TOP, padx=2, pady=2)
    Label(mainwindow, text="NUMBER OF TWEETS", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
    w = Scale(mainwindow, from_=1, to=10, orient=HORIZONTAL)
    w.pack(side=TOP, fill=X, padx=2, pady=2)
    But1 = Button(mainwindow, text="RUN", command=execute)
    But1.pack(side=TOP, fill=X, padx=2, pady=2)
    mainwindow.mainloop()
