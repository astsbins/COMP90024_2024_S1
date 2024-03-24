from mpi4py import MPI
import os

#Initialize
mpi_comm = MPI.COMM_WORLD
rank = mpi_comm.Get_rank() # process id
size = mpi_comm.Get_size() # number of processes



file_size = os.path.getsize("test2.json")
chunk_size = file_size//size
seek_head = file_size - chunk_size*(rank+1)
f = open("test2.json", 'r', encoding="utf8")


f.seek(seek_head)
# print(f"I am process {rank+1} of {size}. I'm reading at {seek_head} of chunk_size {chunk_size} of file size {file_size}\n",f.readline(),"***")

print(f.readline())


f.close()


