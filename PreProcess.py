# sequence of characters that forms a search pattern
import re

def pre_processing(tweet):
    s = ""
    # URL Removal
    tweet = re.sub(r'http\S+', '', tweet)

    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', '', tweet)

    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', '', tweet)

    # Love -- <3, :*, 💙
    tweet = re.sub(r'(<3|:\*|💙)', '', tweet)
    tweet = re.sub(r'(🥰|💓|💖|💗|💞|💘|💘|💓|❤|💚|🧡|🧡|💞|💓|💖|💕|💘|💞|öö|🙃|👀|👇|🔵)', '', tweet)

    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', '', tweet)

    # Sad -- :-(, : (, :(, ):, )-, :
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', '', tweet)

    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', '', tweet)

    # username removal
    tweet = re.sub('@[^/s]+', '', tweet)

    # Numbers removing
    pattern = '[0-9]'
    tweet = [re.sub(pattern, '', i) for i in tweet]
    tweet = s.join(tweet)

    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)

    # Remove All the QWERTY Symbols
    tweet = re.sub(r'(-|\'|\?|\/|\\|\`|\!|\`|\#|\$|\%|\^|\&|\*)', '', tweet)
    tweet = re.sub(r'(\*|\(|\)|\_|\+|\=|\.|\,|\<|\>|\{|\[|\}|\]|\"|\;|\:|\~)', '', tweet)

    # multiple whitespace removal
    tweet = " ".join(tweet.split())
    tweet = str(tweet.lower())

    return tweet