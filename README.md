# Avenger Code Challenge

Code Completed!


Interesting	Coding/Algo Choices -
- Just 2 dictionries(hashmaps) to store all input csv data 
  ```
  inbound = {"tcp":{"port":[],"ip":[]},
             "udp":{"port":[],"ip":[]}}
  outbound = {"tcp":{"port":[],"ip":[]},
              "udp":{"port":[],"ip":[]}
  ```
- Reflection usage to evaluate which inbound/outbound dict and respective child dict 
  ```
  To get the list of ports -
  eval(bound)[protocol]["port"] 
  ```
- Modularization to achieve code resuse.
- Ip address representation 
  ```
  192.131.21.2 -> 192131021002
  ```
- Idea was to programatically merge ranges/values for port and IP in the above dict for less storage and efficient performance.

Other Notes -
- Text formatting changes encoding/decoding not handled.


Team Preference -

    #1 DATA TEAM
    #2 PLATFORM TEAM


