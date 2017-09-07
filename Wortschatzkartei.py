# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 23:14:17 2016

@author: Juice
"""

import unicodedata as ud
from datetime import datetime
import wx
import  wx.lib.mixins.listctrl  as  listmix
import os
import io
import sys

Worten=dict()
Verben=dict()
tipo=str()

def Encuentra(Dicc,iden):
        for j,i in list(enumerate(Dicc.values())):
            if iden == i[len(i)-2]:
                return j+1

def Selecciona(Wdict,block):
    l=list()
    for item in Wdict:
        if block in Wdict[item]: l.append(item)
    return tuple(l)

def Upgrade(Wdict,pal,ren,col,pos,block):
    Not=list(Wdict[ren+1][0:len(Wdict[ren+1])-1])
    if block=="Lernblock":  Not.append("Wiederholungsblock")
    else:                   Not.append("Registerblock")
    Wdict.update({ren+1:  tuple(Not)})

def Schreibe(Wdict,pter,con):
    for i,j in list(enumerate(Wdict.values())):
        #pter.write('*')
        if i<con:   continue
        for l,k in list(enumerate(j)):
            if l<len(list(enumerate(j)))-1: pter.write(k.decode('ISO-8859-1')+u'||')
            else:                           pter.write(unicode(k)+u'\n')
"""def Suche(wort,dictB,pos):#Pos es el numero que indica en que posicion de los tuples estan las palabras
    wort=wort.encode('ISO-8859-1')
    for i in range(len(dictB)):
        if wort in dictB.values()[i]: return i , dictB.values()[i].index(wort)     #Direccion en el dict y en el tuple
    return False,False"""

class windowClass(wx.Frame):
    def __init__(self,parent,id):
            wx.Frame.__init__(self,parent,id,'Wortschatzkartei',pos=wx.DefaultPosition,size=(215,265),
                style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
            self.basicGUI()
            self.__close_callback = None
            self.Panel=wx.Panel(self)
            self.SetBackgroundColour('white')
    def basicGUI(self):
            self.CreateStatusBar()
            menuBar = wx.MenuBar()
            self.Bind(wx.EVT_CLOSE, self._when_closed)
            knopf=wx.Button(self,1,'Wort',(50,20))
            self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
            knopf.SetToolTipString("Para introducir una nueva palabra")
            knopf=wx.Button(self,2,'Verb',(50,60))
            self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
            knopf.SetToolTipString("Para introducir un verbo nuevo")
            if len(Worten)!=0 or len(Verben)!=0:
                knopf=wx.Button(self,3,'Lernblock',(50,100))
                self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
                knopf.SetToolTipString("Checar palabras nuevas")
                knopf=wx.Button(self,4,'Wiederholungsblock',(33,140))
                knopf.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
                knopf.SetToolTipString("Checar palabras por memorizar")
                knopf=wx.Button(self,5,'Registerblock',(50,180))
                self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
                knopf.SetToolTipString("Palabras  aprendidas")

            self.Show(True)

    def _when_closed(self, event):
        doClose = True if not self.__close_callback else self.__close_callback()
        if doClose:
            event.Skip()

    def OnClick(self,e):
        if e.GetId()==1:
            WortClass(None,-1)
            self.Close()
        elif e.GetId()==2:
            VerbClass(None,-1)
            self.Close()
        elif e.GetId()==3:
            self.Close()
            L=LernblockClass()
            L.MainLoop()
        elif e.GetId()==4:
            self.Close()
            W=WiederholungsblockClass(None)
            W.MainLoop()
        else:
            self.Close()
            R=RegisterblockClass(None)
            R.MainLoop()

class WortClass(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Wortschatzkartei',size=(500,500))
        self.basicGUI()
        self.Panel=wx.Panel(self)
        self.SetBackgroundColour('white')
        self.Show()
        self.__close_callback = None

    def basicGUI(self):
        wx.StaticText(self, -1, "Artikel", (15, 50), (75, -1))
        self.art = wx.Choice(self, -1, (90, 50), choices = [u'--w\xe4hlen--','keiner','der','das','die'])
        self.art.SetStringSelection(u'--w\xe4hlen--')
        wx.StaticText(self, -1, "Wort", (15, 85), (75, -1))
        self.wort = wx.TextCtrl(self, -1, "Ingresa tu palabra", size=(375, -1),pos=(90,80))
        wx.StaticText(self, -1, "Plural", (15, 120), (75, -1))
        self.Plur = wx.TextCtrl(self, -1, "Plural de tu palabra", size=(375, -1),pos=(90,115))
        wx.StaticText(self, -1, "Beispielsatz", (15, 155), (75, -1))
        self.Beis = wx.TextCtrl(self,-1,u"Ingresa una oraci\xf3n", size=(375,-1),pos=(90,150))
        wx.StaticText(self, -1, "Komposita", (15, 190), (75, -1))
        self.Komp = wx.TextCtrl(self,-1,"Ingresa una palabra compuesta", size=(375,-1),pos=(90,185))
        wx.StaticText(self, -1, "Verb", (15, 225), (75, -1))
        self.Verb = wx.TextCtrl(self,-1,"Ingresa un verbo", size=(375,-1),pos=(90,220))
        wx.StaticText(self, -1, "Adjektiv", (15, 260), (75, -1))
        self.Adje = wx.TextCtrl(self,-1,"Ingresa un adjetivo", size=(375,-1),pos=(90,255))
        wx.StaticText(self, -1, "Notitz:", (15, 290), (75, -1))
        self.Noti= wx.TextCtrl(self,-1,"",size=(375,100),pos=(90,290),style=wx.TE_MULTILINE)
        Akze=wx.Button(self,0,'Akzeptieren',(90,390))
        self.Bind(wx.EVT_BUTTON, self.Akzeptieren, Akze)
        self.Bind(wx.EVT_CLOSE, self._when_closed)

    def _when_closed(self, event):
        doClose = True if not self.__close_callback else self.__close_callback()
        if doClose:
            event.Skip()

    def Akzeptieren(self,e):
        jaOderNo=wx.MessageDialog(None,'Speichern oder Abbrechen','Question',wx.YES_NO)
        Antworten=jaOderNo.ShowModal()
        if Antworten==wx.ID_NO:
            self.Destroy()
            windowClass(None,-1)
        else:
            if self.art.GetStringSelection()==u'--w\xe4hlen--':
                dlg=wx.MessageDialog(self, 'Wahlen ein Artikel','Aufmerksamkeit',wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
            elif self.wort.GetValue()=='Ingresa tu palabra' and self.Adje.GetValue()=='Ingresa un adjetivo':
                dlg=wx.MessageDialog(self, 'Geben Sie ein Wort oder Adjektiv','Aufmerksamkeit',wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                self.art=self.art.GetStringSelection().encode('ISO-8859-1')
                self.wort=self.wort.GetValue().encode('ISO-8859-1')
                self.Plur=self.Plur.GetValue().encode('ISO-8859-1')
                self.Beis=self.Beis.GetValue().encode('ISO-8859-1')
                self.Komp=self.Komp.GetValue().encode('ISO-8859-1')
                self.Verb=self.Verb.GetValue().encode('ISO-8859-1')
                self.Adje=self.Adje.GetValue().encode('ISO-8859-1')
                self.Noti=self.Noti.GetValue().encode('ISO-8859-1')
                if self.wort=="Ingresa tu palabra":             self.wort=''
                if self.Plur=="Plural de tu palabra":           self.Plur=''
                if self.Beis==str(u"Ingresa una oraci\xf3n".encode('ISO-8859-1')):    self.Beis=''
                if self.Komp=="Ingresa una palabra compuesta":  self.Komp=''
                if self.Verb=="Ingresa un verbo":               self.Verb=''
                if self.Adje=="Ingresa un adjetivo":            self.Adje=''

                self.Iden=list()
                for ren in range(len(Worten)):
                    self.Iden.append(int(Worten[ren+1][len(Worten[ren+1])-2]))

                fW=io.open(__location__+'\\Worten.txt','a+')
                self.Wcounter = sum(1 for line in open('Worten.txt'))
                Worten.update({self.Wcounter+1 :(self.art,self.wort,self.Plur,self.Beis,self.Komp,self.Verb,self.Adje,
                    str(datetime.now()),"0",self.Noti,str(max(self.Iden)+1),"Lernblock")})
                del self.Iden
                if self.Wcounter==0:    Schreibe(Worten,fW,self.Wcounter)
                else:                   Schreibe(Worten,fW,self.Wcounter-1)
                fW.close()
                self.Destroy()

                dlg=wx.MessageDialog(self, 'Gespeicherte Worten !!','Aufmerksamkeit',wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                windowClass(None,-1)

class VerbClass(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Wortschatzkartei',size=(500,500))
        self.basicGUI()
        self.Panel=wx.Panel(self)
        self.SetBackgroundColour('white')
        self.Show()
        self.__close_callback = None

    def basicGUI(self):
        wx.StaticText(self, -1, "Verb:", (15, 50), (75, -1))
        self.Verb = wx.TextCtrl(self, -1, "Ingresa tu verbo", size=(375, -1),pos=(90,50))
        wx.StaticText(self, -1, "Verbvalenz:", (15, 85), (75, -1))
        self.Vale = wx.Choice(self, -1, (90, 80), choices = ["0","1","2","3","4"])
        wx.StaticText(self, -1, "Pr\xe4sens:", (15, 120), (75, -1))
        self.Pras = wx.TextCtrl(self, -1, "Verbo en presente", size=(375, -1),pos=(90,120))
        wx.StaticText(self, -1, "Pr\xe4terit:", (15, 155), (75, -1))
        self.Prat = wx.TextCtrl(self, -1, "Verbo en pasado", size=(375, -1),pos=(90,155))
        wx.StaticText(self, -1, "Perfekt:", (15, 190), (75, -1))
        self.Perf = wx.TextCtrl(self,-1,"Verbo en pasado perfecto", size=(375,-1),pos=(90,190))
        wx.StaticText(self, -1, "Beispielsatz:", (15, 225), (75, -1))
        self.Beis = wx.TextCtrl(self,-1,u"Ingresa una oraci\xf3n", size=(375,-1),pos=(90,225))
        wx.StaticText(self, -1, "Nomen:", (15, 255), (75, -1))
        self.Nome = wx.TextCtrl(self,-1,"Ingresa un sustantivo", size=(375,-1),pos=(90,255))
        wx.StaticText(self, -1, "Notitz:", (15, 290), (75, -1))
        self.Noti= wx.TextCtrl(self,-1,"Notitz",size=(375,100),pos=(90,290),style=wx.TE_MULTILINE)
        Akze=wx.Button(self,0,'Akzeptieren',(90,390))
        self.Bind(wx.EVT_BUTTON, self.Akzeptieren, Akze)
        self.Bind(wx.EVT_CLOSE, self._when_closed)

    def _when_closed(self, event):
        doClose = True if not self.__close_callback else self.__close_callback()
        if doClose:
            event.Skip()

    def Akzeptieren(self,e):
        jaOderNo=wx.MessageDialog(None,'Speichern oder Abbrechen','Question',wx.YES_NO)
        Antworten=jaOderNo.ShowModal()
        if Antworten==wx.ID_NO:
            self.Destroy()
            windowClass(None,-1)

        if self.Verb.GetValue()=='Ingresa tu verbo':
            dlg=wx.MessageDialog(self, 'Geben Sie ein Verb','Aufmerksamkeit',wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.Verb=self.Verb.GetValue().encode('ISO-8859-1')
            self.Vale=self.Vale.GetStringSelection().encode('ISO-8859-1')
            self.Pras=self.Pras.GetValue().encode('ISO-8859-1')
            self.Prat=self.Prat.GetValue().encode('ISO-8859-1')
            self.Perf=self.Perf.GetValue().encode('ISO-8859-1')
            self.Beis=self.Beis.GetValue().encode('ISO-8859-1')
            self.Nome=self.Nome.GetValue().encode('ISO-8859-1')
            self.Noti=self.Noti.GetValue().encode('ISO-8859-1')

        if self.Pras=="Verbo en presente":          self.Pras=''
        if self.Prat=="Verbo en pasado":            self.Prat=''
        if self.Perf=="Verbo en pasado perfecto":   self.Perf=''
        if self.Beis==str(u"Ingresa una oraci\xf3n".encode('ISO-8859-1')):    self.Beis=''
        if self.Nome=="Ingresa un sustantivo":      self.Nome=''

        self.Iden=list()
        for ren in range(len(Verben)):
            self.Iden.append(int(Verben[ren+1][len(Verben[ren+1])-2]))

        fV=io.open(__location__+'\\Verben.txt','a+')

        self.Vcounter = sum(1 for line in open('Verben.txt'))
        Verben.update({self.Vcounter+1 : (self.Verb,self.Vale,self.Pras,self.Prat,self.Perf,self.Beis,self.Nome,str(datetime.now()),
            "0",self.Noti,str(max(self.Iden)+1),"Lernblock")})

        if self.Vcounter==0:    Schreibe(Verben,fV,self.Vcounter)
        else:                   Schreibe(Verben,fV,self.Vcounter-1)
        fV.close()

        self.Destroy()
        dlg=wx.MessageDialog(self, 'Gespeicherte Verben !!','Aufmerksamkeit',wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        windowClass(None,-1)

class LernblockClass(wx.App):
    def OnInit(self):
        Fram(None,"Lernblock")
        return True

class WiederholungsblockClass(wx.App):
    def OnInit(self):
        Fram(None,"Wiederholungsblock")
        return True

class RegisterblockClass(wx.App):
    def OnInit(self):
        Fram(None,"Registerblock")
        return True

class Fram(wx.Frame):
    def __init__(self, parent,block):
        wx.Frame.__init__(self, parent, wx.NewId(),'Blocks',pos=wx.DefaultPosition,
            size=(200,150),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX & ~wx.CLOSE_BOX ^ wx.RESIZE_BORDER  )
        self.block=block
        self.__close_callback = None
        wx.Frame.CenterOnScreen(self)
        self.panel = wx.Panel(self)
        self.SetBackgroundColour('white')
        self.basicGUI()
        self.Show()
    def basicGUI(self):
        self.Bind(wx.EVT_CLOSE, self._when_closed)
        knopf=wx.Button(self,1,'Worten',(50,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
        knopf=wx.Button(self,2,'Verben',(50,50))

        self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)
        knopf=wx.Button(self,3,'Züruck'.decode("UTF-8"),(50,80))
        self.Bind(wx.EVT_BUTTON, self.OnClick, knopf)

    def _when_closed(self, event):
        self.Destroy()

    def OnClick(self,e):
        if e.GetId()==1:
            tipo="W"
            frame = MyFrame(None,tipo,self.block)
            self.Close()
            frame.Show()
            
        elif e.GetId()==2:
            tipo="V"
            frame = MyFrame(None,tipo,self.block)
            self.Close()
            frame.Show()

        elif e.GetId()==3:
            self.Close()
            windowClass(None,-1)

class MyFrame(wx.Frame):
    def __init__(self, parent,tipo,block):
        wx.Frame.__init__(self, parent, wx.NewId(), size=(wx.DisplaySize()[0],wx.DisplaySize()[1]/2))
        self.tipo=tipo
        self.block=block
        self.__close_callback = None
        wx.Frame.CenterOnScreen(self)
        self.panel = MyPanel(self,tipo)
        menuBar = wx.MenuBar()
        fileB=wx.Menu()
        editB=wx.Menu()
        fileB.Append(wx.ID_ANY,'Speichern und beenden')
        self.Bind(wx.EVT_CLOSE, self._when_closed)

        if self.tipo=="W":  fileB.Append(wx.ID_ANY,'Verben')
        else:               fileB.Append(wx.ID_ANY,'Worten')
        fileB.Append(wx.ID_ANY,'Beenden')

    def _when_closed(self, event):
        doClose = True if not self.__close_callback else self.__close_callback()
        if doClose:
            event.Skip()

class MyPanel(wx.Panel):
    def __init__(self, parent,tipo):
        self.tipo=tipo
        self.parent=parent
        self.Iden=list()
        wx.Panel.__init__(self, parent)
        self.block=self.parent.block
        self.list = MyListCtrl(self,9,self.tipo,style=wx.LC_REPORT)
        self.add_button = wx.Button(self, label="Speichern und beenden")
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer.Add(self.add_button, proportion=1, flag=wx.ALL, border=5)
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        v_sizer.Add(h_sizer, proportion=0, flag=wx.EXPAND)
        v_sizer.Add(self.list, proportion=1, flag=wx.EXPAND, border=5)
        self.SetSizer(v_sizer)
        self.add_button.Bind(wx.EVT_BUTTON,self.Save)

        self.Bind(wx.EVT_CLOSE, self._when_closed)

    def _when_closed(self, event):
        doClose = True if not self.__close_callback else self.__close_callback()
        if doClose:
            event.Skip()

    def GetBlocks(self,Dicc,block):
        lista=list()
        noBlock=list()
        for row,cont in list(enumerate(Dicc.values())):
            if not block in cont:
                lista.append(Dicc[row+1])
        return lista

    def Save(self, event):
        if self.tipo=="W":  L=Worten
        else:               L=Verben

        Nueva=self.GetBlocks(L,self.block)
        #Busca palabras que no aparecen en el list control
        #Devuelve numero del Dicc
        #Encuentra(Dicc,Id)
        Ids=list()

        pals=[[None]*len(L[1])]*len(L)
        siz=self.list.GetItemCount()
        for row in range(siz):
            item=list()
            for col in range(12):
                item.append(self.list.GetItem(itemId=row, col=col).GetText().encode("ISO-8859-1"))
            Ids.append(Encuentra(L,item[len(item)-2]))
            item=tuple(item)
            pals[row]=item

        for i,j in list(enumerate(Nueva)):
            pals[siz+i]=j
        for row,j in enumerate(pals):
            L.update({row+1:j})

        del item

        if self.tipo=="W":
            fW=io.open(__location__+'\\Worten.txt','w')
            Schreibe(L,fW,0)
        else:
            fW=io.open(__location__+'\\Verben.txt','w')
            Schreibe(L,fW,0)
        fW.close()
        
        del L
        self.parent.Destroy()

        windowClass(None,-1)


class MyPopupMenu(wx.Menu):
    def __init__(self,parent, item,pos):
        super(MyPopupMenu,self).__init__()
        self.parent = parent
        self.item = item
        self.list=parent.list
        self.pos=pos
        Notitz = wx.MenuItem(self,wx.NewId(), 'Notitz vom %s' % item.GetText())
        self.AppendItem(Notitz)
        self.Bind(wx.EVT_MENU, self.Notitz, Notitz)
        Dele = wx.MenuItem(self,wx.NewId(), 'Delete %s' % item.GetText())
        self.AppendItem(Dele)
        self.Bind(wx.EVT_MENU, self.OnDelete, Dele)

    def Notitz(self,e):
        self.parent.parent.NN = NewWindow(self.parent.parent,(520,200))
        a=self.list.GetItem(itemId=self.pos,col=9).GetText()
        self.Noti= wx.TextCtrl(self.parent.parent.NN,-1,a,size=(375,100),pos=(20,20),style=wx.TE_MULTILINE)
        self.parent.parent.NN.SetBackgroundColour('white')
        self.Acep=wx.Button(self.parent.parent.NN,1,'Save',(395,20))
        self.Acep.Bind(wx.EVT_BUTTON,self.Save)
        self.Canc=wx.Button(self.parent.parent.NN,2,'Exit',(395,50))
        self.Canc.Bind(wx.EVT_BUTTON,self.Cancel)

        self.parent.parent.NN.Show()
    def Save(self,e):
        self.parent.SetStringItem(self.pos,9,self.Noti.GetValue())
        self.parent.parent.NN.Destroy()

    def Cancel(self,e):
        self.parent.parent.NN.Destroy()

    def OnDelete(self,e):
        self.parent.DeleteItem(self.pos)
        if self.parent.tipo=='W':
            Worten.pop(self.pos+1)
        else:
            Verben.pop(self.pos+1)


class MyListCtrl(wx.ListCtrl, listmix.ColumnSorterMixin ,listmix.TextEditMixin):
    def __init__(self, parent, columns,tipo,style=0):
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)
        self.parent = parent
        listmix.TextEditMixin.__init__(self)
        self.Iden=parent.Iden
        self.list=self.GetListCtrl()
        if not self.list:
            raise ValueError, "No wx.ListCtrl available"
        self.tipo=tipo
        self.block=parent.block
        self.R_MOUSE = 0
        if self.tipo=="W":
            self.InsertColumn(0, "Artikel")
            self.InsertColumn(1, "Wort")
            self.InsertColumn(2, "Plural")
            self.InsertColumn(3, "Beispielsatz")
            self.InsertColumn(4, "Komposita")
            self.InsertColumn(5, "Verb")
            self.InsertColumn(6, "Adjektiv")
            self.InsertColumn(7, "Datum")
            self.InsertColumn(8, "Versuche")
            self.InsertColumn(9, "Notitz")
            self.InsertColumn(10, "ID")
            self.InsertColumn(11, "Block")
            self.itemDataMap = Worten

        else:
            self.InsertColumn(0, "Verb")
            self.InsertColumn(1, "Verbvalenz")
            self.InsertColumn(2, "Pr\xe4sens")
            self.InsertColumn(3, "Pr\xe4terit")
            self.InsertColumn(4, "Perfekt")
            self.InsertColumn(5, "Beispielsatz")
            self.InsertColumn(6, "Nomen")
            self.InsertColumn(7, "Datum")
            self.InsertColumn(8, "Versuche")
            self.InsertColumn(9, "Notitz")
            self.InsertColumn(10, "ID")
            self.InsertColumn(11, "Block")
            self.itemDataMap = Verben
        
        self.refresh_list()

        if self.tipo=="W":
            self.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
            self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(3, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(4, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(5, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(6, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(7, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(8, wx.LIST_AUTOSIZE_USEHEADER)
            self.SetColumnWidth(9, 0)
            self.SetColumnWidth(10, 0)
            self.SetColumnWidth(11, 0)
        else:
            self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
            self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(3, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(4, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(5, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(6, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(7, wx.LIST_AUTOSIZE)
            self.SetColumnWidth(8, wx.LIST_AUTOSIZE_USEHEADER)
            self.SetColumnWidth(9, 0)
            self.SetColumnWidth(10, 0)
            self.SetColumnWidth(11, 0)
        if self.GetColumnWidth(5)>200:
            self.SetColumnWidth(5,200)
        if self.GetColumnWidth(6)>200:
            self.SetColumnWidth(6,200)

        listmix.ColumnSorterMixin.__init__(self, 9)
        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect)
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onRightClick)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick)

    def OnColClick(self, event):
        oldCol = self._col
        self._col = col = event.GetColumn()
        self._colSortFlag[col] = int(not self._colSortFlag[col])
        self.GetListCtrl().SortItems(self.GetColumnSorter())
        self.OnSortOrderChanged()

        if self.tipo=='W':
            L=Worten
        else:
            L=Verben

        for row in range(self.list.GetItemCount()):
            item=list()
            for col in range(12):
                item.append(self.list.GetItem(itemId=row, col=col).GetText().encode("ISO-8859-1"))
            L.update({row+1:tuple(item)})

    def GetListCtrl(self):
        return self

    def OnBeginLabelEdit(self,evt):
        col=evt.m_col
        if col==8:
            num=int(self.GetItem(itemId=evt.GetIndex(),col=col).GetText())
            if num==3:
                if self.tipo=="W":
                    L=Worten
                    pos=1
                else:
                    L=Verben
                    pos=0
                
                #Palabras Modificadas
                pal=self.GetItem(itemId=evt.GetIndex(),col=1).GetText()
                item=list()
                iden=self.parent.list.GetItem(itemId=evt.GetIndex(), col=len(L[evt.GetIndex()+1])-2).GetText()
                num=Encuentra(L,iden)
                #Encuentra el index de la palabra usando la Id
                for col in range(12):
                    if col==len(L[num])-2:
                        item.append(str(int(L[num][col])+1))
                    elif col==len(L[num])-4:
                        item.append('0')
                    elif col==len(L[num])-1:
                        if self.block=='Lernblock':
                            item.append('Wiederholungsblock')
                        else:
                            item.append('Registerblock')
                    else:
                        item.append(self.parent.list.GetItem(itemId=evt.GetIndex(), col=col).GetText().encode("ISO-8859-1"))
                L.update({num:tuple(item)})

                del L
                self.refresh_list()
            else:
                self.SetStringItem(evt.GetIndex(),col,unicode(str(num+1),"ISO-8859-1"))
                evt.Veto()

    def refresh_list(self):
        self.DeleteAllItems()
        L=dict()
        if self.tipo=="W":
            L=Worten
            self.pos=1
        else:
            L=Verben
            self.pos=0
        Lern=Selecciona(L,self.block)
        for key,data in L.items():
            if key in Lern:
                index = self.InsertStringItem(sys.maxint, data[0])
                for i, j in list(enumerate(data)):
                    self.SetStringItem(index,i,unicode(j,"ISO-8859-1"))

                self.SetItemData(index,key)

        for colu in range(len(L)):
            self.Iden.append(L[colu+1][len(L[colu+1])-2])
        del L

    def onRightClick(self,evt):
        pos = evt.GetPosition()
        if self.tipo=='W':  n=1
        else:               n=0
        pal=self.GetItem(itemId=evt.GetIndex(),col=n)
        self.PopupMenu(MyPopupMenu(self,pal, evt.GetIndex()))

    #def OnSelect(self, event):
    #    index = event.GetIndex()
    #    self.itemSel = self.GetItem(itemId=index)

class NewWindow(wx.Frame):
    def __init__(self, parent,dimen):
        wx.Frame.__init__(self, parent, size=dimen, style=wx.DEFAULT_FRAME_STYLE)
        self.parent = parent
        self.CenterOnParent()
        self.__close_callback = None
        panel = wx.Panel(self)

    def onClick(self,event):
        self.Close()

class Tuplika:
    def llenar(self,fil,dic):
        self.x=fil.readlines()
        self.l=[[None]*12]*len(self.x)
        for i,k in list(enumerate(self.x)):
            if not k.startswith('*'):
                print k
                print "\nHOLA\n"
                k=k.split('||')
                for m,j in enumerate(k):
                    self.l[i-1][m]=j.strip()
                continue
            """if not k.startswith('*'):
                print "\nHOLA\n"
                self.l=list()   
                k=k.split('\t')
                for j in k:
                    self.l.append(j.strip())
                dic.update({i : tuple(self.l)})
                del self.l
                continue"""
            k=k.split('||')
            for m,j in enumerate(k):
                self.l[i][m]=j.strip()
                print i,m, j.strip()
            print i,self.l
        for row,j in enumerate(self.l):
            dic.update({row+1:tuple(self.l[row])})
        #dic.update({i+1 : tuple(self.l)})  
        del self.l
        dic.clear

if __name__ == "__main__":
    
    t=Tuplika()

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    fV=file(__location__+'\\Verben.txt','a+')
    t.llenar(fV,Verben)

    fW=file(__location__+'\\Worten.txt','a+')
    t.llenar(fW,Worten)
    
    print Worten
    fV.close()
    fW.close()
    app=wx.App()
    windowClass(None,-1)
    app.MainLoop()
