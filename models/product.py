from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Relationships
    orders: Mapped[list['Order']] = relationship('Order', back_populates='product')
