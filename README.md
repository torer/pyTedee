# pyTedee
Simple python script to manage Tedee lock.
Tested on config with one lock and one bridge.

Copy config.py.dist and put there your login and password to your tedee account.

Simple usage:
Get attibutes:
```
 pyTedee.py --attr [attribute_name] --name [lock_name]
      attribute_name :
        - state:
          2 = open
          3 = half closed
          4 = opening
          5 = closing
          6 = closed
        - isCharging: [True|False]
        - batteryLevel: int %
      lock_name:
        Name of your lock
```
Opnening and closing:
```
  pyTedee.py --action [action_name] --name [lock_name]
    lock_name:
      - Name of your lock
    action_name:
      - open
      - close
```
Get full json for debuging and development:
```
   pyTedee.py --action showAll
     - Print full json from API
```
