Feature: Work week data

    Scenario: Calculate actual day
        Given the input
        When the actual day is calculated
        Then the output is as expected

    Scenario Outline: Invalid data
        Given the input <work_week>
        When the data is not valid
        Then the error message '<error>' is shown

        Examples:
        |work_week   | error                                 |
        | placeholder| 'Something wrong with your work week' |
