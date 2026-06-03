# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     from app.users.routes import users_bp
#     from app.auth.routes import auth_bp
#     from app.health.routes import health_bp

#     app.register_blueprint(
#         users_bp,
#         url_prefix="/api/v1/users"
#     )

#     app.register_blueprint(
#         auth_bp,
#         url_prefix="/api/v1/auth"
#     )

#     app.register_blueprint(
#         health_bp,
#         url_prefix="/health"
#     )

#     return app

from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.users.routes import users_bp
    from app.auth.routes import auth_bp
    from app.health.routes import health_bp

    app.register_blueprint(
        users_bp,
        url_prefix="/users"
    )

    app.register_blueprint(
        auth_bp,
        url_prefix="/auth"
    )

    app.register_blueprint(
        health_bp,
        url_prefix="/health"
    )

    # Show all registered routes
    print("\nRegistered Routes:")
    for rule in app.url_map.iter_rules():
        print(rule)

    return app