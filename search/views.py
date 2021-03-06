from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    URL = f"https://www.mygov.in/corona-data/covid19-statewise-status"
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
    # print(soup.prettify())
    links=[]
    for link in soup.find_all(class_="field-item even"):
        links.append(link.text)
    if 'Jammu and Kashmir' in links:
        x=links.index('Jammu and Kashmir')
        result=links[x:(x+4)]
    results={
        "Covid-19 Status " : "J&K",
        " Total " : result[1],
        " Recovered " : result[2],
        " Active":int(result[1])-int(result[2])-int(result[3]),
        " Deceased " : result[3]
    }
#     print(results)
    return render(request, 'index.htm',{'resul':results})

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
