from django.shortcuts import render, get_object_or_404, render_to_response

def view_about(request):
    return render(request, 'about.html', {})

