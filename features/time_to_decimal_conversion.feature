Feature: decimal time and timestamp conversions

    @data
    Scenario Outline: decimal time to timestamp
        Given the timestamp <timestamp>
        When the input is valid
        Then it is converted to a decimal representation of the time <decimal>

        Examples:
        |timestamp| decimal |
        |08:30:00 | 8.5     |
        |17:00:00 | 17      |
        |21:45:00 | 21.75   |

    @data
    Scenario Outline: timestamp to decimal time
        Given the decimal representation of the time <decimal>
        When the input is valid
        Then it is converted to a timestamp <timestamp>

        Examples:
        |timestamp| decimal |
        |08:30:00 | 8.5     |
        |17:00:00 | 17      |
        |21:45:00 | 21.75   |

    @error
    Scenario Outline: invalid timestamp
      Given the timestamp <timestamp>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |timestamp  |error                                |
      |28:30:00   |ERROR: timestamp supplied is not valid|
      |17:00:80   |ERROR: timestamp supplied is not valid|
      |21:65:00   |ERROR: timestamp supplied is not valid|
      |21:45:000  |ERROR: timestamp supplied is not valid|
      |021:00:00  |ERROR: timestamp supplied is not valid|
      |21:43:45:00|ERROR: timestamp supplied is not valid|

    @error
    Scenario Outline: invalid decimal time
      Given the decimal representation of the time <decimal>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |decimal |error                                   |
      |28      |ERROR: decimal time supplied is not valid|
      |-1      |ERROR: decimal time supplied is not valid|
      |200000  |ERROR: decimal time supplied is not valid|
