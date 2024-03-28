from mpi4py import MPI
import os
import read_functions
import time
import cProfile

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

start_time = 0
if rank == 0:
    start_time = time.time()


file_name = "twitter-450mb.json"
file_size = os.path.getsize(file_name)
chunk_size = file_size//size

tweet_dict = read_functions.process_chunk(file_name, chunk_size*rank + 4, chunk_size*(rank+1)-6)
# print(f"Hi i am rank {rank} of {size} reading between {chunk_size*rank} and {chunk_size*(rank+1)} of {file_size}")

all_tweets = comm.gather(tweet_dict, root=0)
all_tweets_dict = {}
if rank == 0:
    all_tweets_dict = read_functions.combine_tweet_dicts(all_tweets)
    final_hour_stats = read_functions.get_stats(all_tweets_dict)
    day_tweets = read_functions.create_day_tweet_dict(all_tweets_dict)
    final_day_stats = read_functions.get_stats(day_tweets)
    end_time = time.time()
    print(all_tweets_dict)
    print(len(all_tweets_dict))
    print(final_hour_stats)
    print(final_day_stats)
    print(end_time-start_time)

