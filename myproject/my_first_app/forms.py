from django import forms
from .models import Employee, Document

class empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['empname','phone','email','date','address']
        # fields='_all_'  # This line is commented out to only include specific fields
        # exclude=['date'] # Exclude the 'date' field from the form
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__' #include all fields from the Document model or ['title', 'image', 'pdf'] to specify