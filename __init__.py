def create_app():

    app = Flask(__name__)

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
