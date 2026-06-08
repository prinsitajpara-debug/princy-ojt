from pathlib import Path

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import BackgroundTasks
from fastapi import Form

from sqlalchemy.orm import Session

from app.auth.api_key import (
    verify_api_key
)

from app.database import (
    get_db
)

from app.utils.validator import (
    validate_cv
)

from app.models import (
    Document
)

from app.services.document_processor import (
    process_document
)

router = APIRouter(
    prefix="/api/v1/documents",
    tags=["Documents"]
)

UPLOAD_DIR = "uploads/cvs"

Path(
    UPLOAD_DIR
).mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload-cv")
async def upload_cv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    employee_id: int = Form(...),
    db: Session = Depends(get_db),
    auth=Depends(
        verify_api_key
    )
):

    validate_cv(
        file.content_type
    )

    file_path = (
        f"{UPLOAD_DIR}/"
        f"{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    new_document = Document(
        employee_id=employee_id,
        file_name=file.filename,
        document_type="cv",
        file_path=file_path
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    background_tasks.add_task(
        process_document,
        file.filename
    )

    return {
        "message":
        "CV uploaded successfully",
        "file": file.filename,
        "document_id": new_document.id
    }


