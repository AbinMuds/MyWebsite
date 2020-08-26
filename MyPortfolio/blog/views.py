from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post,Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm,PostForm,ContactForm
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (ListView,DetailView,TemplateView,
                                  CreateView,DeleteView,UpdateView)

class Thankyoupage(TemplateView):
    template_name = 'blog/Thank.html'

class Thankcommentpage(TemplateView):
    template_name = 'blog/Thankcomment.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post
# get the objects and arrange in an order
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('date_of_creation')


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# Views for Contacts
def ContactInfo(request):
    registered = False

    if request.method == "POST":
        contactform = ContactForm(data=request.POST)

        if contactform.is_valid():
            contactform.save()

            registered = True
            return redirect('thanks')
        else:
            print(contactform.errors)
    else:
        contactform = ContactForm()

    return render(request,'blog/contact_form.html',{'contactform':contactform})

# comments in post and no login required here
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('thankcomment')

    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

# only for super user so login login_required
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
