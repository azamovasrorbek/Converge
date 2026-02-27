from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment

def home(request):
    # Fetch all comments to display on load
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'app/home.html', {'comments': comments})

def post_comment(request):
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            comment = Comment.objects.create(text=text)
            return JsonResponse({
                'status': 'success',
                'text': comment.text,
                'name': 'User', # You can extend this to logged in users
                'time': 'Just now'
            })
    return JsonResponse({'status': 'error'}, status=400)