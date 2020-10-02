from django.shortcuts import render,get_object_or_404
from .models import Posts,Comment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import PostForm,CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def post(request):
	context={
		'posts':Posts.objects.all()	
}
	return render(request,'blog/post.html',context)

def LikeView(request, pk):
	post= get_object_or_404(Posts, id=request.POST.get("likes"))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('blog-post-detail', args=[str(pk)]))


class PostListView(ListView):
	model = Posts
	template_name = 'blog/post.html'
	context_object_name = 'posts'
	ordering='-date_posted'

def PostDetail(request,pk):
	post=get_object_or_404(Posts,id=pk)
	comments=Comment.objects.filter(post=post)
	comment_form=CommentForm(request.POST or None)
	if request.method== 'POST':
		
		if comment_form.is_valid():
			content=request.POST.get('comments')
			comment=Comment.objects.create(post=post,user=request.user,comments=content)
			comment.save()
		else:
			comment_form=CommentForm()


	context={

			'posts':post,
			'comments':comments,
			'comment_form':comment_form,
			'user':request.user
	}
	return render(request,'blog/posts_detail.html',context)

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Posts                            
	
	form_class=PostForm
	

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Posts
	fields=['title','content','git_link']

	

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin,DeleteView):
	model = Posts
	success_url='/'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request,'blog/about.html')
