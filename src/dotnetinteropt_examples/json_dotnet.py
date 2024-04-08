from dotnetinteropt import load

load("dotnetinteropt_examples")  # package where to find the dlls

from Newtonsoft.Json import Formatting
from Newtonsoft.Json import JsonConvert
from System import *
from System.Collections.Generic import Dictionary


def main():
    points = Dictionary[String, Int32]()
    points.Add("James", 9001)
    points.Add("Jo", 3474)
    points.Add("Jess", 11926)

    json = JsonConvert.SerializeObject(points, Formatting.Indented)

    Console.WriteLine(json)


if __name__ == "__main__":
    main()
