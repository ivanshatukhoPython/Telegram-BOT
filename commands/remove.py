import command_system


def remove(step, *args, **kwargs):
    message = "Not working right now ..."
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/remove"]
info_command.description = "Remove an account."
info_command.process = remove
