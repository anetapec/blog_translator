from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request): 
    
    if request.method == 'POST':
        orginal_text = request.POST['my_textarea']
        output = translate.translate(orginal_text)
        return render(request, 'translator.html', {'output_text': output, 'orginal_text': orginal_text})
    else:
        return render(request, 'translator.html')