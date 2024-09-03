def parse_args(commmand: str) -> list[str]:
    """
    Parse command line arguments and return a dictionary of arguments.
    """
    if commmand.startswith("python"):
        args = commmand.split(sep=" ")[2:]

    else:
        args = commmand.split(sep=" ")

    return args


if __name__ == "__main__":
    command = input("Enter command: ")
    args = parse_args(command)
    print(args)