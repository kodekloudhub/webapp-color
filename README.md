# Webapp Color

## Description

This is a Flask webapp that displays the name of the kubernetes pod that it runs on. The backgroud supports several background colors in order to make them stand out, easily.

## Colors
A color can be specified in two ways: as a command line argument with the `--color` parameter or as the enviroment variable `APP_COLOR`. 

The `--color` parameter precedes the enviroment variable `APP_COLOR`.

By default, the app will run choosing one of the supported colors, if none is given.

The following list of colors are supported
| VAR | COLOR  |
|-----|-------:|
| red | #e74c3c |
| green | #16a085 |
| blue | #2980b9 |
| blue2 | #30336b |
| pink | #be2edd |
| darkblue | #130f40 |
