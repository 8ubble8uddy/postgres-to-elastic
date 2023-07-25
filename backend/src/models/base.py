from uuid import UUID

from pydantic import BaseModel


class UUIDMixin(BaseModel):
    """Миксин для хранения первичных ключей."""

    id: UUID
