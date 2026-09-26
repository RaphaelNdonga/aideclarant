from pathlib import Path
from shutil import copyfileobj
from typing import Annotated
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()
ATTACHMENTS_DIR = Path(__file__).resolve().parent / "attachments"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/parse-documents")
def parse_documents(
    commercial_invoice: Annotated[UploadFile, File(description="Commercial invoice PDF")],
    packing_list: Annotated[UploadFile, File(description="Packing list PDF")],
    certificate_of_origin: Annotated[
        UploadFile, File(description="Certificate of origin PDF")
    ],
):
    documents = {
        "commercial_invoice": commercial_invoice,
        "packing_list": packing_list,
        "certificate_of_origin": certificate_of_origin,
    }
    for name, document in documents.items():
        if document.content_type != "application/pdf":
            raise HTTPException(
                status_code=415,
                detail=f"{name} must be uploaded as application/pdf.",
            )

    ATTACHMENTS_DIR.mkdir(parents=True, exist_ok=True)
    upload_id = uuid4().hex
    saved_documents = {}
    for name, document in documents.items():
        filename = f"{name}_{upload_id}.pdf"
        with (ATTACHMENTS_DIR / filename).open("wb") as destination:
            copyfileobj(document.file, destination)
        saved_documents[name] = f"attachments/{filename}"

    return {
        "message": "Documents saved successfully",
        "documents": saved_documents,
    }
