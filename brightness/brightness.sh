#!/bin/bash

case "$1" in
"incress")
	sudo brightnessctl set +5%
	;;
"decress")
	sudo brightnessctl set 5%-
	;;
*)
	echo "Usage: $0 {incress|decress}"
	;;
esac

exit 0
