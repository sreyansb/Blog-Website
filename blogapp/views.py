from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogapp.models import Post,BlogComment
from django.contrib import messages
from blogapp.templatetags import extras

def bloghome(request):
    allposts=Post.objects.all()

    return render(request,"blogapp/bloghome.html",{'allposts':allposts})
# Create your views here.

def blogpost(request,slug):
    obj=Post.objects.get(slug=slug)
    obj.views+=1
    obj.save()
    comments=BlogComment.objects.filter(post=obj,parent=None).order_by('-timestamp')#to get all the comments which are the main ones and not replies
    replies=BlogComment.objects.filter(post=obj).exclude(parent=None).order_by('-timestamp')# to get descending order even in replies
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict:
            replydict[reply.parent.sno]=[]
        replydict[reply.parent.sno].append(reply)
        
    return render(request,"blogapp/blogpost.html",{'obj':obj,"comments":comments,"replies":replydict})

def postcomment(request):

    if request.method=="POST":
        comment=request.POST['comment']
        user=request.user#very important
        post=request.POST['post']#will get us the id of the post
        post=Post.objects.get(sno=post)
        parent=request.POST['parentsno']
        if parent=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            messages.success(request,"Comment registered")
        else:
            parent=BlogComment.objects.get(sno=parent)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Reply registered")
        comment.save()
        
        return redirect(f"/blog/{post.slug}")
    else:
        return redirect("/blog")
