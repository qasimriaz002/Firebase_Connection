import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore
# Delete a document from Firestore
def delete_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()
    print('Document deleted successfully!')

# Usage example
delete_document('users', 'document_id123')