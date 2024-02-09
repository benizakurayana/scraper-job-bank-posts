import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseUtil:
    @staticmethod
    def initialize_firebase():
        cred = credentials.Certificate("C:/Users/Jane/OneDrive/Documents/firebase keys/scraper-job-bank-posts-firebase-adminsdk-2jqik-30a652d252.json")
        firebase_admin.initialize_app(cred)

    @staticmethod
    def get_project_firestore():
        FirebaseUtil.initialize_firebase()
        project_firestore = firestore.client()
        return project_firestore


