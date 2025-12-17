from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
  title ='Home Page'
  return render_template('index.html', title='Home Page')

@app.route('/About')
def about():
  title = 'About Page'
  name = 'Nonlaphan'
  email = 'std.67122420228@ubru.ac.th'
  mobile = '092-642-0363'
  age = 20
  return render_template('About.html', 
                         title='About Page',
                         name=name,
                         email=email,
                         mobile=mobile,
                         age=age)
                 
@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = [ 'พิซซ่า', 'ก๋วยเตี๋ยว', 'คะน้าหมูกรอบ',]
  return render_template('favorite_foods.html',
                         title=title,
                         foods=foods)               

@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite sports Page'
  sports = [ 'ฟุตบอล', 'บาสเกตบอล', 'ว่ายน้ำ',]
  return render_template('favorite_sports.html',
                         title=title,
                         sports=sports)           
@app.route('/favorite/movies')
def favorite_movies():
  title = 'Favorite movies Page'
  movies = ['มินเนี่ยน','ข้างบ้าน', 'สาธุ','ธี่หยด','นีโม่']
  return render_template('favorite_movies.html',
                         title=title,
                         movies=movies)           
                                     