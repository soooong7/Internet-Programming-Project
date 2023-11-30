from django.shortcuts import render

def notice(request):
    return render(
        request,
        'notice/index.html'
    )
