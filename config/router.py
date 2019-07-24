from app import app
from controllers import songs, auth, forumtopics

app.register_blueprint(songs.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
app.register_blueprint(forumtopics.api, url_prefix='/api')
