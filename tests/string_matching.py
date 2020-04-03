import unittest
from constants.answered_questions import ANSWERED_QUESTION
from utilities.question_matcher import QuestionMatcher


class TestStringMatching(unittest.TestCase):

    def test_get_string_matching_score(self):
        array_that_holds_question = []

        # get questions into array
        for json_question in ANSWERED_QUESTION:
            array_that_holds_question.append(json_question['question'])

        # string to compare
        string_to_compare = 'how many genders'

        # get best matching string
        matcher = QuestionMatcher()
        best_matched_string = matcher.get_question_score(questions_array=array_that_holds_question,
                                                         user_string=string_to_compare)

        self.assertTrue(len(best_matched_string) == 5)


