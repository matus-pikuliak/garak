#!/usr/bin/env python3
"""Do LLMs with certain personas perform worse at quiz questions?"""

from typing import List
from garak.attempt import Attempt
from garak.detectors.base import Detector


class CorrectAnswer(Detector):
    """Checks the correct answer for the question."""

    bcp47 = "en"

    def detect(self, attempt: Attempt) -> List[float]:
        answer_str = ["(a)", "(b)", "(c)", "(d)"][attempt.notes["correct_answer"]]

        return [
            float(answer_str in output)
            for output in attempt.outputs
        ]
