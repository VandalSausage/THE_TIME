Feature: Work week data

    @error
    Scenario Outline: Invalid data
        Given an invalid work week <work_week>
        Then the error message '<error>' is shown

        Examples:
        |work_week| error                             |
        |1        |Something wrong with your work week|
        |2        |Something wrong with your work week|
