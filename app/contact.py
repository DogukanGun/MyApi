from fastapi import APIRouter, Depends, HTTPException, Request

from app.data.contact_data import ContactForm
from app.data.general import return_success_response
from utils.constants.collection_name import CollectionName
from utils.constants.environment_keys import EnvironmentKeys
from utils.database.database import Database, get_db
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager
from utils.notification.send_email import send_email

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("")
def create_contact_form(
        contact_form: ContactForm,
        #db: Database = Depends(get_db),
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    #obj_id = db.insert_object(CollectionName.CONTACT_FORM.value, contact_form.__dict__)
    #if obj_id is None or str(obj_id) == "":
    #    raise HTTPException(status_code=400, detail="Database error")
    send_email(env_manager.get_key(EnvironmentKeys.EMAIL.value), "Contact Form", "Contact Form", contact_form.__str__())
    return return_success_response()
