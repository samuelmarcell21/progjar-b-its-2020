import os

class Person:

    def __init__(self):
        if os.path.exists('dropbox') == False:
            os.makedirs('dropbox')

    def adding_file(self,namafile=None,isifile=None):
        f = open('dropbox/' + namafile, 'wb')
        f.write(isifile)
        return True

    def getting_file(self,namafile=None):
        f = open('dropbox/' + namafile, 'rb')
        hasil = f.read()
        f.close()
        # print(hasil)
        hasil = str(hasil, "utf-8")
        return hasil

    def list_file(self):
        hasil = os.listdir('dropbox')
        return hasil

if __name__=='__main__':
    p = Person()