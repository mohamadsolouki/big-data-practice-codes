# load packages
import h5py
import numpy as np

# create an HDF5 file
file = h5py.File('iu.h5', 'w')

# create an empty dataset in the HDF5 file
dataset = file.create_dataset("iu", (4, 6))

# print information about the dataset
print("Dataset shape is", dataset.shape)
print("Dataset name is", dataset.name)
print("Dataset is a member of the group",
      dataset.parent)

# read/write HDF5 file
file = h5py.File('iu.h5', 'r+')

# list existing datasets in the file
list(file.keys())

# create an empty dataset in the HDF5 file
# if this dataset does not already exist
if "iu_numbers" not in list(file.keys()):
    dataset = file.create_dataset("iu_numbers", (4, 6))
else:
    dataset = file['/iu_numbers']

# generate sample data
data = np.random.rand(4 * 6).round(2).reshape(4, 6)

# add the data to the HDF5 dataset
dataset[...] = data

# read the data back from the HDF5 file
data_read = dataset[...]
print(data_read)


dataset.attrs["User"] = "ME"

for k in dataset.attrs.keys():
    print(k, dataset.attrs[k])

# close the file
file.close()
