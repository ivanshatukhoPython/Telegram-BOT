import command_system


def info(step, *args, **kwargs):
    message = ""
    for c in command_system.command_list:
        message += c.keys[0] + " - " + c.description + "\n"
    return (message, [], [], []), step


info_command = command_system.Command()

info_command.keys = ["/help", "help"]
info_command.description = "List of commands"
info_command.process = info
