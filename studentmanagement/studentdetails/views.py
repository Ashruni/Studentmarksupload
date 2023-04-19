from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import*
from .models import*


# Create your views here.
def studentdatavalidation(request):
    if request.method=='POST':
        a=studentdetailsform(request.POST)
        if a.is_valid():


            sn =a.cleaned_data['studentname']
            sdob=a.cleaned_data['studentdob']
            pm=a.cleaned_data['Physicsmarks']
            cm=a.cleaned_data['Chemistrymarks']
            mm=a.cleaned_data['Mathsmarks']
            csm=a.cleaned_data['Computersciencemarks']
            per=pm+cm+mm+csm/400*100
            request.session['studentname'] = sn

            b=studentdetailmodel(studentname=sn,studentdob=sdob,Physicsmarks=pm,Chemistrymarks=cm,Mathsmarks=mm,Computersciencemarks=csm)
            b.save()
            return redirect(studentdetaildisplay)
        else:
            return HttpResponse("something went wrong")
    else:
        return render(request,"studentdetails.html")


def studentdetaildisplay(request):
    use=request.session['studentname']

    a = studentdetailmodel.objects.all()
    py=[]
    che = []
    ms = []
    csm = []
    perc = []
    stnm=[]
    stdob=[]
    for i in a:
        ph= i.Physicsmarks
        py.append(ph)
        ch = i.Chemistrymarks
        che.append(ch)
        mt = i.Mathsmarks
        ms.append(mt)
        cs = i.Computersciencemarks
        csm.append(cs)
        snm = i.studentname
        stnm.append(snm)
        sdob=i.studentdob
        stdob.append(sdob)
        sum=ph+ch+mt+cs
        div=sum/400
        per=div*100
        perc.append(per)

    h=zip(stnm,stdob,py,che,ms,csm,perc)
    return render(request,'studentdisplay.html',{'h':h})




