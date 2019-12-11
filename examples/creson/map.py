import pywren_ibm_cloud as pywren
from creson.factory import Factory

def my_map_function(id, x):
    f = Factory()
    c = f.createCounter("map")
    print("I'm activation number {}".format(id))
    return c.increment(x)


if __name__ == "__main__":
    iterdata = [1, 2, 3, 4]
    pw = pywren.local_executor()
    pw.map(my_map_function, iterdata)
    print(pw.get_result())
    pw.clean()
