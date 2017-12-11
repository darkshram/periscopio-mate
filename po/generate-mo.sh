#!/bin/bash
while read lingua
do msgfmt ${lingua}.po --output-file ${lingua}.mo
done  < LINGUAS
