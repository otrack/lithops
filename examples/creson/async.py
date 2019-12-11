import pywren_ibm_cloud as pywren
from creson.factory import Factory

def my_function(x):
    f = Factory()
    c = f.createCounter("async")
    return c.increment(x)


if __name__ == '__main__':
    pw = pywren.local_executor()
    pw.call_async(my_function, 3)
    print(pw.get_result())
