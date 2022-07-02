from .models import Profile, User, Token


class CreateProfile:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def create_auth_token(self, user):
        auth_token, created = Token.objects.get_or_create(user=user)
        return auth_token
        
    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            auth_token = self.create_auth_token(user)
            profile, created = Profile.objects.get_or_create(user=user, auth_token=auth_token)
            
        return self.get_response(request)