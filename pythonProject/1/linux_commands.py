import argparse
import os

class LinuxCommand:
    def __init__(self):
        pass

    def execute_command(self, command):
        return os.system(command)

    def move_file(self, source, destination):
        command = f"mv {source} {destination}"
        return self.execute_command(command)

    def remove_file(self, path):
        command = f"rm {path}"
        return self.execute_command(command)

    def create_file(self, filename, content=""):
        command = f"echo '{content}' > {filename}"
        return self.execute_command(command)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=[ "mv",  "rm", "echo"])
    parser.add_argument("args", nargs="*",)

    args = parser.parse_args()
    executor = LinuxCommand()


    if args.command == "mv":
        result = executor.move_file(*args.args)
    elif args.command == "rm":
        result = executor.remove_file(*args.args)
    elif args.command == "echo":
        result = executor.create_file(*args.args)
    else:
        result = "Invalid command"

    print(result)

if __name__ == "__main__":
    main()
