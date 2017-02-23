from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

import requests

from .models import Bookmark
from .forms import  BookmarkForm

def index(request):
    """Simply render index page"""
    return render(request,'bkm_app/index.html')

def bookmarks(request):
    """Show all of an user's bookmark"""
    bookmarks = Bookmark.objects.order_by('date_created')
    context = {'bookmarks': bookmarks}
    return render(request,'bkm_app/bookmarks.html', context)

def bookmark(request,bookmark_id):
    """Show details on some bookmark"""
    bookmark = bookmark.objects.get(id=bookmark_id)
    context = {'bookmark': bookmark}
    return render(request, 'bkm_app/bookmark.html', context)
    
def new_bookmark(request):
    """Defines a new entry"""
    #if it ain't POST we safely return a blank form
    if request.method != 'POST':
       form = BookmarkForm()
    #We got an POST
    else:
       form = BookmarkForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('bkm_app:bookmarks'))
    context = {'form': form}
    return render(request,'bkm_app/new_bookmark.html', context)

def edit_bookmark(request, bookmark_id):
    """Let an user edit he's bookmarks"""
    bookmark = Bookmark.objects.get(id=bookmark_id)
    if request.method != 'POST':
        #Fill up previwously the acctual value
        form = BookmarkForm(instance=bookmark)
    else:
        #POST on the run
        form = BookmarkForm(instance=bookmark, data=request.POST)
        if form.is_valid():
            form.save
            return HttpResponseRedirect(reverse('bkm_app:bookmark',args=[bookmark_id]))
    context = {'bookmark': bookmark, 'form': form}
    return render(request,'bkm_app/edit_bookmark.html',context)


        