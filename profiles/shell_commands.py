from django.contrib.auth import get_user_model

User = get_user_model()

random_ = User.objects.last()

# my fallowers
random_.profile.fallowers.all()

#who i fallow
random_.is_fallowing.all()
