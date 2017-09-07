# -*- coding: utf-8 -*-
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
import numpy as np
import wx
import  wx.lib.mixins.listctrl  as  listmix
import os
import io
import sys


class MainWindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Estadistica del kit de Rayos Cosmicos',size=(1600,700))
        panel=wx.Panel(self)
        wx.Frame.CenterOnScreen(self)

        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        file_menu=wx.Menu()
        edit_menu=wx.Menu()

        ID_FILE_NEW = 1
        ID_FILE_OPEN = 2

        ID_EDIT_UNDO = 3
        ID_EDIT_REDO = 4
        
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        
        file_menu.Append(ID_FILE_NEW,"New Window","This is a new window")
        file_menu.Append(ID_FILE_OPEN,"Open...","This will open a new window")

        edit_menu.Append(ID_EDIT_UNDO,"Undo","This will undo your last action")
        edit_menu.Append(ID_EDIT_REDO,"Redo","This will redo your last undo")
        self.titulo=wx.StaticText(self, label="Estadistica del kit de Rayos Cosmicos", pos=(220, 30))

        menubar.Append(file_menu,"File")
        menubar.Append(edit_menu,"Edit")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.test, None, 1)

    def draw(self):
        
        fil=file("C:\Users\Guillermo1\Documents\Strangeness\IPython\Voz.txt",'r')
        arr=fil.readlines()
        arr=[float(i.strip()) for i in arr]
        arr2=arr[:20]
        P=[]
        #print "Lista de números"
        #print str(arr2)+'\n'
        for i in range(5):
            for j in range(5):
                if j==4:
                    P.append((arr2[i*4+j-4]+arr2[i*4+j-3]+arr2[i*4+j-2]+arr2[i*4+j-1])/4.)
                    continue

        fil.close()
        cu=np.arange(len(P))
        self.axes.plot(P,cu)

    def test(self, event):
        self.new = NewWindow(parent=None, id=-1)
        self.new.Show()

class NewWindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'New Window', size=(400,300))
        wx.Frame.CenterOnScreen(self)
        #self.new.Show(False)

if __name__=='__main__':
        app=wx.PySimpleApp()
        frame=MainWindow(parent=None,id=-1)
        frame.draw()
        frame.Show()

        app.MainLoop()