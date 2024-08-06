from django import forms
c=[('MALE','male'),('FEMALE','female')]
s=[('PYTHON','python'),('SQL','sql')]
class studentform(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    #DOB=forms.DateTimeField()
    gender=forms.ChoiceField(choices=c)
    #gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    subjects=forms.MultipleChoiceField(choices=s)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':5}))
