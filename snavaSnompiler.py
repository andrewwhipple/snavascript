import sys


snavaDict = {"snif": "if", "snelse": "else", "sninfinity": "Infinity", "SNaN": "NaN", "snull": "null", "sneval": "eval", "snuneval": "uneval", "snis": "is", "snarse": "parse", "snun": "un", "snecode": "decode", "snencode": "encode", "snescape": "escape", "Snobject": "Object", "Snunction": "Function", "Snoolean": "Boolean", "Snymbol": "Symbol", "Snerror": "Error", "Sneval": "Eval", "Sninternal": "Internal", "Snrange": "Range", "Snyntax": "Syntax", "Snype": "Type", "SNURI": "URI", "Snumber": "Number", "Snmath": "Math", "Snate": "Date", "Snring": "String", "SnregSnexp": "RegExp", "Snarray": "Array", "Snint": "Int", "Snmap": "Map", "Snet": "Set", "SNASON": "JSON", "Sniterator": "Iterator", "snarg": "arg", "snontinue": "continue", "snwitch": "switch", "snar": "var", "snunc": "func", "snreturn": "return", "snfor": "for", "sneach": "each", "snof": "of", "snwhile": "while", "snexport": "export", "snimport": "import", "snwith": "with", "snthis": "this", "snew": "new", "snuper": "super", "snelete": "delete", "snvoid": "void", "sninstanceof": "instanceof"}

if len(sys.argv) < 2:
    print "Please enter a file to snompile (snail compile)"
else:
    with open(sys.argv[1], "r") as snavaFile:
        javaFileName = sys.argv[1][:-3]
        javaFileName = javaFileName + "js"
        if len(sys.argv) == 3:
            javaFileName = sys.argv[2]
        
        with open(javaFileName, "w") as javaFile:
            for line in snavaFile:
                jsLine = line
                for key in snavaDict:
                    print key
                    jsLine = jsLine.replace(key, snavaDict[key])
                javaFile.write(jsLine)   
                    
                         