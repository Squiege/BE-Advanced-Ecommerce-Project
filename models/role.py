from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)

    # Relationships
    customer_management_roles: Mapped[list["CustomerManagementRole"]] = relationship("CustomerManagementRole", back_populates="role")
