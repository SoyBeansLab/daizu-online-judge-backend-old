from datetime import datetime


class Language:
    def __init__(
        self,
        language: str,
        version: str,
        base_image: str,
        compile_command: str,
        execute_command: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.language = language
        self.version = version
        self.base_image = base_image
        self.compile_command = compile_command
        self.execute_command = execute_command
        self.created_at = created_at
        self.updated_at = updated_at
