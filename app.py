from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)


    with app.app_context():
        import routes
        from dashboards.dashboard_template_1 import dashboard_template_1
        app = dashboard_template_1(app)

    return app
