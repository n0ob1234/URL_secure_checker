# Python program to demonstrate
# selenium


from selenium import webdriver

safe_list = ["youtube.com"	       ,
"en.wikipedia.org","twitter.com","instagram.com","amazon.com","pinterest.com","imdb.com",
"es.wikipedia.org",
"facebook.com",
"fandom.com",
"apple.com",
"ja.wikipedia.org",
"de.wikipedia.org",
"live.com",
"cricbuzz.com",
"fr.wikipedia.org",
"linkedin.com",
"globo.com",
"microsoft.com",
"nytimes.com",
"etsy.com",
"it.wikipedia.org",
"mayoclinic.org",
"healthline.com",
"indiatimes.com",
"amazon.in",
"amazon.de",
"bbc.co.uk",
"ikea.com",
"amazon.co.jp",
"amazon.co.uk",
"indeed.com",
"flipkart.com",
"bbc.com",
"espn.com",
"mail.yahoo.com",
"ebay.com",
"hurriyet.com.tr",
"allegro.pl",
"booking.com",
"mercadolivre.com.br",
"britannica.com",
"google.com",
"kompas.com",
"nih.gov",
"cnn.com",
"merriam-webster.com",
"homedepot.com",
"amazon.fr",
"ar.wikipedia.org",
"detik.com",
"nike.com",
"medlineplus.gov",
"id.wikipedia.org",
"brainly.co.id",
"milliyet.com.tr",
"accuweather.com",
"magazineluiza.com.br",
"marca.com",
"medicalnewstoday.com",
"cdc.gov",
"hepsiburada.com",
"cambridge.org",
"cookpad.com",
"m.wikipedia.org",
"dailymail.co.uk",
"as.com",
"ilovepdf.com",
"gsmarena.com",
"byjus.com",
"amazon.it",
"adobe.com",
"investing.com",
"epfindia.gov.in",
"clevelandclinic.org",
"aliexpress.com",
"espncricinfo.com",
"india.com",
"ndtv.com",
"canva.com",
"amazon.es",
"craigslist.org",
"finance.yahoo.com",
"dailymotion.com",
"indiamart.com",
"kinopoisk.ru",
"nl.wikipedia.org",
"onet.pl",
"omegle.com",
"goal.com",
"americanas.com.br",
"investopedia.com",
"dictionary.com",
"mail.ru",
"ebay.co.uk",
"naver.com",
"hm.com",
"hotstar.com",
"bestbuy.com",
"collinsdictionary.com"]


untrusted_TDL =[
    ".rest",
    ".okinawa",
    ".live",
    ".beauty",
    ".bar",
    ".fit",
    ".gp",
    ".haus",
    ".zone",
    ".top"
]


def check_safe_list(ogurl):
    url = ogurl
    begin = ""
    for i in range(len(url)):
        if url[i] == ":":
            i = i + 2
            break
        begin = begin + url[i]
    if begin == "https":
        print("The website is SSL certified according to the ( https ) in the url.")
    else:
        print("The url is not SSL verified according to the ( http ) in the url.")
    url = url[len(begin)+3:]

    # get rid of the www
    try:
        www_index = url.index("www")
    except:
        www_index =-1

    if www_index != -1:
        url = url.removeprefix("www.")

    #get rid of the end
    last_dot = 0

    for i in range(len(url[:63])):
        if url[i] == ".":
            last_dot = i

    #get tdl length
    index = 0
    TDL = ""

    while url[index+last_dot] != "/":
        TDL = TDL + url[index+last_dot]
        index = index +1



    url = url[:last_dot+index]

    #check TDL safeness
    nogo =0
    for i in range(len(untrusted_TDL)):
        if untrusted_TDL[i] == TDL:
            nogo = 1
            print("this top domain level ( " +str(TDL)+" ) has been found on the danger list. It would be smart not to go to this website")
    if nogo ==0:
        if TDL == ".gov" or TDL == ".edu":
            print("This top domain level ( " +str(TDL) + " ) is considered safe, you can freely naviagte to the page \""+ogurl+"\"")

        else:
             print("The Top level domain ( " + str(TDL)+" ) is not found either the safe or unsafe list.")


    most_similar = [0, "nada"]
    numSame=0
    for i in range(len(safe_list)):
        for m in range (len(safe_list[i])):


            new_url = safe_list[i]
            try:
                if new_url[m] == url[m]:
                    numSame = numSame+1
            except:
                break

        if numSame > most_similar[0]:
            most_similar[0] = numSame
            most_similar[1] = safe_list[i]
        numSame = 0
    # part two

    if most_similar[0] == len(url):
        print("Your url is on the safeList, so it should be safe for you.")
    else:
        if most_similar[0]<len(url)/2:
            print("The url given ( "+ogurl+" ) was not similar and/or not the same as any of the urls on the safelist.")
        else:
            print("The url you put in is most similar to " + most_similar[1]+",which is a popular website, but it is not the same as "+ url +",so this might be a spoofing attempt. Be weary.")



    #get beginning

    return most_similar[0]
url = input("What is the website that you want to see is safe?")
maybe_safe= check_safe_list(url)

