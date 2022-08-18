import re
from django.shortcuts import render


def inputdata(request):
    return render(request, 'program/inputdata.html')

def result(request):
    lis=[]
    lis.append(request.GET['A'])
    lis.append(request.GET['B'])

    print(lis)

    sum = 0
    for l in lis:
        sum += int(l)
    ans = sum

    return render(request, 'program/result.html',{'ans':ans, 'lis':lis})

    #return render(request, 'program/result.html')
    
