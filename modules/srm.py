import os
def srm(file):
    f = open(file, 'w')
    f.write(str(10029**7237))
    f.close()
    os.remove(file)
