import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore

# Create a new document in Firestore
def create_document(collection, document_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    print('Document created with ID:', doc_ref.id)

# Usage example
create_document('users', {'name': 'Qasim Riaz', 'email': 'qasim.riaz@giki.edu.pk'})