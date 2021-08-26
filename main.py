#use this to start the website
from website import create_app

app = create_app()

if __name__ == "__main__":
    # run website in debug mode (automatically reruns server whenever you change anything)
    app.run(debug = True)
