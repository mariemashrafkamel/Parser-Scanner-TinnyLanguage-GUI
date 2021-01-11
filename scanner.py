

def scanner_file():
    file = open('Sample_code.txt')


    Reserved_Words = {'if': 'IF',
                      'then': 'THEN',
                      'else': 'ELSE',
                      'end': 'END',
                      'repeat': 'REPEAT',
                      'until': 'UNTIL',
                      'read': 'READ',
                      'write': 'WRITE'}
    Reserved_Words_key = Reserved_Words.keys()

    Special_Symbols = {
        '+': 'PLUS',
        '-': 'MINUS',
        '*': 'MUL',
        '/': 'DIVISION',
        ':=': 'ASSIGNMENT',
        '<': 'LESS',
        '>': 'GREATER',
        '<=': 'LESS|EQUAL',
        '>=': 'GREATER|EQUAL',
        ';': 'SEMICOLON',
        '(': 'OPEN_PARENTHESIS',
        ')': 'CLOSE_PARENTHESIS',
        '=': 'EQUALS',
        ':': 'COLON'}
    Special_Symbols_key = Special_Symbols.keys()

    TokensType = []
    TokensVal = []
    temp = ""
    Number = 0
    Identifier = ""
    Tokens = []

    dataFlag = False
    a = file.read()
    program = a.split("\n")

    for line in program:
        Tokens = line.split(' ')
        temp = "continue"
        i = -1
        for Token in Tokens:
            i = i + 1
            if Token == "{" or temp == "{":
                temp = "{"
                if Token == "}":
                    temp = "continue"
                    continue
            if temp == "continue":
                if Token in Special_Symbols_key:
                    TokensVal.append(Tokens[i])
                    TokensType.append(Special_Symbols.get(Tokens[i]))
                elif Token in Reserved_Words_key:
                    TokensVal.append(Tokens[i])
                    TokensType.append(Reserved_Words.get(Tokens[i]))
                else:
                    tempToken = Tokens[i]
                    if len(tempToken) > 0 and tempToken[0].isalpha():  # if first char is a letter
                        Identifier = Tokens[i]
                        TokensVal.append(Identifier)
                        TokensType.append("IDENTIFIER")
                    elif len(tempToken) > 0 and not (tempToken[0].isalpha()):
                        Number = Tokens[i]
                        TokensVal.append(Number)
                        TokensType.append("NUMBER")

    # write in another txt file "TokensTable.txt"
    fw = open('TokensTable.txt', "w")
    n = len(TokensVal)
    i = 0
    while i < n:
        fw.write(TokensVal[i] + ' , ' + TokensType[i] + '\n')
        i += 1
    fw.close()

    dataFlag = False
