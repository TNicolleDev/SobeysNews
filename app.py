#importing the Flask Class
from flask import Flask
from flask import render_template
from blueprints.stories import stories_bp
from blueprints.merch import merch_bp
from blueprints.auth import auth_bp
from blueprints.blog import blog_bp
import db

# create an instance of this class. 
# The first argument is the name of the application’s module or package.
#  __name__ is a convenient shortcut for this that is appropriate for most cases. 
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

app.config.from_mapping(
   DATABASE='sobeysnews.sqlite3',
   SECRET_KEY='DEV'
)

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def home():
   return render_template("home.html")

app.register_blueprint(stories_bp)
app.register_blueprint(merch_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)

db.init_app(app)

