from django.http import JsonResponse
from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi

def transcript(request):
    video_id = request.GET.get('video_id')
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    t = []
    for transcript in transcript_list:
        if transcript.language_code == 'en-GB' or transcript.language_code == 'en':
            t = transcript.fetch()
    return JsonResponse(t, safe=False)

def index(request):
    video_id = request.GET.get('video_id')
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    t = []
    for transcript in transcript_list:
        if transcript.language_code == 'en-GB' or transcript.language_code == 'en':
            t = transcript.fetch()
    return render(request, 'index.html', {'transcripts': t, 'video_id': video_id, 'transcript_length': len(t)})