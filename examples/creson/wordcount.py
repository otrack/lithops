import pywren_ibm_cloud as pywren
from jpype import *
from jpype import java
from creson.factory import Factory

# Dataset from: https://archive.ics.uci.edu/ml/datasets/bag+of+words
iterdata = ['https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.enron.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.kos.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nips.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nytimes.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.pubmed.txt']


def my_map_function(url):
    print('I am processing the object from {}'.format(url.path))

    f = Factory()
    results = f.createMap("results")
    counter = java.util.HashMap()

    data = url.data_stream.read()
    for line in data.splitlines():
        for word in line.decode('utf-8').split():
                counter[word] = 1

    results.mergeAll(counter,f.Package.Sum())
    return 1

if __name__ == "__main__":
    pw = pywren.local_executor()
    pw.map(my_map_function, iterdata)
    result = pw.get_result()

    f = Factory()
    results = f.createMap("results")
    print(results.size())
