class Language:
    def __init__(self, language, version, base_image, compile_command, execute_command):
        self.language = language
        self.version = version
        self.base_image = base_image
        self.compile_command = compile_command
        self.execute_command = execute_command
