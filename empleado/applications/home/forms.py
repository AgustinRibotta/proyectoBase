from django import forms

from .models import PruebaModels


class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = PruebaModels
        fields = (
            'titulo',
            'sub_titulo',
            'cantidad',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese un titulo'
                }            
            ),
            'sub_titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese un sub titulo'
                }
            ),
            'cantidad': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese una cantidad mayor a 10'
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')

            # TODO Validation
    
        return cantidad
