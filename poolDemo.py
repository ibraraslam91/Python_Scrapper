from multiprocessing import Pool
demo = []
demo2= []

def f(x):
    # complicated processing
    demo.append(x)
    demo2.append(x+1)

pool = Pool(10)

y_serial = []
x = range(100)
pool.map(f, x)
print(demo)



