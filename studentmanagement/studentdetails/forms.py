from django import forms


class studentdetailsform(forms.Form):

    studentname = forms.CharField(max_length=20)
    studentdob = forms.DateField()
    Physicsmarks =forms.IntegerField(min_value=0,max_value=100)
    Chemistrymarks = forms.IntegerField(min_value=0,max_value=100)
    Mathsmarks = forms.IntegerField(min_value=0,max_value=100)
    Computersciencemarks =forms.IntegerField(min_value=0,max_value=100)

