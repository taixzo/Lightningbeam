#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2012 Skyler Lehmkuhl
# Released under the GPLv3. For more information, see gpl.txt.

def colorArray(i):
    return [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0.2,0.2,0.2],[0.4,0.4,0.4],[0.6,0.6,0.6],[0.8,0.8,0.8],[1,1,1],[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1]], [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0.2],[0,0,0.4],[0,0,0.6],[0,0,0.8],[0,0,1],[0.6,0,0],[0.6,0,0.2],[0.6,0,0.4],[0.6,0,0.6],[0.6,0,0.8],[0.6,0,1]],[[0,0.2,0],[0,0.2,0.2],[0,0.2,0.4],[0,0.2,0.6],[0,0.2,0.8],[0,0.2,1],[0.6,0.2,0],[0.6,0.2,0.2],[0.6,0.2,0.4],[0.6,0.2,0.6],[0.6,0.2,0.8],[0.6,0.2,1]],[[0,0.4,0],[0,0.4,0.2],[0,0.4,0.4],[0,0.4,0.6],[0,0.4,0.8],[0,0.4,1],[0.6,0.4,0],[0.6,0.4,0.2],[0.6,0.4,0.4],[0.6,0.4,0.6],[0.6,0.4,0.8],[0.6,0.4,1]],[[0,0.6,0],[0,0.6,0.2],[0,0.6,0.4],[0,0.6,0.6],[0,0.6,0.8],[0,0.6,1],[0.6,0.6,0],[0.6,0.6,0.2],[0.6,0.6,0.4],[0.6,0.6,0.6],[0.6,0.6,0.8],[0.6,0.6,1]],[[0,0.8,0],[0,0.8,0.2],[0,0.8,0.4],[0,0.8,0.6],[0,0.8,0.8],[0,0.8,1],[0.6,0.8,0],[0.6,0.8,0.2],[0.6,0.8,0.4],[0.6,0.8,0.6],[0.6,0.8,0.8],[0.6,0.8,1]],[[0,1,0],[0,1,0.2],[0,1,0.4],[0,1,0.6],[0,1,0.8],[0,1,1],[0.6,1,0],[0.6,1,0.2],[0.6,1,0.4],[0.6,1,0.6],[0.6,1,0.8],[0.6,1,1]],[[0.2,0,0],[0.2,0,0.2],[0.2,0,0.4],[0.2,0,0.6],[0.2,0,0.8],[0.2,0,1],[0.8,0,0],[0.8,0,0.2],[0.8,0,0.4],[0.8,0,0.6],[0.8,0,0.8],[0.8,0,1]],[[0.2,0.2,0],[0.2,0.2,0.2],[0.2,0.2,0.4],[0.2,0.2,0.6],[0.2,0.2,0.8],[0.2,0.2,1],[0.8,0.2,0],[0.8,0.2,0.2],[0.8,0.2,0.4],[0.8,0.2,0.6],[0.8,0.2,0.8],[0.8,0.2,1]],[[0.2,0.4,0],[0.2,0.4,0.2],[0.2,0.4,0.4],[0.2,0.4,0.6],[0.2,0.4,0.8],[0.2,0.4,1],[0.8,0.4,0],[0.8,0.4,0.2],[0.8,0.4,0.4],[0.8,0.4,0.6],[0.8,0.4,0.8],[0.8,0.4,1]],[[0.2,0.6,0],[0.2,0.6,0.2],[0.2,0.6,0.4],[0.2,0.6,0.6],[0.2,0.6,0.8],[0.2,0.6,1],[0.8,0.6,0],[0.8,0.6,0.2],[0.8,0.6,0.4],[0.8,0.6,0.6],[0.8,0.6,0.8],[0.8,0.6,1]],[[0.2,0.8,0],[0.2,0.8,0.2],[0.2,0.8,0.4],[0.2,0.8,0.6],[0.2,0.8,0.8],[0.2,0.8,1],[0.8,0.8,0],[0.8,0.8,0.2],[0.8,0.8,0.4],[0.8,0.8,0.6],[0.8,0.8,0.8],[0.8,0.8,1]],[[0.2,1,0],[0.2,1,0.2],[0.2,1,0.4],[0.2,1,0.6],[0.2,1,0.8],[0.2,1,1],[0.8,1,0],[0.8,1,0.2],[0.8,1,0.4],[0.8,1,0.6],[0.8,1,0.8],[0.8,1,1]],[[0.4,0,0],[0.4,0,0.2],[0.4,0,0.4],[0.4,0,0.6],[0.4,0,0.8],[0.4,0,1],[1,0,0],[1,0,0.2],[1,0,0.4],[1,0,0.6],[1,0,0.8],[1,0,1]],[[0.4,0.2,0],[0.4,0.2,0.2],[0.4,0.2,0.4],[0.4,0.2,0.6],[0.4,0.2,0.8],[0.4,0.2,1],[1,0.2,0],[1,0.2,0.2],[1,0.2,0.4],[1,0.2,0.6],[1,0.2,0.8],[1,0.2,1]],[[0.4,0.4,0],[0.4,0.4,0.2],[0.4,0.4,0.4],[0.4,0.4,0.6],[0.4,0.4,0.8],[0.4,0.4,1],[1,0.4,0],[1,0.4,0.2],[1,0.4,0.4],[1,0.4,0.6],[1,0.4,0.8],[1,0.4,1]],[[0.4,0.6,0],[0.4,0.6,0.2],[0.4,0.6,0.4],[0.4,0.6,0.6],[0.4,0.6,0.8],[0.4,0.6,1],[1,0.6,0],[1,0.6,0.2],[1,0.6,0.4],[1,0.6,0.6],[1,0.6,0.8],[1,0.6,1]],[[0.4,0.8,0],[0.4,0.8,0.2],[0.4,0.8,0.4],[0.4,0.8,0.6],[0.4,0.8,0.8],[0.4,0.8,1],[1,0.8,0],[1,0.8,0.2],[1,0.8,0.4],[1,0.8,0.6],[1,0.8,0.8],[1,0.8,1]],[[0.4,1,0],[0.4,1,0.2],[0.4,1,0.4],[0.4,1,0.6],[0.4,1,0.8],[0.4,1,1],[1,1,0],[1,1,0.2],[1,1,0.4],[1,1,0.6],[1,1,0.8],[1,1,1]]][i]
