from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class QuestionMatcher:

    def get_question_score(self, questions_array, user_string):

        # get ratio for array
        score = process.extract(user_string, questions_array)
        print(score)
        return score
