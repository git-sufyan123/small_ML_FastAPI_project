from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional

class data_validation(BaseModel):
    age: Annotated[int,Field(...,description='age of patient',gt=0,lt=100)]
    sex: Annotated[Literal['male','female'],Field(...,description='gender of patient',examples=['male','female'])]
    bmi: Annotated[float,Field(...,description='bmi of patient',gt=0,lt=100)]
    children: Annotated[int,Field(...,description='number of children patient have',ge=0,lt=10)]
    smoker: Annotated[Literal['yes','no'],Field(...,description='whether patient is smoker or not',examples=['yes','no'])]
    region: Annotated[Literal['southwest','southeast','northwest','northeast'],Field(...,description='region of patient',examples=['southwest','southeast','northwest','northeast'])]

