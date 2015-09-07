import webapp2

class MainPage(webapp2.RequestHandler):
  MAIN_PAGE_HTML="""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
  <title>FinLearning</title>

  <style type="text/css">
  body {
    padding-left: 11em;
    font-family: Georgia, "Times New Roman",
          Times, serif;
    color: purple;
    background-color: #d8da3d }
  ul.navbar {
    list-style-type: none;
    padding: 0;
    margin: 0;
    position: absolute;
    top: 5em;
    left: 1em;
    width: 9em }
  h1 {
    font-family: Helvetica, Geneva, Arial,
          SunSans-Regular, sans-serif }
  ul.navbar li {
    background: white;
    margin: 0.5em 0;
    padding: 0.3em;
    border-right: 1em solid black }
  ul.navbar a {
    text-decoration: none }
  a:link {
    color: blue }
  a:visited {
    color: purple }
  </style>
</head>

<body>

<!-- Site navigation menu -->
<ul class="navbar">
  <li><a href="search.html">Search Data</a>
  <li><a href="add.html">Add New Data</a>
</ul>

<!-- Main content -->
<h1>Financial Data Analysis Platform</h1>

</body>
</html>
"""
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(self.MAIN_PAGE_HTML)

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ], debug=True)
