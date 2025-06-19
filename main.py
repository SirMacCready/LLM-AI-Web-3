import upload
from get_cloud_docs import get_docs
import os
def master(url):
    file_name = get_docs(url)
    try:
        if file_name.endswith(".txt"):
            print("find")
            upload.upload_txtfile(file_name)

        elif file_name.endswith(".json"):
            upload.upload_jsonfile(file_name)
        elif file_name.endswith(".pdf"):
            upload.pdf2text(file_name)
        else:
            print("File type not supported.")
    except Exception as e:
        print(e)
    os.remove(file_name)


if __name__ == "__main__":
    FILE_URL = "https://www.healthymood.fr/wp-content/uploads/ebook-healthymood_Septembre2020_1.pdf"
    master(FILE_URL)  # Insert a URL to a file you want to download and process
