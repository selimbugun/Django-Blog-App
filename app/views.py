from django.shortcuts import get_object_or_404, redirect, render
from app.forms import CommentForm, ContactForm
from app.models import Category, Comment, Contact, Post, Projects
from django.contrib import messages

# Create your views here.

def index(request):
    projects = Projects.objects.all()

    return render(request, 'app/index.html', {'projects': projects})

def blog(request):
    posts = Post.objects.filter(is_active = True)
    categories = Category.objects.all()
    messages_list = messages.get_messages(request)

    return render(request, 'app/blog.html', {
        'posts': posts,
        'categories': categories,
        'messages': messages_list
        })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message']
            )
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Mesajınız Başarıyla Gönderildi!')
            return redirect('blog')
        
    else:
        form = ContactForm()
    
    return render(request, 'app/contact.html', {'form': form})

        


def about(request):
    return render(request, 'app/about.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    
    else:
        comment_form = CommentForm()


    return render(request, 'app/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

    
def posts_by_category(request, category_slug = None):
    categories = Category.objects.all()
    posts = Post.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        posts = posts.filter(categories__in=[category])
        context = {'categories': categories, 'posts': posts, 'chosen_category': category_slug}
        return render(request, 'app/post_list_by_category.html', context)


def search(request):
    if "q" in request.GET and request.GET['q'] != '':
        q = request.GET['q']
        posts = Post.objects.filter(is_active = True, title__icontains = q ).order_by('publish_date')
        categories = Category.objects.all()
    else:
        return redirect('/blog')
    
    return render(request, 'app/search.html', {
        'posts': posts,
        'categories': categories
    })


def project_detail(request, slug):
    project = get_object_or_404(Projects, slug=slug)
    return render(request, 'app/project_detail.html', {
        'project': project
    })