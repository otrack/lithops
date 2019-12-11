import pywren_ibm_cloud as pywren
from creson.factory import Factory

def my_function(x):
    f = Factory("34.94.237.246:11222")
    c = f.createCounter("async")
    return c.increment(x)


if __name__ == '__main__':
    pw = pywren.ibm_cf_executor()
    pw.call_async(my_function, 3)
    print(pw.get_result())
