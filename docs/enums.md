# Enums

Enums are defined using the `#` character, before which comes the name of the enum.

Each of the enum members has to be separated with a semicolon.

By default, enum members are assigned increasing numbers, starting from 0.

You can provide your own values for enum members by simply assigning values to the names.

Enum members cannot be modified.

```sm
Shape # {
    Circle;
    Square;
}

Color # {
    Red: "#FF0000";
    Green: "#00FF00";
    Blue: "#0000FF";
}

=> * {
    Shape!;
    Shape.Circle!;
    Shape.Square!;
    Color.Red!;
}
```
```
Enum(Shape)
0
1
#FF0000
```