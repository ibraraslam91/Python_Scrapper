d = {'as':1,'aa':5}



def demo():
    try:
        s = d['as']
    except:
        s = 0
    try:
        v = d['a']
    except:
        v = 0
    if (s > v):
        print('s')
    else:
        print('v')

demo()