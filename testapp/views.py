from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
def movies_news_view(request):
    news1 = 'dangal movie is blockbuster movies on box office'
    news2 = 'Aamir khan earned thousand crores from this movies'
    news3 = 'it is based on true story about Geeta and Babita phogat'
    news4 = 'even this movie earned hundred crore in china'
    news5 = 'even i have been watched three times in theater'
    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    
    return render(request,'testapp/mnews.html',my_dict)
def sports_news_view(request):
    news1 = 'cricket is not only game in india , it is a religion in india'
    news2 = 'even i like most this game and dhoni was my favorite cricketer ever'
    news3 = 'in our country cricket is attached with our emotions'
    news4 = 'india won times icc world cup'
    news5 = 'and current time t20 and ipl also apart of this interesting game'
    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    
    return render(request,'testapp/mnews.html',my_dict)
def politics_news_view(request):
    news1 = 'upcoming election is coming in uttar pradesh'
    news2 = 'there are three major party in this election'
    news3 = 'Mr. yogi adityanath is the current chief minister of uttar pradesh'
    news4 = 'this time that eletion battle in between  yogi and akhilesh '
    news5 = 'but bypoll shows in up , 70% public support is with yogi ji'
    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    
    return render(request,'testapp/mnews.html',my_dict)


