# THIS IS FOR DEVELOPMENT ONLY - DO NOT USE IN PRODUCTION
# This script is used to run a flask development server. It should not be used in production.
# Use the docker container provided to run the backend :) 
# Best regards, Jan Koch


from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)