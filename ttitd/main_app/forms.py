

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = [
            'profile_name',
            'location',
            'gender',
            'age',
            'weight',
            'bio',
            'social_link',
            'ghost_key'
        ]
