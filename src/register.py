
def register_endpoints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix=f'/{blueprint.name}')
