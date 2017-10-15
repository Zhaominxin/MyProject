import easygui as g
import re
import urllib.request
import json
import random


def url_open(url):#打开网页
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3103.400 ')
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def get_wordlist(html):
    global wordlist
    wordlist = re.findall(r'\b[a-z]{4,20}\b', html)
    wordlist =list(set(wordlist))
    print(wordlist)
    return wordlist

def get_word(wordlist):
    global word
    word = random.choice(wordlist)
    global worddict
    worddict = {i:word[i] for i in range(len(word))}
    vowel = ['a','e','i','o','u']
    global tipsdict
    tipsdict = {}
    for each in range(len(word)):
        if worddict[each] in vowel:
            tipsdict[each] = worddict[each]
    #print(tipsdict)
    return tipsdict


def check():
    get_answer()
    correct = {}
    correct = tipsdict
    while True:
        if guess == word:
            g.msgbox(msg='恭喜！回答正确！')
            break
        else:
            if len(guess) != len(word):
                g.msgbox('单词长度不等，请重新输入')
                get_answer()
            else:
                for each in range(len(word)):
                    if guessdict[each] == worddict[each]:
                        correct[each] = guessdict[each]
                        print(tipsdict)
            
                helping = g.buttonbox(msg='加油~继续猜~↖(^ω^)↗', title='猜单词游戏', choices=('继续', '显示中文翻译', '答案'))
                if helping == '显示中文翻译':
                    message = translate(word)
                    g.msgbox(msg=message)
                    get_answer()
                
                elif helping == '答案':
                        g.msgbox(msg=word)
                        get_answer()
                else:
                    get_answer()


                   
  
def get_answer():
    global tipstring
    tipstring =''
    for each in range(len(word)):
        if each in tipsdict:
            tipstring += tipsdict[each]
        else:
            tipstring += '_ '
    global guess
    guess = g.enterbox(msg=('提示：%s ' % tipstring), title='猜单词游戏')
    global guessdict
    guessdict = {i:guess[i] for i in range(len(guess))}
    return guessdict
    
    
def translate(word):
    
    trans_url = 'http://fanyi.sogou.com/reventondc/translate'

    data = {}
    data['from'] = 'auto'
    data['to'] = 'en'
    data['client'] = 'wap'
    data['text'] = word
    data['useDetect'] = 'on'
    data['useDetectResult'] = 'on'
    data['needQc'] = 1
    data['uuid'] = '33e0c587-d192-4138-bd6f-a16dff0939c4'

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(trans_url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    result = '中文解释：%s' % target['translate']['dit']
    return result



if __name__ == '__main__':
    #url = 'http://xue.youdao.com/sw/m/1416661?showmethod=native&_=1499825348551&callback=jsonp1'
    url = 'http://edition.cnn.com/'
    word_list = get_wordlist(url_open(url))
    while True:
        get_word(word_list)
        check()
