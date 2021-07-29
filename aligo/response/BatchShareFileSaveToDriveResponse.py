"""批量响应"""

from dataclasses import dataclass

from aligo.types import *


@dataclass
class BatchShareFileSaveToDriveResponse(DataClass):
    """..."""
    file_id: str = None
    drive_id: str = None
    domain_id: str = None
    async_task_id: str = None
