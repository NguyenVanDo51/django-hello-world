import json
from django.http import JsonResponse
from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi
from .models import Writings


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


def save_result(request):
    # Lấy nội dung của phần thân và chuyển đổi thành chuỗi
    body = request.body.decode('utf-8')
    # Chuyển đổi chuỗi JSON thành đối tượng Python
    data = json.loads(body)
    if request.method == 'POST':
        try:
            content = data['content']
            video_id = data['video_id']
            writing = Writings.objects.update_or_create(
                video_id=video_id, defaults={'content': content})
            return JsonResponse({'message': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid method'}, status=405)
