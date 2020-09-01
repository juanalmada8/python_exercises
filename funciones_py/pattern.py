from pattern.web import Twitter

def trending_topics():
        print (Twitter().trends(cached=False))

def busco_en_twitter(cadena):

        t = Twitter()
        i = None
        for j in range(3):
                for tweet in t.search(cadena, start=i, count=10):
                        print(tweet.text)
                        print("-------")
                        i = tweet.id

trending_topics()
busco_en_twitter("#UNLP")