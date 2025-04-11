from datetime import date, datetime
import hashlib
from typing import Optional
from sqlalchemy import Date, Index, String, Integer, Time, Boolean, DateTime, Enum as SAEnum, event
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EncryptedType
from app.core.config import settings
from app.db.base import Base
from app.core.fernet_wrapper import FernetWrapper
from passlib.context import CryptContext

ENCRYPTION_KEY = settings.SECRET_KEY

class User(Base):
    __tablename__ = "user"
    __table_args__ = (
         Index('ix_user_dni_hash', 'dni_hash', unique=True),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dni: Mapped[str] = mapped_column(
        EncryptedType(String(512), ENCRYPTION_KEY, lambda: FernetWrapper(ENCRYPTION_KEY)),
        nullable=False
    )
    dni_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        EncryptedType(String(512), ENCRYPTION_KEY, lambda: FernetWrapper(ENCRYPTION_KEY)),
        nullable=True
    )
    phone_number: Mapped[str] = mapped_column(
        EncryptedType(String(512), ENCRYPTION_KEY, lambda: FernetWrapper(ENCRYPTION_KEY)),
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(
        EncryptedType(String(512), ENCRYPTION_KEY, lambda: FernetWrapper(ENCRYPTION_KEY)),
        nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        EncryptedType(String(512), ENCRYPTION_KEY, lambda: FernetWrapper(ENCRYPTION_KEY)),
        nullable=False
    )
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    modify_password: Mapped[bool] = mapped_column(Boolean, default=False)
    # profile_img: Mapped[str] = mapped_column(String(200), nullable=True, default="/static/img/profiles/default.png")
    # job_title: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    # date_of_birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    # employee_id: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, unique=True)
    # hire_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    # emergency_contact: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    # emergency_phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    # active: Mapped[bool] = mapped_column(Boolean, default=True)
    # last_login: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    # created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    # updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    # Relaciones
    user_company_roles = relationship(
        "UserCompanyRole",
        back_populates="user",
        foreign_keys="[UserCompanyRole.user_id]"
    )
    companies = association_proxy("user_company_roles", "company")
    departments = relationship("UserDepartmentRel", back_populates="user")
    locations = relationship("UserLocationRel", back_populates="user")
    notifications = relationship("Notification", back_populates="user")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash(data: str) -> str:
    return pwd_context.hash(data)

def get_credetial_deterministic_hash(value: str) -> str:
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

@event.listens_for(User.dni, 'set', retval=True)
def lowercase_dni(target, value, oldvalue, initiator):
    return value.lower() if isinstance(value, str) else value

@event.listens_for(User, 'before_insert')
def set_dni_hash(mapper, connection, target):
    target.dni_hash = get_credetial_deterministic_hash(target.dni)

@event.listens_for(User, 'before_update')
def update_dni_hash(mapper, connection, target):
    target.dni_hash = get_credetial_deterministic_hash(target.dni)

@event.listens_for(User, 'before_insert')
def set_password_hash(mapper, connection, target):
    def is_already_hashed(password: str) -> bool:
        return password.startswith('$2b$') or password.startswith('$2a$')
    if not is_already_hashed(target.password):
        target.password = get_hash(target.password)
