from django.shortcuts import render

# Create your views here.

def translator_view(request): 
    
    if request.method == 'POST':
        orginal_text = request.POST['my_textarea']
        output = orginal_text.upper()
        return render(request, 'translator.html', {'output_text': output, 'orginal_text': orginal_text})
    else:
        return render(request, 'translator.html')