import ast, json, urllib.request as ur
def ipynbinfo(info, file_name):
    def call(file_name):
        if 'http' == file_name[0:4]:
            print('\nPlease WAIT, content is loading from URL...\n')
            su = ur.urlopen(str(file_name)).read().decode('ascii')
        elif '{' == file_name[0]: su = file_name
        elif '\\' or '/' in file_name: su = open(file_name).read()
        try: y = json.loads(str(su))
        except: y = su
        return ast.literal_eval(str(y))
    def recdict(d):
        try: box.append(d[info])
        except Exception as e: e=e
        for i in list(d.values()):
            if type(i) == list:
                for j in i:
                    if type(j) == dict: recdict(j)
            if type(i) == dict: recdict(i)
        return box
    return recdict(call(file_name))
n, box, file_name = 130, [], input('Enter ipynb file Contents : ')
for i in ipynbinfo('source', file_name):
    for j in i: print(j)
    print('='*n, end='\n\n')