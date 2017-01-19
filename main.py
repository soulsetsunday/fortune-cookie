import webapp2
import random

def getRandomFortune():
    fortunes = [
    "Today it's up to you to create the peacefulness you long for.",
    "A friend asks only for your time not your money.",
    "If you refuse to accept anything but the best, you very often get it."]
    fortunepick = random.randrange(0, len(fortunes))
    return fortunes[fortunepick]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        
        fortune='<strong>'+getRandomFortune()+'</strong>'
        fortune_sentence = 'Your fortune: '+fortune
        fortune_paragraph = '<p>'+fortune_sentence+'</p>'

        lucky_number = '<strong>'+str(random.randint(1,100))+'</strong>'        
        number_sentence = 'Your lucky number: ' + lucky_number
        number_paragraph = '<p>'+number_sentence+'</p>'
        
        cookie_again_button = "<a href ='.'><button>Another cookie?</button></a>"
        
        content = header+fortune_paragraph+number_paragraph+cookie_again_button
        self.response.write(content)
        
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('...')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler)
], debug=True)
