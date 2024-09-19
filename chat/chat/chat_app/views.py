from django.shortcuts import render

def chatpage(request):
    return render(request, 'chat_app/chatpage.html', context={"msg":"ChatPage Room"})