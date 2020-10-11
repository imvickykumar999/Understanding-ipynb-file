# [Understanding-ipynb-file](https://github.com/imvickykumar999/Understanding-ipynb-file/blob/main/ipynb%20to%20dictionary.ipynb)

### Recursive dictionary function is used.
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

### ...this is for Automating task !!!
    def call():
        file_name = input('Enter : ')

        if 'http' == file_name[0:4]:
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

### function call :
        recdict(call())
        
### where, in recdict function parameter, data is any content of ipynb file... for example,

## data = [Click below Screenshot](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)

[![Sample ipynb file](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/screenshot.png?style=centerme)](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)
