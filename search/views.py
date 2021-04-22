from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.htm')

def word(request):

    word = request.GET['word']
#     URL = f"https://hamariweb.com/dictionaries/urdu-english-dictionary.aspx?eu={word}&sk=true"
#     res = requests.get(URL)
   
    URL = f"https://urdu.wordinn.com/{word}" 
    res1 = requests.get(URL)
    meaning2 = []
    meaning5= []
    soup = bs4.BeautifulSoup(res1.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    for meaning in soup.find_all(class_ = "cell urdu"):
        meaning2.append(meaning.getText(""))
    for meaning3 in soup.find_all(class_="cell"):
        meaning5.append(meaning3.getText(""))
    
    results = {
            'word' : word,
        }
    dd={}
    for i in range(0,len(set((meaning2)))*2-2,2):
        dd[meaning5[i]]=meaning5[i+1]
    return render(request, 'word.htm', {'results': results , 'result':dd})
#     if res:
#         # soup = bs4.BeautifulSoup(res.text, 'lxml')
#         soup = bs4.BeautifulSoup(res.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#         meaning1 =[]
#         for meaning in soup.find_all(class_ = "UrduTextNafees urdufontgray14"):

#         # meaning = soup.find_all('div', {'value': '1'})
        
#             meaning1.append(meaning.getText(""))
#         meaning4 = []
#         for meaning3 in soup.find_all(class_="fontGray11 titlecase MontserratFont"):
    
#         # meaning = soup.find_all('div', {'value': '1'})
        
            meaning4.append(meaning3.getText(""))


    results = {
            'word' : word,
                    }
    di = {}
    if meaning1:
        for i in range(len(meaning1)):
            di[meaning4[i]] = meaning1[i]
        result=di
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        di={"":word}
    
    return render(request, 'word.htm', {'results': results, 'result':di})
def word1(request):
    word1 = request.GET['word1']
    URL = f"https://meaningin.com/urdu-to-english/{word1}-in-english" 
    res1 = requests.get(URL)
    meaning1= []
    if res1:
         # soup = bs4.BeautifulSoup(res.text, 'lxml')
        soup = bs4.BeautifulSoup(res1.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        for meaning in soup.find_all('p',class_="engtext"):
            meaning1.append(meaning.getText(""))
    
    else:
        print("No Result")
    if len(meaning1):
        xx=meaning1[0].split(" ")
      
    else:
        xx=[" " ,f"Sorry, {word1} Is Not Found In Our Database"]
    results1 = {
            'word1' : word1,
            'meaning':set(xx[1:])
                    }
    return render(request, 'word1.htm', {'results': results1})


    
def about(request):
    return render(request, 'about.htm')
