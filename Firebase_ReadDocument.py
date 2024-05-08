import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Read a document from Firestore
def read_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        print('Document data:', document.to_dict())
    else:
        print('No such document!')

# Usage example
read_document('users', 'suiAodpmjbtV9uoSJUPz')