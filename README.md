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

### function call :
        recdict(data)
        
### where, in recdict function parameter, data is any content of ipynb file... for example,

## data = [Click below Screenshot](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)

[![Sample ipynb file](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/screenshot.png?style=centerme)](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)
