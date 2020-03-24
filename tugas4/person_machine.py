from handler import Person
import json
import logging

p = Person()

'''
    FORMAT DARI PROTOCOL
    
    Command nya adalah 2 string yang terpisah oleh spasi
    Format : command *spasi* parameter (untuk add ada tambahan *spasi* parameter2)
    FITUR YANG BISA DILAKUKAN :
    a. Meletakkan File
       Fitur ini digunakan untuk meletakkan file ke dalam folder "dropbox"
       Request : add
       Parameter : namafile *spasi* isi dari file 
       Response yang diberikan: Jika berhasil -> "File successfully added!"
                                Jika gagal -> "ERROR"
                                
    b. List File
       Fitur ini digunakan untuk melihat list file di dalam folder 'dropbox'
       Request : list
       Parameter: -
       Response: Jika berhasil -> "List of File accepted!"
       
    c. Mengambil File
       Fitur ini digunakan untuk mengambil file berdasarkan nama file dari folder 'dropbox'
       Request : get
       Parameter : namafile yang ingin diambil
       Response: jika berhasil -> "File has been received"
                 jika gagal -> "ERROR"
    d. Jika command tidak dikenali akan merespon dengan ERRCMD
    
'''

class PersonMachine:
    def proses(self,string_to_process):
        s = string_to_process
        commands = s.split(" ")
        # print(len(commands))
        try:
            command = commands[0].strip()
            # print(command)
            if (command=='add'):
                # print('masuk brow')
                logging.warning("add")
                namafile = commands[1].strip()
                # print(namafile)
                isifile = commands[2].strip()
                for i in range(3, len(commands)):
                    isifile = isifile + ' ' + commands[i].strip()
                # print(isifile)
                p.adding_file(namafile,isifile.encode())
                return "File successfully added!"
            elif (command=='list'):
                logging.warning("list")
                list_file = {}
                list_file['files'] = []
                hasil = p.list_file()
                for file in hasil:
                    list_file['files'].append({"namafile":file})
                return json.dumps(list_file, indent=2)
            elif (command=='get'):
                logging.warning("get")
                namafile = commands[1].strip()
                hasil = p.getting_file(namafile)
                return hasil
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = PersonMachine()