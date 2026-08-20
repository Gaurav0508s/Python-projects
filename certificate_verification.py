import json
import os

FILE_NAME = "certificates.json"


def load_certificates():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {}


def save_certificates():
    with open(FILE_NAME, "w") as file:
        json.dump(certificates, file, indent=4)


def add_certificate():
    certificate_id = input("Enter Certificate ID: ").strip()

    if certificate_id in certificates:
        print("Certificate ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    date = input("Enter Issue Date: ").strip()

    certificates[certificate_id] = {
        "name": name,
        "course": course,
        "date": date,
        "status": "Valid"
    }

    save_certificates()
    print("Certificate added successfully.")


def verify_certificate():
    certificate_id = input("Enter Certificate ID: ").strip()

    if certificate_id not in certificates:
        print("Certificate not found.")
        return

    certificate = certificates[certificate_id]

    print("\nCertificate Details")
    print("-------------------")
    print("Certificate ID:", certificate_id)
    print("Name:", certificate["name"])
    print("Course:", certificate["course"])
    print("Issue Date:", certificate["date"])
    print("Status:", certificate["status"])


def view_certificates():
    if not certificates:
        print("No certificates available.")
        return

    print("\nAll Certificates")
    print("----------------")

    for certificate_id, certificate in certificates.items():
        print("\nCertificate ID:", certificate_id)
        print("Name:", certificate["name"])
        print("Course:", certificate["course"])
        print("Issue Date:", certificate["date"])
        print("Status:", certificate["status"])


def search_certificate():
    search = input("Enter student name or course: ").strip().lower()
    found = False

    for certificate_id, certificate in certificates.items():
        if (search in certificate["name"].lower()
                or search in certificate["course"].lower()):

            print("\nCertificate ID:", certificate_id)
            print("Name:", certificate["name"])
            print("Course:", certificate["course"])
            print("Issue Date:", certificate["date"])
            print("Status:", certificate["status"])

            found = True

    if not found:
        print("No matching certificate found.")


def revoke_certificate():
    certificate_id = input("Enter Certificate ID: ").strip()

    if certificate_id not in certificates:
        print("Certificate not found.")
        return

    certificates[certificate_id]["status"] = "Revoked"

    save_certificates()
    print("Certificate has been revoked.")


def delete_certificate():
    certificate_id = input("Enter Certificate ID: ").strip()

    if certificate_id not in certificates:
        print("Certificate not found.")
        return

    confirm = input("Are you sure you want to delete it? (yes/no): ")

    if confirm.lower() == "yes":
        del certificates[certificate_id]
        save_certificates()
        print("Certificate deleted successfully.")
    else:
        print("Delete operation cancelled.")


certificates = load_certificates()


while True:
    print("\nCertificate Verification System")
    print("--------------------------------")
    print("1. Add Certificate")
    print("2. Verify Certificate")
    print("3. View All Certificates")
    print("4. Search Certificate")
    print("5. Revoke Certificate")
    print("6. Delete Certificate")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_certificate()

    elif choice == "2":
        verify_certificate()

    elif choice == "3":
        view_certificates()

    elif choice == "4":
        search_certificate()

    elif choice == "5":
        revoke_certificate()

    elif choice == "6":
        delete_certificate()

    elif choice == "7":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")