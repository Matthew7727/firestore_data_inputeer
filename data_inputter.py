import argparse
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firestore
def init_firestore():
    cred = credentials.Certificate('credentials.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()

# Add data to Firestore
def add_data_from_json(db, collection, document_id, json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.set(data)
    print(f'Data added to {collection}/{document_id} from {json_file_path}')

def main():
    parser = argparse.ArgumentParser(description="Firestore CLI Tool")
    parser.add_argument('collection', help="Firestore collection name")
    parser.add_argument('document_id', help="Firestore document ID")
    parser.add_argument('json_file', help="Path to the JSON file containing data")

    args = parser.parse_args()

    # Initialize Firestore
    db = init_firestore()

    # Add data from JSON file to Firestore
    add_data_from_json(db, args.collection, args.document_id, args.json_file)
    

if __name__ == '__main__':
    main()
