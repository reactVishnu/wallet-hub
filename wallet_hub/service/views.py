from django.shortcuts import render, redirect

from .forms import TextDetailForm
"""
This view   ->  handles the uploaded file, 
                checks the type of file and size
                upload it to the server
"""


def basic_text_details(request):
    if request.method == 'POST':
        form = TextDetailForm(request.POST)
        if form.is_valid():
            text_detail = form.save(commit=False)
            text_detail.user = request.user
            text_detail.save()
            return redirect('operations:success')  # Redirect to the dashboard after saving the data
    else:
        form = TextDetailForm()
    return render(request, 'service/basic_details.html', {'form': form})
