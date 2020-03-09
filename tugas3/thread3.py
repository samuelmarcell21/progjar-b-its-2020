import logging
import requests
import os
import threading

def download_gambar(url=None, nama_foto=None, thread=None):
    if (url is None and thread is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'
    content_type = ff.headers['Content-Type']
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        fp = open(f"{nama_foto}.{ekstensi}","wb")
        fp.write(ff.content)
        print(f'{nama_foto} berhasil didownload dengan thread {thread}')
        fp.close()
    else:
        return False

if __name__=='__main__':
    list_url_foto = []
    list_url_foto.append('https://images8.alphacoders.com/505/505616.png')
    list_url_foto.append('https://images7.alphacoders.com/607/607718.png')
    list_url_foto.append('https://images7.alphacoders.com/424/424443.jpg')
    list_url_foto.append('https://images5.alphacoders.com/607/607886.jpg')
    list_url_foto.append('https://images5.alphacoders.com/573/573801.jpg')
    for i in range(5):
        t = threading.Thread(target=download_gambar, args=(list_url_foto[i], f'Foto ke {i}', i,))
        t.start()