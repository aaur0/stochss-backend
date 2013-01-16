import webapp2,os

class MainPage(webapp2.RequestHandler):
  def get(self):
      file = open("test.txt", 'w')	
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('Hello, webapp2 World!\n')
      self.response.write('creating anand2.txt using os.system call : \n')
      res= os.system("touch anand2.txt")
      #self.response.write(res) 
      self.response.write('printing the list of files in the directory using os.open call : \n') 
      process = os.popen('ls')
      res= process.read()
      self.response.write(res)
      process.close()
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

