from django.http import JsonResponse
from .models import Issue
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_issue(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        issue = Issue.objects.create(title=title, description=description)
        return JsonResponse({'message': 'Issue created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

@csrf_exempt
def list_issues(request):
    issues = Issue.objects.all()
    data = [{'title': issue.title, 'description': issue.description} for issue in issues]
    return JsonResponse(data, safe=False)
