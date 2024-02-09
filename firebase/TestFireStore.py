from FirebaseUtil import FirebaseUtil

if __name__ == "__main__":
    db = FirebaseUtil.get_project_firestore()

    data = {
        'jobName': 'a job',
        'jobID': 'abc'
    }

    doc_ref = db.collection("users").document("benizakurayana").collection("applied-jobs").document("jpIvae8oLU0Wdj7MCKol")

    doc_ref.set(data)

