from django import forms

from .models import CustomerRequest


class CustomerRequestForm(forms.ModelForm):


    ANTENNA_CHOICES = [

        ("", "Select Antenna Type"),

        ("Yagi Antenna", "Yagi Antenna"),

        ("Parabolic Antenna", "Parabolic Antenna"),

        ("Panel Antenna", "Panel Antenna"),

        ("Log Periodic Antenna", "Log Periodic Antenna"),

        ("Helical Antenna", "Helical Antenna"),

        ("Horn Antenna", "Horn Antenna"),

        ("Dipole Antenna", "Dipole Antenna"),

        ("Monopole Antenna", "Monopole Antenna"),

        ("GPS Antenna", "GPS Antenna"),

        ("GSM Antenna", "GSM Antenna"),

        ("Wi-Fi Antenna", "Wi-Fi Antenna"),

        ("RFID Antenna", "RFID Antenna"),

        ("VHF Antenna", "VHF Antenna"),

        ("UHF Antenna", "UHF Antenna"),

        ("4G/LTE Antenna", "4G/LTE Antenna"),

        ("5G Antenna", "5G Antenna"),

        ("Vehicle Antenna", "Vehicle Antenna"),

        ("Outdoor Antenna", "Outdoor Antenna"),

        ("Indoor Antenna", "Indoor Antenna"),

        ("Custom Antenna", "Custom Antenna"),

    ]


    product = forms.ChoiceField(

        choices=ANTENNA_CHOICES,

        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )

    )


    class Meta:

        model = CustomerRequest


        fields = [
            "name",
            "email",
            "phone",
            "product",
            "quantity",
            "message",
        ]


        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Customer name",
                }
            ),


            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                }
            ),


            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone number",
                }
            ),


            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Enter quantity",
                }
            ),


            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder":
                    "Enter additional requirements...",
                    "rows": 5,
                }
            ),

        }