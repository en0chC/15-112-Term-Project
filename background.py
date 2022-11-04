#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : November 4th 2022
#------------------------------------------------------------------------------
"""
This module contains the background class which handles the background in
levels.
"""
#------------------------------------------------------------------------------
import pygame

class Background:
    def __init__(self, game, backgroundFile):
        self.image = pygame.image.load(backgroundFile)
        self.rect = self.image.get_rect()