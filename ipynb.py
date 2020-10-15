import ast
import json
import urllib.request as ur

def ipynbinfo(info, file_name):
    
    def call(file_name):
        if 'http' == file_name[0:4]:
            
            print('\nPlease WAIT, content is loading from URL...\n')
            su = ur.urlopen(str(file_name)).read().decode('ascii')
            
        elif '{' == file_name[0]:
            su = file_name
        elif '\\' or '/' in file_name:
            su = open(file_name).read()
            
        try:
            y = json.loads(str(su))
        except:
            y = su
        return ast.literal_eval(str(y))
    
    def recdict(d):
        try:
            box.append(d[info])
        except Exception as e:
            pass
        
        for i in list(d.values()):
            if type(i) == list:
                
                for j in i:
                    if type(j) == dict:
                        recdict(j)
                        
            if type(i) == dict:
                recdict(i)
                
        return box
    return recdict(call(file_name))

n, box = 130, []
file_name = input('Enter ipynb file Contents : ')

if file_name == '':
    file_name = 'https://raw.githubusercontent.com/imvickykumar999/vixtor/master/vixtor.ipynb'
    
extract = ['cell_type', 'execution_count', 'outputs', 'source']
for i in ipynbinfo(extract[3], file_name):
    
    for j in i:
        print(j)
    print('='*n, end='\n\n')
