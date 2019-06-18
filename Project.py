from myparser import MyParser

if __name__ == "__main__":
    parser = MyParser()
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)
