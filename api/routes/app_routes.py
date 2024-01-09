from api.routes.recommendation_system.popularity_bp import popularity_recommend_bp


def app_routes(app):
    app.register_blueprint(popularity_recommend_bp, url_prefix='/api')
