# created by shridevlopment
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # getting text

    djtext = request.POST.get('text', 'default')
    # checking on off condions of checkbox

    rfunc = request.POST.get('removepunc', 'off')
    upercase = request.POST.get('upercase', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    charCount = request.POST.get("charCount", 'off')
    # analyzed=djtext

    if rfunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        # Analyze text
        params = {'purpose': 'Removed punctuations', 'Analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # checking upper case
    if (upercase == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'UPPER CASE', 'Analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (newLineRemover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'New Line Removed', 'Analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if ( spaceRemover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Space Removed', 'Analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charCount == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)

        params = {'purpose': 'Char Counter', 'Analyzed_text': analyzed}

    if (rfunc != 'on' and upercase != 'on' and charCount != 'on' and newLineRemover != 'on' and spaceRemover != 'on'):
        return HttpResponse("Please Select Atleast one option and try again!!!")

    return render(request, 'analyze.html', params)
