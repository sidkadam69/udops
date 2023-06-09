from udops.src.dep.Manager.AuthenticationControlManager import udpos_authentication
from udops.src.dep.Manager.AuthoriseControlmanager import udops_authorise
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
prop=properties()
connection = Connection()
conn = connection.get_connection()

class UserAuthenticationHandler:
    def authenticate_user(self,ACCESS_TOKEN):
        authentication = udpos_authentication()
        user_id = authentication.authenticate_user(ACCESS_TOKEN,conn)
        return user_id
        # if username == 1:
        #     return ("invalid user")
        # else:
        #     print("Authentication is successful!!!!")
        #     authorise = udops_authorise()
        #     return authorise.authorise_access_to_corpus(username,conn)
    def get_user_team(self,user_id):
        authentication = udpos_authentication()
        team_id= authentication.get_user_team(user_id,conn)
        if team_id ==1:
            return 1
        else:
            return team_id

    def authorize_user(self,user_id,corpus_id,access_type):
        authentication = udops_authorise()
        if authentication.authorise_user(user_id,corpus_id,access_type,conn)==1:
            return 1
        else:
            return 2