from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command classes
class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

class ChangeChannelCommand(Command):
    def __init__(self, tv, channel):
        self.tv = tv
        self.channel = channel

    def execute(self):
        self.tv.change_channel(self.channel)

class AdjustVolumeCommand(Command):
    def __init__(self, tv, volume):
        self.tv = tv
        self.volume = volume

    def execute(self):
        self.tv.adjust_volume(self.volume)

# Receiver class (TV)
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

    def change_channel(self, channel):
        print(f"Channel changed to {channel}")

    def adjust_volume(self, volume):
        print(f"Volume set to {volume}")

# Invoker class (RemoteControl)
class RemoteControl:
    def __init__(self):
        self.on_command = None
        self.off_command = None
        self.channel_command = None
        self.volume_command = None

    def set_on_command(self, on_command):
        self.on_command = on_command

    def set_off_command(self, off_command):
        self.off_command = off_command

    def set_channel_command(self, channel_command):
        self.channel_command = channel_command

    def set_volume_command(self, volume_command):
        self.volume_command = volume_command

    def press_on_button(self):
        if self.on_command:
            self.on_command.execute()

    def press_off_button(self):
        if self.off_command:
            self.off_command.execute()

    def press_channel_button(self):
        if self.channel_command:
            self.channel_command.execute()

    def press_volume_button(self):
        if self.volume_command:
            self.volume_command.execute()

# Main code
if __name__ == "__main__":
    tv = TV()

    # Create commands
    turn_on = TurnOnCommand(tv)
    turn_off = TurnOffCommand(tv)
    change_channel = ChangeChannelCommand(tv, 5)
    adjust_volume = AdjustVolumeCommand(tv, 20)

    # Create remote control
    remote = RemoteControl()
    remote.set_on_command(turn_on)
    remote.set_off_command(turn_off)
    remote.set_channel_command(change_channel)
    remote.set_volume_command(adjust_volume)

    remote.press_on_button()  # Turn on the TV
    remote.press_off_button()  # Turn off the TV
    remote.press_channel_button()  # Change the channel
    remote.press_volume_button()  # Adjust the volume
