from sys import argv

class Language():
    def __init__(self, attr):
        self.syntax = attr[0]
        
class Compiler():
    def __init__(self):
        self.raw: str = self.get_raw()
        self.tokens: list[str] = self.tokenize()
        
        self.compiled = self.compile_tokens()
        self.exec_compiled()
        
    def get_raw(self):
        with open(f'{argv[1]}') as file:
            lines = file.readlines()[4::]
            raw = []
            
            for line in lines:
                raw.append(line.strip('\n'))
                
            return raw
        
    def tokenize(self):
        tokens = ''
        line_cache = ''
        stringing = False
        pos = 0
        
        for line in self.raw:
            stringing = False
            
            if line[0:2] == '""' and line[2] == '"':
                continue
                
            while pos <= len(line):
                match = False
            
                if len(line) == pos:
                    break
                
                if stringing:
                    line_cache += line[pos]
                    pos += 1
                    continue
                
                if line[pos] == '"':
                    line_cache += line[pos]
                    pos += 1
                    stringing = not stringing
                    continue
                
                for key in language.syntax:
                    value = language.syntax[key]
                    
                    if line[pos: pos+len(value)] == value:
                        line_cache += key
                        match = True
                        pos += len(value)
                        
                        break
                
                if not match:
                    line_cache += line[pos]
                    pos += 1
                    continue
                
            if line_cache != '':
                tokens += line_cache + '\n'
                
            line_cache = ''
            pos = 0
            
        return tokens
    
    def compile_tokens(self):
        return compile(self.tokens, "n/a", "exec")
    
    def exec_compiled(self):
        exec(self.compiled)
        
if __name__ == '__main__':
    with open("syntax.txt", "r") as raw_syntax:
        syntax = eval(raw_syntax.read())
        language = Language([
            syntax
            ])
    
    compiler = Compiler()
