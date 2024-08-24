from datetime import date, datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

# Nome;
#  CPF;
#  Data de nascimento;
#  E-mail.


@table_registry.mapped_as_dataclass
class Cliente:
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    cpf: Mapped[str] = mapped_column(unique=True)
    data_nasc: Mapped[date]
    email: Mapped[str] = mapped_column(unique=True)
    update_at: Mapped[datetime] = mapped_column(
        init=False, server_default=None, nullable=True, onupdate=func.now()
    )
