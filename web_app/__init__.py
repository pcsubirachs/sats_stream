# import the create_app function from our app file
from .app import create_app

# if we run the init file, it should run our app after importing it
if __name__ =="__main__":
    my_app = create_app()
    my_app.run(debug=True)