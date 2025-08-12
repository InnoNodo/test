import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import (
    Column, BigInteger, Numeric, DateTime, String, Enum, func, ForeignKey, text, Index
)
from sqlalchemy.dialects.postgresql import JSONB, UUID as PGUUID
from app.db import Base

tx_state_enum = Enum("OPEN", "CONFIRMED", "CANCELED", "EXPIRED", name="tx_state", create_type=False)

class Balance(Base):
    __tablename__ = "balances"

    user_id = Column(BigInteger, primary_key=True)
    current = Column(Numeric(20, 4), nullable=False, server_default=text("0"))
    maximum = Column(Numeric(20, 4), nullable=False, server_default=text("0"))
    locked = Column(Numeric(20, 4), nullable=False, server_default=text("0"))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(BigInteger, ForeignKey("balances.user_id", ondelete="CASCADE"), index=True, nullable=False)
    amount = Column(Numeric(20, 4), nullable=False)
    state = Column(tx_state_enum, nullable=False)
    owner_service = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    metadata = Column(JSONB, nullable=True)

Index("idx_tx_user_state", Transaction.user_id, Transaction.state)
