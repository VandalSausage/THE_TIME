Feature: Calculating the actual time

    Scenario Outline: After hours error
      Given the timestamp <timestamp>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |timestamp | error                      |
      |"28:30:00"| 'This is not a valid time' |
      |"17:00:00"| 'This is not a valid time' |
      |"21:45:00"| 'This is not a valid time' |

    Scenario Outline: weekend error
      Given the decimal representation of the time <decimal>
      When the input is not valid
      Then the error message '<error>' is shown

      Examples:
      |decimal | error                      |
      |28      | 'This is not a valid time' |
      |-1      | 'This is not a valid time' |
      |200000  | 'This is not a valid time' |
