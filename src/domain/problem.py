class Problem:
    def __init__(
            self,
            contest_id: str,
            problem_id: str,
            problem_name: str,
            problem_text: str,
            problem_constraint: str,
            time_limit: int,
            memory_limit: int,
            input_format: str,
            input_example: str,
            output_example: str,
            output_format: str,
            input_comment=None,
            output_comment=None,
        ):

        self.contest_id = contest_id
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.problem_text = problem_text
        self.problem_constraint = problem_constraint

        self.time_limit = time_limit
        self.memory_limit = memory_limit

        self.input_format = input_format
        self.input_example = input_example
        self.input_comment = input_comment

        self.output_format = output_format
        self.output_example = output_example
        self.output_comment = output_comment
