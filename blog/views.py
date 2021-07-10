from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, FormView

from blog.models import Post, Author, Tag, Comment
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CommentForm


# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Micheal",
#         "date": date(2020, 7, 21),
#         "title": "Mountain Hiking",
#         "summary": "There's nothing like the views on a mountain hiking.I was not event prepared for the same.",
#         "content": """
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#         """
#     },
#     {
#         "slug": "python-is-fun",
#         "image": "woods.jpg",
#         "author": "Batman",
#         "date": date(2020, 8, 20),
#         "title": "Python is fun",
#         "summary": "Python is much easier to, and perform development",
#         "content": """
#        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#        """
#     },
#     {
#         "slug": "travel",
#         "image": "travel.jpg",
#         "author": "Superman",
#         "date": date(2021, 3, 28),
#         "title": "Travel around the world",
#         "summary": "The article provides an insight on how should one travel",
#         "content": """
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#         """
#     },
#     {
#         "slug": "is-universe-expanding-too-much",
#         "image": "universe.jpg",
#         "author": "Mad Man",
#         "date": date(2021, 6, 30),
#         "title": "Is the universe expanding too much",
#         "summary": "We will take about the expansion of the universe how various solar system are moving away",
#         "content": """
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#         """
#     }
# ]


# def get_date(post):
#     return post['date']

# def starting_page(request):
#     # sorted_post = sorted(all_posts, key=get_date)
#     # latest_posts = sorted_post[-3:]
#     latest = Post.objects.all().order_by('-date') [:2]
#     # print("last",latest)
#     return render(request, "blog/index.html", {"posts": latest})


class StartingPageView(TemplateView):
    template_name = "blog/index.html"
    def get_context_data(self, **kwargs):
        latest = Post.objects.all().order_by('-date') [:2]
        context = super().get_context_data(**kwargs)
        context ["posts"] = latest
        return context



# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all_posts.html", {"posts": all_posts})
class PostsView(ListView):
    template_name = "blog/all_posts.html"
    model=Post
    context_object_name = "posts"




# def post_detail(request, post_slug):  # add ref to comment form here
#     selected_post = Post.objects.get(slug=post_slug)
#     post_tags = selected_post.tags.all()
#     # selected_post = next((post for post in all_posts if post['slug'] == post_slug), False)
#     # print("tags",post_tags)
#
#     if selected_post:
#         return render(request, "blog/post_detail.html", {"post": selected_post, "post_tags": post_tags})
#     else:
#         return HttpResponseNotFound("Post Not Found")
# class PostsDetailView(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"
#     context_object_name = "posts"
#     query_pk_and_slug = True
class PostsDetailView(DetailView):
    model=Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     selected_post=Post.objects.get(slug=slug)
    #     tags=selected_post.all()
    #     context=super().get_context_data(**kwargs)
    #     context["post_tags"]=tags
    #     return context




class CommentView(View):
    def get(self, request):
        form = CommentForm()
        return render(request, "blog/comment.html", {"form": form})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request,"blog/comment.html",{"form":form })


class AboutView(TemplateView):
    template_name = "blog/about.html"


class PolicyView(TemplateView):
    template_name = "blog/policy.html"


class CarrersView(TemplateView):
    template_name = "blog/carrers.html"


# def about(request):
#     return render(request, "blog/about.html")
# def policy(request):
#     return render(request, "blog/policy.html")
# def carrers(request):
#     return render(request, "blog/carrers.html")


# class CommentView(View):
#     def get(self, request):
#         form = CommentForm()
#         return render(request, "blog/comment.html", {"form": form})
#
#     def post(self, request):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request,"blog/comment.html",{"form":form })


class ThankYouView(TemplateView):
    template_name = "blog/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["message"] = "You feedback is saved!!!!"
        return context

# class CommentView(FormView):#form view will do get and post
#     template_name = "blog/comment.html"
#     form_class = CommentForm
#     success_url = "/thank-you"
#     def form_valid(self,form):
#
#         form.save()
#         return super().form_valid(form)

#

#
# def showcomments(request):
#     form=CommentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context={'form':form}
#     return render(request,'blog/comment.html',context)

