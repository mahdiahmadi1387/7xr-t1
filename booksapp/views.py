from django.shortcuts import render,HttpResponse

from .models import Book,Topic,Ages,Author, Comment
from .form import  CommentForm


def name(request):
    books = Book.objects.order_by('number')
    return render(request,'booksapp/name.html',{'books':books})

def author(request):
    books = Book.objects.order_by('number')
    authors = []
    for book in books:
        if book.author not in authors:
            authors.append(book.author)
    return render(request,'booksapp/author.html',{'authors':authors})

def topic(request):
    books = Book.objects.order_by('number')
    topics = []
    for book in books:
        if book.topic not in topics:
            topics.append(book.topic)
    return render(request,'booksapp/topic.html',{'topics':topics})

def ages(request):
    books = Book.objects.order_by('number')
    agess = []
    for book in books:
        if book.ages not in agess:
            agess.append(book.ages)
    return render(request,'booksapp/ages.html',{'agess':agess})   


def home (request):
    books = Book.objects.order_by('number')
    return render(request,'booksapp/books.html',{'books':books})

def app_detail(request,slug_detail):
    # return HttpResponse(slug)
    book = Book.objects.get(number=slug_detail)
    comments = book.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        print("new comment detected")
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print("comment form is valid")
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = book
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()                   

    print(book)
    return render(request,'booksapp/detail.html',{'book':book,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})

def author_detail(request,slug_author):
    # return HttpResponse(slug_author)
    author = Author.objects.get(name=slug_author)
    books = Book.objects.all().filter(author=author)
    print(books)
    return render(request,'booksapp/author_detail.html',{'author':author,'books':books})

def topic_detail(request,slug_topic):
    # return HttpResponse(slug_topic)
    topic = Topic.objects.get(name=slug_topic)
    books = Book.objects.all().filter(topic=topic)
    print(books)
    return render(request,'booksapp/topic_detail.html',{'topic':topic,'books':books})


def ages_detail(request,slug_ages):

    # return HttpResponse(slug_ages)
    ages = Ages.objects.get(name=slug_ages)
    books = Book.objects.all().filter(ages=ages)
    print(books)
    return render(request,'booksapp/ages_detail.html',{'ages':ages,'books':books})

