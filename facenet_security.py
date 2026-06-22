import os
import cv2
import numpy as np
from keras_facenet import FaceNet
from mtcnn import MTCNN
from scipy.spatial.distance import euclidean

AUTHORIZED_DIR = "authorized"
TEST_DIR = "test"
THRESHOLD = 0.9

detector = MTCNN()
facenet_model = FaceNet()


def extract_face(image_path, required_size=(160, 160)):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(image_rgb)

    if len(faces) == 0:
        raise ValueError(f"No face detected in image: {image_path}")

    x, y, width, height = faces[0]["box"]
    x, y = abs(x), abs(y)

    face = image_rgb[y:y + height, x:x + width]
    face = cv2.resize(face, required_size)

    return face


def get_embedding(image_path):
    face = extract_face(image_path)
    face = np.expand_dims(face, axis=0)
    embedding = facenet_model.embeddings(face)
    return embedding[0]


def build_authorized_database():
    database = {}

    for filename in os.listdir(AUTHORIZED_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            identity = os.path.splitext(filename)[0]
            image_path = os.path.join(AUTHORIZED_DIR, filename)

            try:
                embedding = get_embedding(image_path)
                database[identity] = embedding
                print(f"Loaded authorized identity: {identity}")
            except Exception as e:
                print(f"Skipped {filename}: {e}")

    return database


def verify_identity(test_image_path, database):
    test_embedding = get_embedding(test_image_path)

    best_match = None
    smallest_distance = float("inf")

    for identity, known_embedding in database.items():
        distance = euclidean(test_embedding, known_embedding)

        if distance < smallest_distance:
            smallest_distance = distance
            best_match = identity

    if smallest_distance < THRESHOLD:
        return "AUTHORIZED", best_match, smallest_distance
    else:
        return "UNAUTHORIZED", "Unknown Individual", smallest_distance


def run_image_test(test_image_path):
    print("\nBuilding authorized personnel database...")
    database = build_authorized_database()

    if not database:
        print("No authorized identities found. Add images to the authorized folder.")
        return

    print("\nTesting facial recognition system...")
    status, identity, distance = verify_identity(test_image_path, database)

    print("\n--- SECURITY ACCESS RESULT ---")
    print(f"Status: {status}")
    print(f"Identity: {identity}")
    print(f"Distance Score: {distance:.4f}")

    if status == "AUTHORIZED":
        print("Access Granted")
    else:
        print("Access Denied")


if __name__ == "__main__":
    test_image = os.path.join(TEST_DIR, "test.jpg")

    if not os.path.exists(test_image):
        print("Please place a test image named test.jpg inside the test folder.")
    else:
        run_image_test(test_image)