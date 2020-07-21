# Badges

![Image of dancing fuzzball](docs/A-GrumpyFuzzball-Dance.gif)

SIPB Badges Project for fun achievements.

## Installing

The project uses old versions of Python, pip, and Django that is used by SIPB
Scripts service. Required packages are listed in `requirements.txt` To avoid version
conflicts and make development easier, usage of `virtualenv` is recommended. In the 
repo's root folder, run the following commands if `virtualenv` is installed.

```
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

The first line tells `virtualenv` to create a new virtual environment and store
required binaries and scripts in `venv`. The second line activates the environment.
In this environment, your `pip install` will only affect this environment not your
own installation of Python. The last line installs all requirements listed in the
file `requirements.txt`.

You are now ready to develop. Have fun!

## Contributing

The project is under heavy construction. If you want to know more about the
project, contact any of the maintainers. If you're a new maintainer for the
project, consider checking out the [wiki](https://github.com/sipb/Badges/wiki).

## License

[GPL v3](LICENSE)

## Maintainers:
- jnoguera ('23)
- sabina22 ('22)
- rihn | rihn [at] mit [dot] edu
- Michael Gilbert ('22) | <gilbertm@mit.edu>
- fionalin ('23)
