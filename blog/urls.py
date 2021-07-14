from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.PostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.PostsDetailView.as_view(), name="selected-post"),
    path("about/",views.AboutView.as_view(),name='about'),

    path("policy/",views.PolicyView.as_view(),name="policy"),
    path("carrers/",views.CarrersView.as_view(),name="carrers"),
    path("comment/",views.CommentView.as_view()),
    path("read-later/",views.ReadLaterView.as_view(), name="read-later"),
    path("fav/",views.FavPostView.as_view(), name="fav-posts"),

    path("thank-you/",views.ThankYouView.as_view(),name="thank-you")

]