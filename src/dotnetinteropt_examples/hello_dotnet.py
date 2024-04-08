from dotnetinteropt import load

load("dotnetinteropt_examples")  # package where to find the dlls

from System import Console


def main():
    Console.WriteLine("Hello from .NET!")


if __name__ == "__main__":
    main()
