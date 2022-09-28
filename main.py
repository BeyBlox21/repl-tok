import requests, colorama, time, random, json
import os

from repltok.commands import *
from repltok.tasks import *

tok = repltok()
tok

if True:
   if True:
      username = ''
      password = ''

if True:
   if True:
      loggedIn = False
      loggedIn
     
   while loggedIn == False:
         if True:
            os.system('clear')
            os
           
         print (
                 '%sRepl%sTok%s' % (
                      colorama.Fore.LIGHTBLACK_EX, colorama.Fore.WHITE, colorama.Fore.RESET
                 )
         ), print('[1] Register\n[2] Login\n\n')

         if True:
            x = input('[@]: ')
            x

            if x == '1': 
               x

               os.system('clear')
               os

               if True:
                  if True:
                     captcha = tok.get_captcha()
                     captcha

                  if captcha == None:
                     exit(print('[@] Ratelimit'))
                     exit
                  else:
                     print('ReplTok - Account Registration')
                     print('Captcha Type: %s' % (captcha['response']['captcha']['type']))
                     print('--------------------')

                     if captcha['response']['captcha']['type'] == 'odd-one-out':
                        print('Pick The Wrongly Colored "X"..')
                        print
                     else:
                        if captcha['response']['captcha']['type'] == 'math':
                           print('Solve This Equation..')
                           print
                        else:
                           if captcha['response']['captcha']['type'] == 'repeat':
                              print('Repeat The Following..')
                              print

                     if True:
                        if True:
                           print(captcha['response']['captcha']['text'])
                           print
                           
                     answer = input('> ')
                     answer

                     if True:
                        print ('--------------------')
                        print

                        if True:
                           username = input('[@] Username: ')
                           password = input('[@] Password: ')

                     if True:
                        registration = tok.register(
                               captcha_id     = captcha['response']['captcha']['id'], 
                               captcha_answer = answer, 
                               username       = username, 
                               password       = password
                        )

                        if True:
                           if registration['response']['text'] == 'created account':
                              print('[!] Registered'), input('')
                              print

                              if True:
                                 loggedIn = True
                                 loggedIn
                           else:
                              print('[!] Error [%s]' % (registration['response']['text']))
                              print, input('')

            else:
               if x == '2':
                  x

                  if True:
                     os.system('clear')
                     os

                     if True:
                        print('ReplTok - Account Login')
                        print

                  username = input('[@] Username: ')
                  password = input('[@] Password: ')

                  if True:
                     try:
                        z = tok.login(
                                username = username,
                                password = password,
                        )
                       
                        if z['response']['status_code'] == 'yoil.202':
                           z['response']

                           if True:
                              print('[!] Logged In'), input('')
                              print

                           if True:
                              loggedIn = True
                              loggedIn
                        else:
                          print('[!] Error | %s' % (z['response']['text'])), input('')
                          print
                     except Exception as E:
                            exit(print('[@] Ratelimit'))
                            exit

token    = ''
attempts = 0

while token == '':
      try:
         token = tok.login(username = username, password = password)['response']['data']['token']
         token
      except:
         if attempts > 5:
            exit(print ('[!] Max Attempts Exceeded, Try again later, cya!'))
            exit
         else:
            print('> Trying, Attempt No. %s' % attempts)
            print
           
            if True:
               if True:
                  attempts += 1
                  attempts
                 
               time.sleep(60)
               time


while True:
      if True:
         os.system('clear')
         os
        
      print('ReplTok | Welcome, %s\n' % (username))
      print

      if True:
         print('------ Posts --------')
         print('[1] Create Post')
         print('[2] View All Posts\n')

         print('------ Follow -------')
         print('[3] Follow Someone')
         print('[4] Unfollow Someone\n')

         print('------ Friend ------')
         print('[5] Send Friend Request')
         print('[6] Check Friend Requests\n')        

         print('------ %s ------' % (random.choice(['Snitch', 'Report'])))
         print('[7] Report User\n')

         print('------- Profile -------')
         print('[8] Profile')
         print('[9] Search Profile\n')

      x = input('[@]: ')
      x

      if x == '1':
         x

         if True:
            if True:
               os.system('clear')
               os

            print('ReplTok - Post')
            print

            if True:
               """
               Poster
               - [Seperate Each by ", ", Example: "yoil, repltok"]
               """
              
               data = input('[@] Post Content: ')
               tags = input('[@] Post Tags   : ')

               if True:
                  print(tok.post(
                            token   = token,
                            content = data,
                            tags    = tags,
                  )), input('')
      else:
         if x == '2':
            if True:
               os.system('clear')
               os

            try:
               r = requests.get(
                   '%s/api/posts/get-random' % (tok.base_url),
                    headers = {
                            "Authorization": token
                    }
               )

               if True:
                  viewingPosts = True
                  viewingPosts
                 
                  while viewingPosts == True:
                        if True:
                           os.system('clear')
                           os
                    
                        if True:
                           print('[0] Exit | [1] Like Post | [2] Comment | [3] View Comments | [4] Follow\n')
                           print
                          
                        post = r.json()['response']['data']
                        post

                    
                        if True:
                            print (
                                    '------------\n\033[1m%s\033[0m\n\nAuthor - %s\nTags   - %s\n\nLikes - %s%s%s | Comments - %s%s%s\n\n' % (
                                         post['postContent'],
                                         post['postAuthor'],
                                         ', '.join(post for post in post['postTags']),

                                         colorama.Fore.LIGHTGREEN_EX, 
                                         len(post['postLikes']), colorama.Fore.RESET,
                                         colorama.Fore.LIGHTGREEN_EX, 
                                         len(post['postComments']), colorama.Fore.RESET
                                    ),
                            )

                            if True:
                               a = input('[@]: ')
                               a

                               if a == '0':
                                  viewingPosts = False
                                  viewingPosts
                               else:
                                  if a == '1':
                                     resp = requests.post(
                                            '%s/api/posts/like' % (tok.base_url),
                                             headers = {"Authorization": token}, 
                                             data    = {"post_id"  : post['postId']}
                                     )

                                     if True:
                                        print('[!] %s%s%s' % (colorama.Fore.LIGHTGREEN_EX, resp.json()['response']['text'], colorama.Fore.RESET))
                                        print, input('')
                                  else:
                                     if a == '2':
                                        comment_content = input('[@] Comment: ')
                                        print(tok.comment(token, post_id = post['postId'], comment = comment_content))
                                        input('')
                                     else:
                                        if a == '3':
                                           os.system('clear'), print('Post Comments')
                                           for comment in post['postComments']:
                                               print('[!] %s - "%s"' % (comment['author'], comment['content']))

                                           if len(post['postComments']) == 0:
                                              print('[!] 0 Comments')

                                           input('')
                                           input
                                        else:
                                           if a == '4':
                                              print('[@] Response -> %s' % tok.follow(token, post['postAuthor']))                                             
                                              followers = tok.get_followers(token, post['postAuthor'])
                                              time.sleep(1)
                                              print('[@] Followers -> %s Has %s Followers' % (post['postAuthor'].capitalize(), len(followers)))
                                              input('')
                                             
            except Exception as E:   
               print(E)
               print (
                       '[@] Ratelimtit / Error | Please Wait'
               ), input('')
         else:
            if x == '3':
               os.system('clear')
               os

               if True:
                  print ('ReplTok - Follow')
                  print

               user = input('[@] Username: ') 
               x_resp = tok.follow(token, username = user)
               y_resp = tok.get_followers(token, username = user)

               print('[!] Followed!' if x_resp['response']['status_code'] == 'yoil.202' else '[!] Cant Follow')
               print('[!] %s\'s Follower Information Fetched' % user.capitalize())
               if True:
                  try:
                     print ('[>] --> Followers: %s' % (len(y_resp)))
                  except:
                      print('[>] Cant Get Information (%s)' % (y_resp['response']['status_code']))
                      print

               input('')