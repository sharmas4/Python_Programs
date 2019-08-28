"""
Persistence using Pickle
“Pickling” is the process whereby a Python object hierarchy is converted into
a byte stream, and “unpickling” is the inverse operation.
Pickle is used for serializing and de-serializing Python object structure.
Serialization refers to the process of converting an object in memory to a
byte stream that can be stored on disk or sent over a network.

Pickling is not to be confused with compression! The former is the conversion
of an object from one representation (data in Random Access Memory (RAM)) to
another (text on disk), while the latter is the process of encoding data with
fewer bits, in order to save disk space.

It can also be used to send data over a Transmission Control Protocol (TCP)
or socket connection, or to store python objects in a database. Pickle is very
useful for when you're working with machine learning algorithms, where you want
to save them to be able to make new predictions at a later time, without having
to rewrite everything or train the model all over again.

If you want to use data across different programming languages, pickle is not
recommended. Its protocol is specific to Python, thus, cross-language
compatibility is not guaranteed.

Objects that can be pickled: boolean, int, float, complex numbers, string(normal
 and unicode), tuple, list, set, dict that contain picklable objects.
 Also, classes and functions if they are defined at top level of a module.
 Objects which cannot be pickled: generators, inner classes, lambda functions,
 defaultdicts

Pickle vs JSON:
JSON is more secure and faster than pickle. However, if you only need to use
Python, then the pickle module is still a good choice for its ease of use and
ability to reconstruct complete Python objects.

When a class's object is pickled to a file and class has been updated as:
    1. A new variable added to the class: The previously pickled object doesn't have the new variable. The old object
    will get unpickled without any error but if any instance function which uses the new variable is called, error will
    be there.
    2. One of the originally present variables is removed from the class: No error while unpcikling
"""
import pickle
import pprint
import io

print("Example 2")

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print("Data:", end=" ")
pprint.pprint(data)

pickledData = pickle.dumps(data)
print("Pickled data is: ", pickledData)

unpickledData = pickle.loads(pickledData)
print("data is unpickledData? ", (data is unpickledData))
print("data == unpickledData? ", (data == unpickledData))

## Dump binary pickled data in a file
pickleFile = open("TestPickle.pkl", "wb")

pickle.dump(data, pickleFile)

pickleFile = open("TestPickle.pkl", "rb")
unpickledData2 = pickle.load(pickleFile)
pickleFile.close()

print("Output fom pickle File: ", unpickledData2)
print("\n" + "*" * 75)
print("*" * 75)
print("*" * 75)
print("**************************** Example 2 ******************************")
"""
In addition to dumps() and loads(), pickle provides a couple of convenience
functions for working with file-like streams. It is possible to write multiple
objects to a stream, and then read them from the stream without knowing in
advance how many objects are written or how big they are.
"""


class SimpleObject():
    def __init__(self, name):
        self.name = name
        l = list(self.name)
        l.reverse()
        self.reversedName = "".join(l)
        return


data = []
data.append(SimpleObject("Pickle"))
data.append(SimpleObject("StringIO"))
data.append(SimpleObject("PPrint"))

# Simulate a file with StringIO
out_string = io.BytesIO()

# Write to the stream
for d in data:
    print("Writing: {0} ({1})".format(d.name, d.reversedName))
    pickle.dump(d, out_string)
    out_string.flush()

print("-------------------------------------------------")
# set up read stream
in_string = io.BytesIO(out_string.getvalue())

# read the data
while True:
    try:
        o = pickle.load(in_string)
    except:
        break
    else:
        print("READ: {0} ({1})".format(o.name, o.reversedName))
