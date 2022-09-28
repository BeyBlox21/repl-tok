import requests

class repltok: 
      def __init__(self):
          self.base_url = 'https://repl-tok-database.yoil.repl.co'
          self.base_url

      def get_captcha(self):
          r = requests.post('%s/api/create-captcha' % (self.base_url))
          r

          if r.status_code == 429:
             return None
          else:
             if True:
                return r.json()

      def get_followers(self, token = '', username = ''):
          return requests.get(
                 '%s/api/users/followers' % (self.base_url),
                  headers = {
                          'Authorization': token
                  }, data = {
                          'username' : username
                  }
          ).json()
        
      def follow(self, token = '', username = ''):
          return requests.post(
                 '%s/api/users/followers' % (self.base_url),
                  headers = {
                          'Authorization': token
                  }, data = {
                          'username' : username
                  }
          ).json()  
  
      def post(
          self,
          token = '',
          content = '',
          tags  = '',
      ):
          return requests.post(
                 '%s/api/posts/create' % (self.base_url),
                  headers = {
                          'Authorization': token
                  }, data = {
                          'post_data'    : content,
                          'post_tags'    : tags
                  }
          ).json()
        
      def login(
          self,
          username = '',
          password = '',
      ):
          return requests.post(
                 '%s/api/login' % self.base_url,
                  data = {
                       'username'  : username,
                       'password'  : password,
                  }
          ).json()

      def comment(
          self,
          token = '',
          post_id = '',
          comment = ''
      ):
          return requests.post(
                 '%s/api/posts/comment' % (self.base_url),
                  headers = {
                          'Authorization': token
                  }, data = {
                          'post_id'      : post_id,
                          'comment_data' : comment
                  }
          ).json()
        
      def register(
          self,
          username = '',
          password = '',
          captcha_id = '',
          captcha_answer = ''
      ):
          return requests.post(
                 '%s/api/register' % self.base_url,
                  data = {
                       'captcha_id'     : captcha_id,
                       'captcha_answer' : captcha_answer,
                       'username'       : username,
                       'password'       : password,
                  }
          ).json()
          