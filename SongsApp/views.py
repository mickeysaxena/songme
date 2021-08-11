from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Song

def index(request):
    return HttpResponse("Hello Abhinav !")

def song_by_id(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'songs.html',{'song': song})
    #return HttpResponse(("Song :{0}, Singer : {1}, Released on : {2}").format(song.song_title,song.singer,song.release_date))
    #return HttpResponse(Song Name :"{song.song_title}")
