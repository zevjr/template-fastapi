"""
# Modulo de Excessões
Item usado para disponibilizar as excessões personalizadas da aplicação.
"""

from .crud_error import (
    CRUDCreateError,  
    CRUDDeleteError,  
    CRUDSelectError,  
    CRUDUpdateError,  
)

__all__ = [
    "CRUDCreateError",
    "CRUDUpdateError",
    "CRUDDeleteError",
    "CRUDSelectError",
]
