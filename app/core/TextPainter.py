import pygame
import pygame.font
from pygame.font import Font
from pygame import Color, Surface
from core.Globals import TerminalSize, ScreenSize, CellSize, TextAntialiasing
from core.DebugProcessor import DateTime

import OpenGL.GL as gl
import OpenGL.GLU as glut

class TextPainter:
    def get_chunks(self, src, size):
        text = src[:]
        while len(text) > 0:
            text_chunk = text[:size]
            yield text_chunk
            text = text[len(text_chunk):]

    def paint(self, text: str, surface: Surface, font: Font) -> None:
        glut.gluOrtho2D(0, ScreenSize[0], 0, ScreenSize[1])
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glPushMatrix()
        gl.glLoadIdentity()
        gl.glDisable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        # blit_list = []
        top: int = 0
        for line in [x if x else [] for x in text.split("|")]:
            if top + 1 > TerminalSize[1]:
                top = 0
            left: int = 0
            for ch in self.get_chunks(line, TerminalSize[0]):
                if left + len(ch) > TerminalSize[0]:
                    left = 0
                    top += 1
                text_surface: Surface = font.render(ch, True, (255, 255, 255, 255)).convert_alpha()
                text_data = pygame.image.tostring(text_surface, "RGBA", True)
                gl.glWindowPos2d(left * CellSize[0], (TerminalSize[1] - top - 1) * CellSize[1])
                gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
                gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, text_surface.get_width(), text_surface.get_height(), 0, gl.GL_BGRA, gl.GL_UNSIGNED_BYTE, text_data)
                x = left * CellSize[0]
                y = (TerminalSize[1] - top - 1) * CellSize[1]
                gl.glBegin(gl.GL_QUADS)
                gl.glTexCoord2f(0, 0)
                gl.glVertex2f(x, y)
                gl.glTexCoord2f(1,0)
                gl.glVertex2f(x + text_surface.get_width(), y)
                gl.glTexCoord2f(1,1)
                gl.glVertex2f(x + text_surface.get_width(), y + text_surface.get_height())
                gl.glTexCoord2f(0,1)
                gl.glVertex2f(x, y + text_surface.get_height())
                gl.glEnd()
                left += len(ch)
            top += 1

        gl.glDisable(gl.GL_BLEND)
        gl.glDisable(gl.GL_TEXTURE_2D)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glPopMatrix()
