from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import datetime
from uuid import UUID

class Money(BaseModel):
    __root__: Decimal

class BalanceOut(BaseModel):
    user_id: int
    current: Decimal
    maximum: Decimal
    locked: Decimal
    updated_at: Optional[datetime]

class OpenTxIn(BaseModel):
    amount: Decimal
    ttl_seconds: Optional[int] = 3600
    owner_service: str

class OpenTxOut(BaseModel):
    tx_id: UUID
    expires_at: Optional[datetime]
