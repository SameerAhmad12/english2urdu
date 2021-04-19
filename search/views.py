from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.htm')

def word(request):

    word = request.GET['word']
    URL = f"https://hamariweb.com/dictionaries/urdu-english-dictionary.aspx?eu={word}&sk=true"
    res = requests.get(URL)
   


    if res:
        # soup = bs4.BeautifulSoup(res.text, 'lxml')
        soup = bs4.BeautifulSoup(res.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        meaning1 =[]
        for meaning in soup.find_all(class_ = "UrduTextNafees urdufontgray14"):

        # meaning = soup.find_all('div', {'value': '1'})
        
            meaning1.append(meaning.getText(""))
        meaning4 = []
        for meaning3 in soup.find_all(class_="fontGray11 titlecase MontserratFont"):
    
        # meaning = soup.find_all('div', {'value': '1'})
        
            meaning4.append(meaning3.getText(""))
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning4 = ''
        meaning1=" "

    
    results = {
        'word' : word,
        }
    di = {}
    for i in range(len(meaning1)):
        di[meaning4[i]] = meaning1[i]
    return render(request, 'word.htm', {'results': results , 'result':di})
def about(request):
    return render(request, 'about.htm')