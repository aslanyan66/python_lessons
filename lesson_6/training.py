file_path = 'new_file.txt'
with open(file_path, 'w') as f:
    f.write('seeelelelrflela\n')
    f.writelines(['1', '2', '3', '4'])
    f.close()
    f = open(file_path,'r')
    print(f.read())
    f.close()
