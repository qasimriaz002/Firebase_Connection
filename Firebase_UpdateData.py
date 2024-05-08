import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore

# Update a document in Firestore
def update_document(collection, document_id, update_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(update_data)
    print('Document updated successfully!')

# Usage example
update_document('users', 'document_id123', {'name': 'Jamil Aslam'})