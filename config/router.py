import os
from app import app
from controllers import songs, auth, forumtopics

app.register_blueprint(songs.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
app.register_blueprint(forumtopics.api, url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    if os.path.isfile('dist/' + path):
        return app.send_static_file(path)

    return app.send_static_file('index.html')
