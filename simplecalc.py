# %%
import pandas as pd
import json
import time
# TODO: Check for duplicate Ids
# TODO: decide on outliers, dicts ints -3
# %%
start_time = time.time()
df = pd.read_json("twitter-450mb.json", orient = "records")
read_time = time.time()
# # %%
# from tabulate import tabulate
# sentiment0 = df.rows[0]["doc"]["data"]["sentiment"]
# time0 = df.rows[0]["doc"]["data"]["created_at"][:-11]
# sentiment0
# time0
# # %%
# sentiments = []
# for i in range(len(df.rows)-1):
#     tweet_data = df.rows[i]["doc"]["data"]
#     if "sentiment" in tweet_data:
#         if type(tweet_data["sentiment"]) is  int:
#             # print(type(tweet_data["sentiment"])) 
#             # print (tabulate([tweet_data["sentiment"], tweet_data["text"]]))
#             sentiments.append([tweet_data["sentiment"], tweet_data["text"]])
            
# # %%
# sentiments.sort(reverse=True)

# print(tabulate(sentiments))        
# # %%
maxtweetshour = ''
maxhourtweets = 0
maxSentimenthour = ''
maxsumsentiment = 0

scores = []
time_sentimentDict = {}
for i in range(len(df.rows)-1):
    tweet_data = df.rows[i]["doc"]["data"]
    try:
        if "sentiment" in tweet_data:
            current_tweet_time = tweet_data["created_at"][:-11]
            current_tweet_sentiment = tweet_data["sentiment"]
            if type(current_tweet_sentiment) is dict:
                current_tweet_sentiment = current_tweet_sentiment["score"]
        else:
            continue
    except Exception as e:
        print("error", e)
        print(i,df.rows[i]["doc"]["data"])
        # print e
        break
    if current_tweet_time in time_sentimentDict:
        time_sentimentDict[current_tweet_time].append(current_tweet_sentiment)
    else:
        time_sentimentDict[current_tweet_time] = [current_tweet_sentiment]
        
    # scores.append([current_tweet_sentiment, tweet_data["text"]])
    
        
# %%
maxhour = ''
maxhourtweets = 0
maxSentiment = ''
maxsumsentiment = 0
for hour in time_sentimentDict:
    try:
        if len(time_sentimentDict[hour]) > maxhourtweets:
            maxhour = hour
            maxhourtweets = len(time_sentimentDict[hour])
        
        if sum(time_sentimentDict[hour]) > maxsumsentiment:
            maxSentiment = hour
            maxsumsentiment = sum(time_sentimentDict[hour])
            # print(maxsumsentiment)
    except Exception as e:
        print(e)
        print(time_sentimentDict[hour])
        print(len(time_sentimentDict[hour]))
        break
end_time = time.time()
print("max hour tweet", maxhour)
print("max hour sentiment", maxsumsentiment)
print("read in", read_time-start_time)
print("ran in", end_time-start_time)