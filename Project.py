from mylexer import MyLexer

if __name__ == "__main__":
    ml = MyLexer()
    ml.build()
    ml.test(input("input: "))
