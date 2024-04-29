# # creating sign up and login from using django forms 

# from django import forms 

# class signupForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())


# class loginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))    
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    
    
    
# # creating sign up and login from UserCreationForm
# Advantage of using UserCreationForm over forms - It assists in monitoring user input validation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        

class signupForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=150,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unique email address'}))
    
    
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] ='User name'
        self.fields['username'].label = ''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only </small></span>'
        
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text=' <ul class="form-text text-muted" > <li>Your password can\'t be too similar to your personal information.</li> <li> Your password must contain 8 characters. </li><li>Your password can\'t be too commonly used password</li> <li> Your password can\'t be entirely numeric. </ul>'
        
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

        

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form'}))




""" PRODUCT UPLOAD FORM CREATION """
from .models import productTable

class Product_form(forms.ModelForm):
    class Meta:
        model = productTable
        fields = [
            # 'productId',
            'product_name',
            'product_img',
            'category',
            'price',
            'quantity',
            'description',
            'created_at',
            'user_id'
        ]
        
        widgets = {
            'description': forms.Textarea(attrs={'cols':100, 'rows':10}),
        }