from apps.engine import create_app


def engine_app():
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=5000)
