from django.contrib.auth.models import User

class EmailAuth:
    """
    Authenticate a user by email
    """
    
    def authenticate(self, username=None, password=None):
        """
        Get a user instance based of the email and password
        """
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            
            return None
        
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Used by django authentication to retrieve a user
        """
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            
            return None
        
        except User.DoesNotExist:
            return None