from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, "count.html")

def result(request):
    # 나는 여기서 POST를 보내는 줄 알았는데 그게 아니라 request를 parameter로 받았잖아. 
    # request.POST['text'] -> request보낸 것 중에 POST라는 method로 request 보낸 것 중에 이름이 'text'인 것만 text라는 변수에 넣어줘
    text = request.POST['text']
    total_len = len(text)
    total_without = len(text.replace(' ', ''))
    total_words = len(text.split())
    return render(request, "result.html", {"total_len": total_len, "total_without": total_without, 'text': text, 'total_words': total_words})