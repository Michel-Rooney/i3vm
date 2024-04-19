#!/bin/bash

# Função para mover o mouse
move_mouse() {
	xdotool mousemove_relative --sync -- $1 $2
}

# Função para clicar com o botão esquerdo do mouse
left_click() {
	xdotool click 1
}

# Função para clicar com o botão direito do mouse
right_click() {
	xdotool click 3
}

# Verificar os argumentos fornecidos
case "$1" in
"up")
	move_mouse 0 -50
	;;
"down")
	move_mouse 0 50
	;;
"left")
	move_mouse -50 0
	;;
"right")
	move_mouse 50 0
	;;
"click")
	left_click
	;;
"rightclick")
	right_click
	;;
"up-slow")
	move_mouse 0 -10
	;;
"down-slow")
	move_mouse 0 10
	;;
"left-slow")
	move_mouse -10 0
	;;
"right-slow")
	move_mouse 10 0
	;;
*)
	echo "Usage: $0 {up|down|left|right|click|rightclick}"
	exit 1
	;;
esac

exit 0
