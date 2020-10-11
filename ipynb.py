import ast, json
import urllib.request as ur

def recdict(d):
    print('\n.................................................WELCOME......................................................\n')
    key = list(d.keys())
    lenkey = len(key)
    value = list(d.values())
    
    for i in value:
        typei = type(i)
        print(typei)
        print(i)
        print()
        
        if typei == list:
            for j in i:
                typej = type(j)
                if typej == dict:
                    recdict(j)
                    print('\n...................welcome back...................\n')
                    
        if typei == dict:
            recdict(i)
            print('\n...................welcome back...................\n')

    return key

def call():
    file_name = input('Enter : ')

    if 'http' == file_name[0:4]:
        print('\nPlease WAIT, content is loading from URL...\n')
        u = ur.urlopen(str(file_name)).read()
        su = u.decode('ascii')

    elif '{' == file_name[0]:
        su = file_name

    elif '\\' or '/' in file_name:
        su = open(file_name).read()

    try:
        y = json.loads(str(su))
    except:
        y = su

    data = ast.literal_eval(str(y))
    return data

while True:
    recdict(call())