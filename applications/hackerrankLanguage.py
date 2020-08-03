if __name__ == '__main__':
    languages = ["C", "CPP", "JAVA", "PYTHON", "PERL", "PHP", "RUBY", "CSHARP", "HASKELL", "CLOJURE", "BASH", "SCALA",
                 "ERLANG", "CLISP", "LUA", "BRAINFUCK", "JAVASCRIPT", "GO", "D", "OCAML", "R", "PASCAL", "SBCL", "DART",
                 "GROOVY", "OBJECTIVEC"]

    for _ in range(int(input())):
        id, l = input().split()
        print("VALID") if languages.count(l) > 0 else print("INVALID")
