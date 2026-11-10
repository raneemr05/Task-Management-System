class User:
    '''Stores user information'''
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.name = name
        # sensitive data that should only be accessible via a getter
        self.__email = email    # private - sensitive data
 
    def get_user_id(self):
        return self.__user_id
 
    def get_email(self):
        return self.__email
