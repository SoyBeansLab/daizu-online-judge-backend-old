class Problem:
    def __init__(self, problemName: str, problemText: str, problemConstraint: str,\
                       timeLimit: int, memoryLimit: int,\
                       input: str, inputExam: str, inputComment: str,\
                       output: str, outputExam: str, outputComment: str):

        self.problemName = problemName
        self.problemText = problemText
        self.problemConstraint = problemConstraint

        self.timeLimit = timeLimit
        self.memoryLimit = memoryLimit

        self.input = input
        self.inputExam = inputExam
        self.inputComment = inputComment

        self.output = output
        self.outputExam = outputExam
        self.outputComment = outputComment

