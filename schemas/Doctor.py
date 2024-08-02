from schemas import User, UserBase, UserCreate, UserUpdate


class DoctorBase(UserBase):
    expirience: int
    speciality: str

class DoctorCreate(UserCreate, DoctorBase):
    pass

class DoctorUpdate(UserUpdate, DoctorBase):
    expirience: int | None = None
    speciality: str | None = None

class Doctor(User, DoctorBase):
    pass
