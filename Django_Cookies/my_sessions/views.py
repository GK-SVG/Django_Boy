from django.shortcuts import render,HttpResponse


def set_session(request):
    request.session['name']='sonam'
    request.session['lname']='kumari'
    return render(request, 'setsessions.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        keys = request.session.keys()
        items = request.session.items()
        request.session.modified = True
        return render(request,'getsessions.html',{'name':name,'keys':keys,'items':items})
    else:
        return HttpResponse('Session Expired.......')


    

def del_session(request):
    #deleting session data from DB
    del request.session['name']
    #deleting Session from browser
    request.session.flush()
    #deleting sesion and data from DB and Browser
    request.session.clear_expired()
    return render(request,'delsessins.html')

