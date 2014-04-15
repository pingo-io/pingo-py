#! /bin/bash

cd ..
find -name '*.py' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
find -name '*.sh' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
