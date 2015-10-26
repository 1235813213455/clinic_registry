from django import forms

class RegisterForm(forms.Form):
    doctor_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    doctor_name = forms.CharField(label="Doctor name", \
                    widget=forms.TextInput(attrs={'readonly':'readonly'}))
    assignment_date = forms.CharField(label="Assignment date", \
                    widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    assignment_time = forms.CharField(label="Assignment time", \
                    widget=forms.TextInput(attrs={'readonly':'readonly'}))
    second_name = forms.CharField(label="Second name", max_length=200, required=True)
    first_name = forms.CharField(label="First name", max_length=200, required=True)
    father_name = forms.CharField(label="Father name", max_length=200, required=False)
