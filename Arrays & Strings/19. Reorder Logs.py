class Solution:
    """
        To illustrate the idea, let us first define a Student object as follows, which has three properties: name, grade, age.

            class Student:
                def __init__(self, name, grade, age):
                    self.name = name
                    self.grade = grade
                    self.age = age

            student_objects = [
                Student('john', 'A', 15),
                Student('jane', 'B', 12),
                Student('dave', 'B', 10),
            ]
    """
    def reorderLogFiles(self, logs):

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorderLogFiles(logs))
