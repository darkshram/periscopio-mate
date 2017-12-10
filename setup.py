from setuptools import setup

PACKAGE = 'periscopio'

setup(name = PACKAGE,
      version = '1.18.0',
      license = "GNU LGPL",
      description = "Python module to download subtitles for a given video file",
      author = "Joel Barrios",
      author_email = "pdarkshram@gmail.com",
      url = "https://github.com/darkshram/periscope/",
      packages= [ "periscopio", "periscopio/plugins" ],
      py_modules=["periscopio"],
      scripts = [ "bin/periscopio" ],
      install_requires = ["BeautifulSoup >= 3.2.0"]
      )
