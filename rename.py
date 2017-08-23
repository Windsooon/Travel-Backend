import os

path = '/Users/anchuang/learn/Travel-Backend/static/imgs/'
[os.rename((path+f), (path+f).split('/')[-1][4:])
    for f in os.listdir(path) if f.endswith('.png')]
