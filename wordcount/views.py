# Add templates folder directory that just already created in the setting.py templates array

# from django.http import HttpResponse
from django.shortcuts import render
import operator

# def home(request):
#     return HttpResponse('Hellow')

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # Add to dictionary
            worddictionary[word] = 1

        sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedWords':worddictionary.items})
