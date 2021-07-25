from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, FormView
from rest_framework.generics import get_object_or_404

from blog.models import Post, Author, Tag, Comment
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CommentForm, UploadForm
from django.urls import reverse
from .models import Post



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






class PostsDetailView(View):

    def is_read_later(self, request, post_id):
        stored_post_ids = request.session.get("stored_posts")
        if stored_post_ids is not None:
            return post_id in stored_post_ids
        return False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm()
        print(self.is_read_later(request, post.id))
        return render(request, "blog/post_detail.html",
                      {"post": post, "post_tags": post.tags.all(), "comments": post.comments.all().order_by("-id"), "comment_form": comment_form,
                          "is_read_for_later": self.is_read_later(request, post.id)})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.post = post
            comment_form.save()
            url = reverse("selected-post", args=[slug, ])
            return HttpResponseRedirect(url)
        return render(request, "blog/post_detail.html",
                      {"post": post, "post_tags": post.tags.all(), "comments": post.comments.all().order_by("-id"), "comment_form": comment_form,
                          "is_read_for_later": self.is_read_later(request, post.id)})


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


class ReadLaterView(View):
    def get(self, request):
        stored_posts_ids = request.session.get("stored_posts")
        context = {}
        if stored_posts_ids is not None:
            posts = Post.objects.filter(id__in=stored_posts_ids)
            context ["posts"] = posts
            context ["has_posts"] = True
        else:
            context ["has_posts"] = False
        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        read_later_id = request.POST ["read_later_id"]
        post_id = int(read_later_id)
        stored_posts_ids = request.session.get("stored_posts")
        if stored_posts_ids is None or len(stored_posts_ids)==0:
            stored_posts_ids = [post_id, ]
        else:
            if post_id not in stored_posts_ids:
                stored_posts_ids.append(post_id)
            else:
                stored_posts_ids.remove(post_id)
        request.session ["stored_posts"] = stored_posts_ids
        return HttpResponseRedirect("/")


class FavPostView(View):
    def get(self, request):
        fav_posts_ids = request.session.get("fav_posts")
        context = {}
        if fav_posts_ids is not None:
            posts = Post.objects.filter(id__in=fav_posts_ids)
            context ["posts"] = posts
            context ["has_posts"] = True
        else:
            context ["has_posts"] = False
        return render(request, "blog/fav_posts.html", context)

    def post(self, request):
        fav_posts_id = request.POST ["fav_posts_id"]
        post_id = int(fav_posts_id)
        fav_posts_ids = request.session.get("fav_posts")
        if fav_posts_ids is None or len(fav_posts_ids)==0:
            fav_posts_ids = [post_id, ]
        else:
            if post_id not in fav_posts_ids:
                fav_posts_ids.append(post_id)
            else:
                fav_posts_ids.remove(post_id)
        request.session ["fav_posts"] = fav_posts_ids
        return HttpResponseRedirect("/")

#
#
def create_view(request):
    context={}
    form=UploadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/thank-you")
    context['form']=form
    return render(request,"blog/create_view.html",context)




def update_view(request,id):
    context={}
    obj=get_object_or_404(Post,id=id)
    form=UploadForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context ["form"] = form

    return render(request, "blog/update_view.html", context)