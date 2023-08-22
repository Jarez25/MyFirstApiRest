from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uid
from pydantic import BaseModel
from src.router.get_contacts import ManageDB

from src.lib.managedb import ManageDB


class ContactModel(BaseModel):
    id: int = str(uid())
    name: str = ""
    phone: str = ""


app = FastAPI()
dt = ManageDB()


@app.get('/')
def root():
    return {'mensaje': "este es un mensaje"}


@app.get('/contacts')
def get_contacts():
    return dt.Read_contacts()


@app.get('/contacts/{id_contact}')
def get_single_contact(id_contact: int):
    contacts = dt.Read_contacts()

    for contact in contacts:
        if contact["id"] == id_contact:
            return contact

    raise HTTPException(status_code=404, detail="contacto no encontrado")


@app.post('/contacts')
def add_contacts(new_contacts: ContactModel):
    contacts = dt.Read_contacts()
    new_contacts = new_contacts.dict()

    contacts.append(new_contacts)

    dt.write_contacts(contacts)

    return {
        "sucess": "True",
        "message": "adden new contact"
    }


@app.put('/contacts/{id_contact}')
def update_contact(id_contact: int, new_contact: ContactModel):
    contacts = dt.Read_contacts()

    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.dict()

            if new_contact.name == "":
                contacts[index]['name'] = contact['name']

            if new_contact.phone == "":
                contacts[index]['phone'] = contact['phone']

            dt.write_contacts(contacts)

            return {
                "success": "True",
                "message": "update Contacts"
            }

    raise HTTPException(status_code=404, detail="contacto no encontrado")


@app.delete('/contacts/{id_contact}')
def remove_contact(id_contact: int):
    contacts = dt.Read_contacts()
    updated_contacts = []

    for contact in contacts:
        if contact["id"] == id_contact:
            continue  # Skip the contact you want to delete
        updated_contacts.append(contact)

    dt.write_contacts(updated_contacts)  # Write the updated list of contacts

    return {
        "success": "True",
        "message": "Contact deleted"
    }

    raise HTTPException(status_code=404, detail="Contacto no encontrado")
