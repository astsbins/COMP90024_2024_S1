# %%
import pandas as pd
import json
import time
# TODO: Check for duplicate Ids
# TODO: decide on outliers, dicts ints -3
# TODO: MPI

# %%
def parse_json(json_string):
    json.loads(json_string)
    
def read_line(file, seek_head):
    # skip line if seek head starts in midde of a line
    # that is something that should have been picked up by previous readline
    if seek_head !=0:
        file.seek(seek_head-1)
        if file.read(1)!= '\n':
            file.readline() 
            
    # sprint(file.readline)
    new_line = file.readline().rstrip(",\n ")
    return(new_line)

def get_tweet_data(file_line):
    tweet_dict = json.loads(file_line)
    tweet_data = tweet_dict["doc"]["data"]
    return tweet_data
    
def get_tweet_date(tweet_data):
    tweet_hour =  tweet_data["created_at"][:-11]
    return tweet_hour

def get_tweet_sentiment(tweet_data):
    tweet_sentiment = None
    if "sentiment" in tweet_data.keys():
        tweet_sentiment = tweet_data["sentiment"]
        if isinstance(tweet_sentiment, dict):
            tweet_sentiment = tweet_sentiment['score']
    else:
        tweet_sentiment = 0
    
    return tweet_sentiment
    
def add_tweet_stats_to_dict(tweets_dict,tweet_data):
    tweet_date = get_tweet_date(tweet_data)
    tweet_sentiment = get_tweet_sentiment(tweet_data)
    if tweet_date in tweets_dict.keys():
        tweets_dict[tweet_date][0] += 1
        tweets_dict[tweet_date][1] += tweet_sentiment
    elif tweet_date not in tweets_dict.keys():   
        tweets_dict[tweet_date] = [1, tweet_sentiment]
    return()
# %%
def process_chunk(file_name, chunk_start, chunk_end):
    tweet_stats_dict = {}
    seek_head = chunk_start
    with open(file_name, encoding='utf-8') as tweet_file:
        while seek_head < chunk_end:
            full_tweet = read_line(tweet_file, seek_head)
            seek_head = tweet_file.tell()
            if full_tweet =='': # exhausted tweets
                break
            tweet_data = get_tweet_data(full_tweet)
            add_tweet_stats_to_dict(tweet_stats_dict,tweet_data)
    return tweet_stats_dict

def combine_tweet_dicts(all_tweets_data):
    all_tweets_data_dict = {}
    for tweet_dict in all_tweets_data:
        for key in tweet_dict.keys():
            if key not in all_tweets_data_dict.keys():
                all_tweets_data_dict[key] = tweet_dict[key]
            else:
                all_tweets_data_dict[key][0] += tweet_dict[key][0]
                all_tweets_data_dict[key][1] += tweet_dict[key][1]
    return all_tweets_data_dict

def create_day_tweet_dict(all_tweets_data_dict):
    day_tweet_dict = {}
    # print(all_tweets_data_dict.keys())
    for hour in all_tweets_data_dict.keys():
        day = hour[:-3]
        # print(hour, day)
        if day in day_tweet_dict.keys():
            day_tweet_dict[day][0] += all_tweets_data_dict[hour][0] 
            day_tweet_dict[day][1] += all_tweets_data_dict[hour][1]
        else:
            day_tweet_dict[day] = all_tweets_data_dict[hour]
    return day_tweet_dict
    


def get_stats(all_tweets_data_dict):
    most_active_hour = 0
    most_active_hour_tweets = 0
    highest_sentiment_hour = 0
    highest_sentiment_value = 0
    for date in all_tweets_data_dict.keys():
        if all_tweets_data_dict[date][0]>most_active_hour_tweets:
            most_active_hour = date
            most_active_hour_tweets = all_tweets_data_dict[date][0]
        if all_tweets_data_dict[date][1]>highest_sentiment_value:
            highest_sentiment_hour = date
            highest_sentiment_value = all_tweets_data_dict[date][1]
            
    return (most_active_hour,
            most_active_hour_tweets,
            highest_sentiment_hour,
            highest_sentiment_value)


def main():
    pass



if __name__ == "__main__":
    main() 
# %%

