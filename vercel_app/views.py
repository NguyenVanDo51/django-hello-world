from django.http import JsonResponse
from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi

from youtube.models import Writings


def index(request):
    video_id = request.GET.get('video_id')
    if (video_id == None):
        video_id = 'vq2x7k_nofw'

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    t = []
    for transcript in transcript_list:
        if transcript.language_code == 'en-GB' or transcript.language_code == 'en':
            t = transcript.fetch()
    try:
        writing = Writings.objects.get(video_id=video_id)
    except Exception:
        pass
    return render(request, 'index.html', {'transcripts': t, 'video_id': video_id, 'transcript_length': len(t), 'content': str(writing.content)})
