import collections
import re
def open_file():
    with open('table.xml', encoding = 'utf-8') as f:
        text = f.read()
    return text

def find_se(text):
    pattern = '(<se>\n)(.*?)(</se>)'
    result = re.search(pattern, text, flags = re.MULTILINE|re.DOTALL)
    return result.group(2)

def count_line(text):
    pattern = '\n'
    result = re.findall(pattern, text)
    num = len(result)
    return num

def write_result(k):
    with open('countline.txt','w',encoding = 'utf-8') as f:
        f.write(str(k))

def find_words(text):
    pattern = '<ana gr="([^"]*)(?:.*)'
    result = re.findall(pattern,text)
    return result

def create_dict(words):
    mydict = collections.Counter(words)
    # или так mydict=Counter(words)
    return mydict

def print_dict(dic):
    with open('dict.txt','w',encoding = 'utf-8') as f:
        for key,value in dic.most_common(None):
            line = key + ' | ' + str(value) + '\n'
            f.write(line)

def find_lex(text):
    pattern = '<ana gr="([^,]*).*lex="([^"]*)(?:.*)'
    result = re.findall(pattern,text)
    return result

def create_sdic(words):
    mydict = {}
    for pos, lex in words:
        if pos not in mydict:
            mydict[pos] = []
        mydict[pos].append(lex)
    return mydict

def print_sdict(dic):
    with open('dict.txt','w',encoding = 'utf-8') as f:
        for key,value in dic.items():
            f.write('\n'.join(value) + '\n')

def main():
    table = open_file()
    words = find_lex(table)
    mydic = create_sdic(words)
    print_sdict(mydic)
main()
    
