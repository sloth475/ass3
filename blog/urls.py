from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.PostsView.as_view(), name="all-posts"),
    path("posts/<slug:post_slug>", views.PostsDetailView.as_view(), name="selected-post"),
    path("about/",views.AboutView.as_view(),name='about'),
    # path("about/",views.about,name="about"),
    path("policy/",views.PolicyView.as_view(),name="policy"),
    path("carrers/",views.CarrersView.as_view(),name="carrers"),
    path("comment/",views.CommentView.as_view()),
    # path("comment/",views.showcomments),
    path("thank-you/",views.ThankYouView.as_view(),name="thank-you")

]