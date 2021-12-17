from app import create_app, db
from app.resources.models import User, Contact
from flask_migrate import Migrate 


app =  create_app("development")
Migrate(app, db)

@app.shell_context_processor
def shel_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Contact=Contact,
    )
