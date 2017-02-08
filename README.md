# Probability_calculator
A way of calculating statistic probabilities. This has been custom built to suit problems with TSP

===============================================================================================================================
Usage:

1) Open a terminal window (Mac or Linux) or a Command prompt window (Windows)

2) Navigate to the Downloads folder where the calculator is. Use ls (Mac or Linux) or dir (Windows) to see your directories, and cd to change directory (OS independent)

3) Type "python Probability_calculator.py {function name}" where you replace {function name} with one of the listed functions
===============================================================================================================================

*******************************************************************************************************************************
Function list:
-------------------------------------------------------------------------------------------------------------------------------
total_outcomes

Takes the arguments sing_event, tot_events
Returns the total number of outcomes. For example rolling a fair 6 sided dice 50 times. Number of outcomes for one
event would be 6 (sing_event), and the total number of events is 50 (tot_events).
-------------------------------------------------------------------------------------------------------------------------------
chose

Takes arguements tot_events, wanted_outcomes
Returns the number of wanted outcomes. For example flipping a fair coin 50 times. How many ways can you get
25 heads? In this case the events would be 50 (tot_events) and the outcomes would be 25 (wanted_outcomes).
-------------------------------------------------------------------------------------------------------------------------------
probability_of_event

Takes arguments tot_events, wanted_outcomes, sing_events
Returns the probability of a certain event happening. For example flipping a fair coin 50 times. The probability of
getting exactly 25 heads then the number of events is 50 (tot_events), the number of wanted outcomes is 25
(wanted_outcomes), and the number of outcomes for a single event is 2, heads or tails (sing_events).
-------------------------------------------------------------------------------------------------------------------------------
*******************************************************************************************************************************
