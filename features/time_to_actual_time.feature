Feature: Calculating the actual time

    @comparison
    Scenario: Truman and Aisha time comparisons
      Given the timestamp <timestamp> and day <day>
      When you request the actual time from aisha
      and you request the actual time from truman
      Then the two actual times are equal

    Scenario Outline: get the actual time from truman
      Given the timestamp <timestamp> and day <day>
      When you request the actual time from truman
      Then the actual time is <actual_time>

      Examples:
      |timestamp|day    |actual_time |
      |17:30:00 |Friday |17:30       |
      |09:00:00 |Monday |09:00       |

    Scenario Outline: get the actual time from aisha
      Given the timestamp <timestamp> and day <day>
      When you request the actual time from aisha
      Then the actual time is <actual_time>

      Examples:
      |timestamp|day    |actual_time |
      |17:30:00 |Friday |17:30       |
      |09:00:00 |Monday |09:00       |

    @error
    Scenario Outline: check errors truman
      Given the timestamp <timestamp> and day <day>
      When you request the actual time from truman
      Then the error message '<error>' is shown

      Examples:
      |timestamp|day     |error                                                |
      |21:00:00 |Monday  |You are off the clock right now - get it together    |
      |12:00:00 |Saturday|Why are you checking this on the weekend, you maniac?|

    @error
    Scenario Outline: check errors aisha
      Given the timestamp <timestamp> and day <day>
      When you request the actual time from aisha
      Then the error message '<error>' is shown

      Examples:
      |timestamp|day     |error                                                |
      |21:00:00 |Monday  |You are off the clock right now - get it together    |
      |12:00:00 |Saturday|Why are you checking this on the weekend, you maniac?|
