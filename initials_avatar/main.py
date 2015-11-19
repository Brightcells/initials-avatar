#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2015 HQM <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import time

from cStringIO import StringIO
from decimal import Decimal
from hash_ring import HashRing
try:
    from PIL import Image, ImageFont, ImageDraw
except ImportError:
    import Image, ImageFont, ImageDraw


class InitialsAvatar(object):
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.SRC_DIR = os.path.join(self.BASE_DIR, 'resource')
        self.FONT_DIR = os.path.join(self.SRC_DIR, 'fonts')
        self.TEMP_PATH = '/tmp/'
        self.DEFAULT_FONT_COLOR = '#fff'
        self.DEFAULT_BACKGROUND = (69, 189, 243, 255)
        self.HashRing = HashRing([
            (69, 189, 243, 255),
            (224, 143, 112, 255),
            (77, 182, 172, 255),
            (149, 117, 205, 255),
            (176, 133, 94, 255),
            (240, 98, 146, 255),
            (163, 211, 108, 255),
            (121, 134, 203, 255),
            (241, 185, 29, 255)
        ])
        self.SVG = u"""
        <svg xmlns="http://www.w3.org/2000/svg" width="{size}px" height="{size}px" style="border-radius:{radius}px;border-top-left-radius:{radius}px;border-top-right-radius:{radius}px;border-bottom-right-radius:{radius}px;border-bottom-left-radius:{radius}px">
            <g>
                <rect x="0" y="0" fill="{backgroud}" width="{size}px" height="{size}px">
                </rect>
                <text y="50%" x="50%" fill="{color}" text-anchor="middle" dominant-baseline="central" style="font-family: {font_family}; font-size: {font_size}px">
                  {initial}
                </text>
            </g>
        </svg>
        """

    def initial(self, text):
        """
        Get the Initial from the text
        :param text:
        :return:
        """
        text = text.strip()
        return text[0] if text else None

    def background(self, initial):
        return self.HashRing.get_node(initial.encode('unicode_escape')) or self.DEFAULT_BACKGROUND

    def filename(self, path, name, fmt):
        return u'{path}{name}.{fmt}'.format(path=path or self.TEMP_PATH, name=name or time.time(), fmt=fmt)

    def corner(self, im, radius):
        """
        Add Corners for Image
        See http://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
        :param im:
        :param radius:
        :return:
        """
        # Draws a circle with radius, using draw.ellipse()
        circle = Image.new('L', (radius * 2, radius * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

        # Create an image for the alpha channel the same size as your image
        alpha = Image.new('L', im.size, 255)

        # Chop our circle into four pieces (the rounded corners)
        # and place them in the correct corners of the alpha image
        w, h = im.size
        alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
        alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
        alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
        alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))

        # Put the alpha channel into your image using putalpha()
        im.putalpha(alpha)
        return im

    def image(self, text, size=48, circle=False, radius=0, font='simsun.ttc', color=None, background=None):
        initial = self.initial(text)

        # Get Consistent Hashing Background if Parm Backgroud is None
        # hash_ring.get_node doesn't Support Unicode
        # UnicodeEncodeError: 'ascii' codec can't encode character u'\u9ec4' in position 0: ordinal not in range(128)
        # So do unicode_escape by initial.encode('unicode_escape')
        background = background or self.background(initial)
        im = Image.new('RGBA', (size, size), background)

        if not text:
            return 'blank', im

        # Use ImageFont.truetype method to create a font object for a font of the calculated size
        draw = ImageDraw.Draw(im)
        font_size = int(size * 0.7)
        font_file = font if os.path.exists(font) else os.path.join(self.FONT_DIR, font)
        font = ImageFont.truetype(font_file, font_size)

        # Use Draw.textsize method to calculate text size to draw text center-middle-align
        # See http://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        # See http://effbot.org/imagingbook/imagedraw.htm#tag-ImageDraw.Draw.textsize
        w, h = draw.textsize(initial, font=font)
        draw.text(((size - w) / 2.0, (size - h) / 2.0), initial, fill=color or self.DEFAULT_FONT_COLOR, font=font)

        # Set radius as half of size if circle is True
        # Call corner to add corner if radius isn't zero
        radius = Decimal(size / 2.0) if circle else radius
        if radius:
            im = self.corner(im, radius)

        return initial, im

    def avatar(self, text, size=48, circle=False, radius=0, font='simsun.ttc', fmt='png', quality=100, color=None, background=None, path=None, name=None):
        """
        Get Initial Avatar
        :param text:
        :param size:
        :param font:
        :param fmt:
        :param color:
        :param background:
        :param path: With trailing slash!
        :param name:
        :return:
        """
        initial, im = self.image(text, size=size, font=font, circle=circle, radius=radius, color=color, background=background)
        filename = self.filename(path, name, fmt)
        im.save(filename, format=fmt, optimize=True, quality=quality)
        return filename

    def bytes(self, text, size=48, circle=False, radius=0, font='simsun.ttc', fmt='png', quality=100, color=None, background=None):
        """
        Get Initial Bytes
        :param text:
        :param size:
        :param font:
        :param fmt:
        :param color:
        :param background:
        :return:
        """
        initial, im = self.image(text, size=size, font=font, circle=circle, radius=radius, color=color, background=background)
        out = StringIO()
        im.save(out, format=fmt, optimize=True, quality=quality)
        return out.getvalue()

    def svg(self, text, size=48, circle=False, radius=0, font_family='simsun', font_size=None, color=None, background=None, path=None, name=None):
        """
        GET SVG Avatar
        :param text:
        :param size:
        :param circle:
        :param radius:
        :param font_family:
        :param font_size:
        :param color:
        :param background:
        :param path: With trailing slash!
        :param name:
        :return:
        """
        initial = self.initial(text)
        radius = 99999 if circle else radius
        background = background or 'rgba{rgba}'.format(rgba=self.background(initial))
        font_size = font_size or int(size * 0.7)
        svg = self.SVG.format(size=size, radius=radius, backgroud=background, color=color or self.DEFAULT_FONT_COLOR, font_family=font_family, font_size=font_size, initial=initial)
        filename = self.filename(path, name, 'svg')
        with open(filename, 'w') as f:
            f.write(svg.encode('utf8'))
        return filename


# For backwards compatibility
_global_instance = InitialsAvatar()
avatar = _global_instance.avatar
bytes = _global_instance.bytes
svg = _global_instance.svg
