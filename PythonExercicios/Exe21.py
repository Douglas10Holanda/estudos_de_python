# Exercicio 21 de Python - Tocando um MP3

# Faça um programa em Python que abra e reproduza o áudio de um aquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('exe21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()