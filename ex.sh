#/bin/bash
thelist=$(<mylist)
thechoice=$(yad --title="Choose a value" --width=200 --height=200 --list --column="Values" --separator="" $thelist)
exit $(yad --title="You chose..." --text=$thechoice)
