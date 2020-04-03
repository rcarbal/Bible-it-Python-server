from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class QuestionMatcher:

    def get_question_score(self, questions_array, user_string):

        # get ratio for array
        score = process.extract(user_string, questions_array)
        return score

    def get_best_question_score(self, questions_array, user_string):

        for question in questions_array:
            score = fuzz.ratio(question[0], user_string)

            if score == 100:
                return question
