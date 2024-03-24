# # %%
from mpi4py import MPI


# comm = MPI.COMM_WORLD   # commuincator object includes all process
# size = comm.Get_size()  # get number of processors in communicator
# rank = comm.Get_rank()  # 

# if rank == 0:
#     data = [(i+1)**2 for i in range(size)]
# else:
#     data = None
# data = comm.scatter(data, root=0)
# assert data == (rank+1)**2 
# print(data)
# %%
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Assuming a file with 'size' number of integers written in it
file_name = 'data.bin'
item_count = 1

# Create a file handle for reading
fh = MPI.File.Open(comm, file_name, MPI.MODE_RDONLY)

# Calculate the offset based on the rank of the process
# Assuming each integer is 4 bytes
offset = rank * item_count * 4
fh.Seek(offset)

# Prepare a buffer for reading the data
data = np.empty(item_count, dtype='i')

# Read data from the file
fh.Read(data)

print(f"Process {rank} read data: {data}")

# Close the file
fh.Close()