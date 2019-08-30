import requests      
  
def NewsFromApi(): 
      
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=352dd727fa584cb985827bcda6502875"
  
    open_bbc_page = requests.get(main_url).json() 
  
    article = open_bbc_page["articles"] 
  
  
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        print(i + 1, results[i])                  
  
if __name__ == '__main__': 
      
    NewsFromApi()  