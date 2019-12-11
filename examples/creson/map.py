import pywren_ibm_cloud as pywren
from creson.factory import Factory

def my_map_function(id, x):
    f = Factory("34.94.237.246:11222")
    c = f.createCounter("cnt")
    print("I'm activation number {}".format(id))
    return c.increment(x)


if __name__ == "__main__":
    iterdata = [1, 2, 3, 4]
    pw = pywren.ibm_cf_executor()
    pw.map(my_map_function, iterdata)
    print(pw.get_result())
    pw.clean()
