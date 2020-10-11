# understanding-ipynb-file
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

## input data = [Click below Screenshot](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)

[![Sample ipynb file](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/screenshot.png)](https://raw.githubusercontent.com/imvickykumar999/understanding-ipynb-file/main/Sample%20ipynb%20file.ipynb)
