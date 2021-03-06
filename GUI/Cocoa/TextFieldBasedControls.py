#
#   Python GUI - PyObjC
#
#   Base class for controls based on an NSTextField
#

from Foundation import NSRect, NSPoint, NSSize
from AppKit import NSTextField, NSSecureTextField, NSTextFieldCell
from GUI.Utils import NSMultiClass
from GUI import Color
from GUI.Utils import ns_size_to_fit, PyGUI_NS_EventHandler
from GUI.StdFonts import system_font

class TextFieldBasedControl(object):

    _ns_handle_mouse = True

    def _create_ns_textfield(self, editable, text, font,
            multiline = False, password = False, border = False,
            padding = (0, 0)):
        self._ns_is_password = password
        if password:
            ns_class = PyGUI_NSSecureTextField
        else:
            ns_class = PyGUI_NSTextField
        ns_frame = NSRect(NSPoint(0, 0), NSSize(20, 10))
        ns_textfield = ns_class.alloc().initWithFrame_(ns_frame)
        ns_textfield.pygui_component = self
        if multiline and not password:
            ns_textfield.pygui_multiline = True
        # Be careful here -- calling setBordered_ seems to affect isBezeled as well
        if editable:
            ns_textfield.setBezeled_(border)
        else:
            ns_textfield.setBordered_(border)
        if not editable:
            ns_textfield.setDrawsBackground_(False)
        ns_textfield.setEditable_(editable)
        ns_textfield.setSelectable_(editable)
        ns_textfield.setFont_(font._ns_font)
        ns_textfield.setStringValue_(text)
        ns_size_to_fit(ns_textfield, padding = padding)
        return ns_textfield
    
    def get_border(self):
        ns_textfield = self._ns_inner_view
        if ns_textfield.isEditable():
            return ns_textfield.isBezeled()
        else:
            return ns_textfield.isBordered()
    
    def set_border(self, border):
        ns_textfield = self._ns_inner_view
        if ns_textfield.isEditable():
            ns_textfield.setBezeled_(border)
        else:
            ns_textfield.setBordered_(border)

    def get_text(self):
        return self._ns_inner_view.stringValue()
    
    def set_text(self, v):
        self._ns_inner_view.setStringValue_(v)

    def get_color(self):
        return Color._from_ns_color(self._ns_inner_view.textColor())
    
    def set_color(self, v):
        self._ns_inner_view.setTextColor_(v._ns_color)
    
    def _get_vertical_padding(self):
        if self.border:
            return 5
        else:
            return 0
    
    _vertical_padding = property(_get_vertical_padding)

#------------------------------------------------------------------------------

class PyGUI_NSTextField(NSTextField): #, PyGUI_NS_EventHandler):
    __metaclass__ = NSMultiClass

    pygui_multiline = False

class PyGUI_NSSecureTextField(NSSecureTextField): #, PyGUI_NS_EventHandler):
    __metaclass__ = NSMultiClass

    pygui_multiline = False

