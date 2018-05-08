from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)
from blog.forms import PostForm,CommentForm
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy


# Create your views here.


class AboutView(TemplateView):
    template_name='about.html'


class PostListView(ListView):
            model=Post

            def get_queryset(self):
                return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='post_detail'
    form_class=PostForm

    model=Post


class  PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    template_name='post_draft_list.html'
    login_url='/login/'
    redirect_field_name='blog/post_draft_list.html'
    print('hello')
    form_class=PostForm
    model=Post

    def get_queryset(self):
        list= Post.objects.filter(published_date__isnull=True).order_by('-create_date')
        print (list)
        return list


#############comments model####################

@login_required
def add_comments_to_post(request,pk):
    # post=models.Post.objects.get(pk=pk)
    post=get_object_or_404(Post,pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            #post field in Comment model is set
            comment.post=post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return  render(request,'blog/comment_form.html',{'form':form})


@login_required
def comments_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()

    return redirect('blog:post_detail',pk=comment.post.pk)



@login_required
def comments_remove(request,pk):
    comments=get_object_or_404(Comment,pk=pk)

    post_pk=comments.post.pk
    comments.delete()
#post_pk because after deleting pk won't be available
    return redirect('blog:post_detail',pk=post_pk)



@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()

    #pk=pk since need id of post, back in comments we reffered this as comment.post.pk
    return redirect('blog:post_detail',pk=post.pk)
