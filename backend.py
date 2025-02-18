# Setup Pydantic model 
from pydantic import BaseModel
from typing import List
class RequestState(BaseModel):
    model_name:str
    mode_provider:str
    system_prompt:str
    message:List[str]
# Setup AI Agent from FrontEnd Request
# Run app & Explore Swaggers UI
