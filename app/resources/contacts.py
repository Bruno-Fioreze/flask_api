from flask_restful import Resource, marshal
from app.resources.models import Contact
from app import request, db
from app.resources.schemas import contact_field

class Contacts(Resource):
    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts, contact_field, "contacts")
    
    def post(self):
        payload = request.only(["name", "cellphone"])
        name = payload["name"]
        cellphone = payload["cellphone"]
        contact = Contact(name, cellphone)
        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_field, "contact")    
        
    def put(self):
        pass
    
    def patch(self):
        pass
    
    def delete(self):
        pass
    
