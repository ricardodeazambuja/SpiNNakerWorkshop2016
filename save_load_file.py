"""

Makes life easier when it is necessary to save (pickle) something to a file in binary format.

"""

import cPickle as pickle
# import pickle
import dill
import gzip


def save_to_file(my_object, file_name):
    with open(file_name, 'wb') as f:
        # print "Saving..." + file_name
        pickle.dump(my_object, f)
        # print "Saving...Done!"

def load_from_file(file_name):
    with open(file_name, 'rb') as f:
        # print "Loading..." + file_name
        my_object = pickle.load(f)
        # print "Loading...Done!"
    return my_object


def save_to_file_gz(my_object, file_name):
    with gzip.open(file_name, 'wb') as f:
        # print "Saving..." + file_name
        pickle.dump(my_object, f)
        # print "Saving...Done!"


def load_from_file_gz(file_name):
    with gzip.open(file_name, 'rb') as f:
        # print "Loading..." + file_name
        my_object = pickle.load(f)
        # print "Loading...Done!"
    return my_object        