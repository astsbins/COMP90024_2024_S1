import pandas as pd
import json
import time
# TODO: Check for duplicate Ids
# TODO: decide on outliers, dicts ints -3
# TODO: MPI

# %%
def read_json(file_name):
    file = open(file_name)
    parsed_json = json.load(file)
    return parsed_json

def read_chunk(filename, seekhead):
    file = open("test2.json")
    file.seek(0)
    print(file.readline)
    return(file.readline())

def main():
    pass



if __name__ == "__main__":
    main() 