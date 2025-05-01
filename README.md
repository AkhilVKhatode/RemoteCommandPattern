# TV Remote Control Command Pattern

This project demonstrates the **Command Design Pattern** by simulating a TV remote control system. The program provides a set of commands to control a TV, including turning it on, turning it off, changing channels, and adjusting the volume.

## Design Pattern: Command

The **Command Design Pattern** encapsulates a request as an object, thereby allowing for parameterization of clients with different requests. In this project, each operation on the TV (turn on, turn off, change channel, adjust volume) is encapsulated as a command object.

### Classes and Structure:
- **Command**: An interface (abstract class in Python) for all commands, with an `execute()` method.
- **TurnOnCommand**: Command to turn the TV on.
- **TurnOffCommand**: Command to turn the TV off.
- **ChangeChannelCommand**: Command to change the TV's channel.
- **AdjustVolumeCommand**: Command to adjust the TV's volume.
- **TV**: The receiver class with the methods for TV operations.
- **RemoteControl**: The invoker class, which triggers commands through buttons.

## How it works:
1. The `RemoteControl` object acts as the invoker, allowing the user to press buttons to perform actions on the TV.
2. The concrete command classes (`TurnOnCommand`, `TurnOffCommand`, `ChangeChannelCommand`, `AdjustVolumeCommand`) encapsulate the respective actions that the `TV` class can perform.
3. Commands are executed by invoking the `execute()` method, either through the `RemoteControl`'s `press_on_button()` or `press_off_button()` methods or by directly calling `execute()` on other commands.

## Usage:
Clone this repository and run the Python script to simulate a TV remote control system.

### Example:
```python
from tv_remote import TV, TurnOnCommand, TurnOffCommand, ChangeChannelCommand, AdjustVolumeCommand, RemoteControl

# Create the TV object
tv = TV()

# Create commands
turn_on = TurnOnCommand(tv)
turn_off = TurnOffCommand(tv)
change_channel = ChangeChannelCommand(tv, 5)
adjust_volume = AdjustVolumeCommand(tv, 20)

# Create remote control and set commands
remote = RemoteControl()
remote.set_on_command(turn_on)
remote.set_off_command(turn_off)

# Test the remote control
remote.press_on_button()  # Turn on the TV
remote.press_off_button()  # Turn off the TV

# Execute other commands directly
change_channel.execute()  # Change the channel to 5
adjust_volume.execute()   # Adjust the volume to 20
```
