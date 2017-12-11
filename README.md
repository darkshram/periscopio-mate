periscopio-mate
============

A Python2 module to search and download subtitles, forked from [persicope](https://github.com/patrickdessalle/periscope) by Patrick Dessalle.

Expect some network connection warnings and errors in ~/.xsession-errors for some services if they are unreachable from your location.

Current supported services
==========================

- http://www.podnapisi.net/
- http://thesubdb.com/
- http://www.subswiki.com/
- http://www.podnapisi.net/
- http://www.subtitlesource.org/
- http://legendas.tv/ (requires username/password)
- http://www.addic7ed.com/
- http://www.opensubtitles.org/
- http://subscene.com/
- http://www.subdivx.com/
- http://subscene.com/
- http://www.tvsubtitles.net/

Installation.
============

```bash
git clone https://github.com/darkshram/periscopio-mate
cd periscopio-mate
python2 setup.py build
python2 setup.py install
install -m 0755 bin/periscopio-caja/periscopio-caja.py* \
    /usr/share/python-caja/extensions/
for n in po/*.mo ; do
        install -p -D -m0644 $n /usr/share/locale/`basename $n .mo`/LC_MESSAGES/periscopio-caja.mo
done
```

Then restart caja.

Configuration.
=============

Just edit ~/.config/periscopio/config

You will find:

```bash
[DEFAULT]
lang =
lang-in-name = no
plugins =

[LegendasTV]
user =
pass =
unrarpath =
supportedsubtitleextensions =
```
- Language is detected by default. But if you want to manually set a different one from used in the the desktop environment, then set the desired language.
- Set if you want to append the language name to the subtitle file. Default is no.
- Set if you want to use a plugin in particular. Empty means use all.
     -Addic7ed
     -LegendasTV
     -OpenSubtitles
     -Podnapisi
     -Podnapisi2
     -SubDivX
     -SubScene
     -SubsWiki
     -SubtitleDatabase
     -SubtitleSource
     -TheSubDB
     -TvSubtitles
- Set user and password for LegendasTV in case you have one account there.

Screenshots.
===========

![Caja context menu](screenshots/screenshot1.png?raw=true "Caja context menu")

![Desktop notification](screenshots/screenshot2.png?raw=true "Desktop notification")

