from django.urls import path
from .views import news_list, news_detail,  ContactPageView, infoPage404
from .views import HomePageView, infoAboutPage, LocalNewsView, SportNewsView, TechnologyNewsView, ForeignNewsView
from .views import NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view, SearchResultsList

urlpatterns = [

    path('',  HomePageView.as_view(), name="home_page"),
    path('news/', news_list, name="all_news_list"),
    path('news/create/', NewsCreateView.as_view(), name="news_create"),
    path("news/<slug:news>/", news_detail, name="news_detail_page"),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('page-404', infoPage404, name='info_page'),
    path('about-us', infoAboutPage, name='about_page'),
    path('mahalliy/', LocalNewsView.as_view(), name='local_news_view'),
    path('texnologiya/', TechnologyNewsView.as_view(), name="technology_news_view"),
    path('xorijiy/', ForeignNewsView.as_view(), name='foreign_news_view'),
    path('sport/', SportNewsView.as_view(), name="sport_news_view"),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('search_result/', SearchResultsList.as_view(), name='search_results'),

]
