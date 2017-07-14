from mainapp import app

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8000)