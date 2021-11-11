from django import forms


product_categories=[('--Ürün Kategorisini Seçiniz--','--Ürün Kategorisini Seçiniz--'),('Kart Setleri','Kart Setleri'),
('Elektromekanik Montaj','Elektromekanik Montaj'),
('Kablo','Kablo'),
('Fiber Optik Kablo','Fiber Optik Kablo'),
('Bobin Trafo','Bobin Trafo'),
('Kabinet Panel Kablo','Kabinet Panel Kablo'),
('Diğer','Diğer')]

company_types=[('--Şirket Türü Seçiniz--','--Şirket Türü Seçiniz--'),('Satıcı','Satıcı'),
('Üretici','Üretici'),
('Yan-Sanayi','Yan-Sanayi'),
('Hizmet','Hizmet'),
('Diğer','Diğer')]

class Supplier1(forms.Form):
    
    company_name = forms.CharField(max_length = 15,label = "Şirket İsmi")
    company_type= forms.CharField(label='Şirket Türü',widget=forms.Select(choices=company_types))
    
    tax_administration= forms.CharField(max_length = 15,label = "Vergi Dairesi")
    tax_number=forms.CharField(label = "Vergi Numarası")
       
    contact_name = forms.CharField(max_length = 15,label = "Adı")
    contact_phone_number = forms.CharField(max_length = 15,label = "İletişim Numarası")
    contact_mail_addres = forms.EmailField(label="İletişim Mail Adresi")
    product_category= forms.CharField(label='Ürün Kategorisi',widget=forms.Select(choices=product_categories))
    
    additional_information = forms.CharField(max_length = 50,label = "Ek")
    def clean(self):
        company_name = self.cleaned_data.get("company_name")
        company_type = self.cleaned_data.get("company_type")
        tax_administration = self.cleaned_data.get("tax_administration")
        tax_number = self.cleaned_data.get("tax_number")
        
        contact_name = self.cleaned_data.get("contact_name")
        contact_phone_number = self.cleaned_data.get("contact_phone_number")
        contact_mail_addres = self.cleaned_data.get("contact_mail_addres")
        product_category = self.cleaned_data.get("product_category")
        additional_information = self.cleaned_data.get("additional_information")
        

        values = {
            "company_name" : company_name,
            "company_type" : company_type,
            "tax_administration" : tax_administration,
            "tax_number" : tax_number,
            
            "contact_name" : contact_name,
            "contact_phone_number" : contact_phone_number,
            "contact_mail_addres" : contact_mail_addres,
            "product_category" : product_category,
            "additional_information" : additional_information,
            
        }
        return values

from django import forms
from .models import Supplier
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["company_name","company_type","tax_administration","tax_number","contact_name","contact_phone_number","contact_mail_addres","product_category","additional_information"]