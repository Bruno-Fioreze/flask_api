from flask_restful import Resource


class Contacts(Resource):
    def get(request):
        return {"message": "Hello World!"}
    
    def post():
        pass

    def put():
        pass
    
    def patch():
        pass
    
    def delete():
        pass
    
