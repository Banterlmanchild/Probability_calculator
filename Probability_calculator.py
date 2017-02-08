#! /usr/bin/env python2.7
from numpy import abs

__author__ = "Adam Richardson"
__date__ = '08/02/17'


class Factorial:
    def __init__(self, n):
        self.n = n
        if self.n < 0.0:
            raise ValueError("Cannot have a negative factorial")
        elif self.n != int(self.n):
            raise ValueError("Cannot have non-integer factorial")

    def factorial(self):
        if self.n == 0.0:
            return 1.0
        else:
            return self.n * Factorial(self.n - 1.0).factorial()


"""Returns the total number of outcomes. For example rolling a fair 6 sided dice 50 times. Number of outcomes for one
event would be 6 (event_outcomes), and the total number of events is 50 (total_events)."""


def total_outcomes(event_outcomes, total_events):
    return event_outcomes ** total_events


"""This returns the number of wanted outcomes. For example flipping a fair coin 50 times. How many ways can you get
25 heads? In this case the events would be 50 and the outcomes would be 25."""


def choose(events, outcomes):
    if events < outcomes:
        raise ValueError("The # of events should be bigger than the # of outcomes. Code will run anyway assuming you've"
                         "got the numbers the wrong way round")
    diff = abs(events - outcomes)
    return Factorial(events).factorial() / (Factorial(outcomes).factorial() * Factorial(diff).factorial())


"""Returns the probability of a certain event happening. For example flipping a fair coin 50 times. The probability of
getting exactly 25 heads then the number of events is 50 (tot_events), the number of wanted outcomes is 25
(tot_outcomes), and the number of outcomes for a single event is 2, heads or tails (sing_events)."""


def probability_of_event(tot_events, tot_outcomes, sing_event):
    return choose(tot_events, tot_outcomes) / total_outcomes(sing_event, tot_events)
