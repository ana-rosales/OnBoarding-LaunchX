def main():
    try:
        configuration = open('config.txt')
    # error "no se encuentra"
    except FileNotFoundError:
        print("Couldn't find de config.txt file!")
    # otro error
    except PermissionError:
        print("Found config.txt but permission to read it is denied.")
    # agrupar
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()