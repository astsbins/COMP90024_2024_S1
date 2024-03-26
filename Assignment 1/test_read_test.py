from read_functions import *
import pytest

# def test_read_file():
#     file = read_json("test.json")
#     assert file == {"test": "this is a test"}
import os
  
def test_read_line0():
    file_name = "test.json"
    file = open(file_name)
    seek_head = 0
    assert read_line(file, seek_head) == '{"test": "this is a test"}'

    
def test_read_line0_seek_head_past_0():
    file_name = "test.json"
    file = open(file_name)
    seek_head = 3
    assert read_line(file, seek_head) == '{"test2": "2this is a test2"}'
    
def test_read_line0_edge_case_line_end():
    file_name = "test.json"
    file = open(file_name)
    seek_head = 26
    assert read_line(file, seek_head) == '{"test2": "2this is a test2"}'
    
def test_get_tweet_data():
    file_name = "test_tweet.txt"
    file = open(file_name, encoding='utf8')
    file_line = read_line(file, 0)
    tweet_data = get_tweet_data(file_line)
    assert tweet_data == {"author_id":"709718136","conversation_id":"1405861219370782721","created_at":"2021-06-21T10:35:40.000Z","entities":{"mentions":[{"start":0,"end":10,"username":"rociomag3"},{"start":11,"end":27,"username":"socorro49046006"}]},"geo":{},"lang":"und","public_metrics":{"retweet_count":0,"reply_count":0,"like_count":0,"quote_count":0},"text":"@rociomag3 @socorro49046006 👏🏼👏🏼👏🏼👏🏼👏🏼😘","sentiment":{"score":0.24,"comparative":0,"calculation":[],"tokens":["@rociomag3","@socorro49046006","👏🏼👏🏼👏🏼👏🏼👏🏼😘"],"words":[],"positive":[],"negative":[]}}

def test_get_tweet_date():
    file_name = "test3.txt"
    file = open(file_name, encoding='utf8')
    tweet = get_tweet_data(read_line(file, 0))
    tweet_date = get_tweet_date(tweet)
    assert tweet_date == '2021-06-21T03'

def test_get_tweet_sentiment_number():
    file_name = "test3.txt"
    file = open(file_name, encoding='utf8')
    tweet = get_tweet_data(read_line(file, 0))
    tweet_sentiment = get_tweet_sentiment(tweet)
    assert tweet_sentiment == 0.7142857142857143

def test_get_tweet_sentiment_object():
    file_name = "test_tweet.txt"
    file = open(file_name, encoding='utf8')
    tweet = get_tweet_data(read_line(file, 0))
    tweet_sentiment = get_tweet_sentiment(tweet)
    assert tweet_sentiment == 0.24

def test_get_tweet_sentiment_none():
    file_name = "test_tweet_no_sentiment.json"
    file = open(file_name, encoding='utf8')
    tweet = get_tweet_data(read_line(file, 0))
    tweet_sentiment = get_tweet_sentiment(tweet)
    assert tweet_sentiment == 0

def test_add_tweet_sentiment_to_dict():
    file_name = "test_tweet.txt"
    file = open(file_name, encoding='utf8')
    tweet = get_tweet_data(read_line(file, 0))
    tweets_dict = {}
    add_tweet_stats_to_dict(tweets_dict,tweet)
    assert tweets_dict == {'2021-06-21T10':[1,0.24]}
    
def test_process_chunk_whole_file():
    file_name = "test_tweet.txt"
    tweets_dict = process_chunk(file_name, 0, os.path.getsize(file_name)-2)
    assert tweets_dict == {"2021-06-21T10" : [2,0.32], "2021-06-21T23" : [3,-0.44]}
        
def test_process_chunk_part_file():
    file_name = "test_tweet.txt"
    tweets_dict = process_chunk(file_name, 1, os.path.getsize(file_name)-2)
    assert tweets_dict == {"2021-06-21T10" : [1,0.08], "2021-06-21T23" : [3,-0.44]}
                
    
    
    
    
        
