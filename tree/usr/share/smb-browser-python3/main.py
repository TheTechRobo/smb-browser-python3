#!/usr/bin/python3
import gi,subprocess

class EmptyClass: pass

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Set Mount Format", transient_for=parent, flags=0)
        self.add_buttons(
            "CANCEL", 78111112, "Read Only", 42.0, "Read/Write", 69
        )

        self.set_default_size(150, 100)

        label = Gtk.Label(label="What do you want to mount as?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()
class MyWindow(Gtk.Window):
    def __init__(self):
        # MAIN BEHIND THE SCENES INIT
        super().__init__(title="SMB Browser Revamped")

        dialog = Gtk.MessageDialog(
            transient_for=self,flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Note",
        )
        dialog.format_secondary_text(
            "This program is only for browsing shares on other computers. If you would like to share files on your computer simply open Thunar, right-click on the directory you want to share and select the option 'Share'. If you want to manage your Shared configurations or set advanced options run 'Samba Admin', you can find it in your menu."
            "\tYour computer will scan for shares when you press OK. SMB-Browser might freeze for a few seconds."
        )
        dialog.run()

        dialog.destroy()

        self.MainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) #because gtk is stubborn
        self.add(self.MainBox)
        self.notebook = Gtk.Notebook() #main tab system
        self.MainBox.pack_start(self.notebook, True, True, 0)

        self.box = Gtk.Box()
        self.box.props.expand = True
        self.box.set_name('bottombar')#bottom bar (about and quit)
        self.MainBox.pack_start(self.box, True, True, 0)

        self.Tabs = EmptyClass()
        self.Widgets = EmptyClass()
        # NOW WE'RE ACTUALLY DOING SHIT
        self.Tabs.tab2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.Widgets.setmountform = Gtk.Button(label="Read only or read-write?")
        self.Widgets.mountparams = Gtk.Entry()
        self.Tabs.tab2.pack_start(Gtk.Label(label="Params to pass to the mount command"), True, True, 0)
        self.Tabs.tab2.pack_start(self.Widgets.mountparams, True, True, 0)
        self.Widgets.setmountform.connect("clicked", self.mntform)
        self.Tabs.tab2.pack_start(self.Widgets.setmountform, True, True, 0)

        self.Tabs.tab0 = Gtk.Box()
        self.serverData = self._getServers(self)
        self.Widgets.ServerListBox = Gtk.TreeStore(str)
        for i in self.serverData:
            ip, hostname = i
            self.Widgets.ServerListBox.append(None, [f"{ip} ({hostname})"])
        self.Widgets.ServerListView = Gtk.TreeView(model=self.Widgets.ServerListBox)
        self.renderer = Gtk.CellRendererText()
        self.column = Gtk.TreeViewColumn(cell_renderer=self.renderer, text=0, weight=1)
        self.Widgets.ServerListView.append_column(self.column)
        self.Widgets.ServerListView.get_selection().connect("changed", self.showData)

        self.Tabs.tab0.pack_start(self.Widgets.ServerListView, True, True, 5)
        self.notebook.append_page(self.Tabs.tab0, Gtk.Label(label="Main"))
        self.notebook.append_page(self.Tabs.tab2, Gtk.Label(label="Mount options"))
        self.about = Gtk.Button(label="About")
        self.about.connect("clicked", self.about_box)
        self.box.pack_start(self.about, True, True, 10)
        self.box.pack_start(Gtk.Label(label="SMB-Browser Revamped by TheTechRobo"), True, True, 0)
        self.quit = Gtk.Button(label="Quit")
        self.quit.connect("clicked", self.destroyy)
        self.box.pack_end(self.quit, True, True, 0)
        #self.GetServerButon = Gtk.Button(label="DEBUG")
        #self.GetServerButon.connect("clicked",self._getServers)
        #self.box.pack_end(self.GetServerButon, True, True, 0)
        self.getShareData("192.168.2.186")
    def showData(self, sel):
        model, treeiter = sel.get_selected()
        if treeiter is None: return
        sel = model[treeiter][0]
        STRING = sel
        sel = STRING.split(" ")[0], STRING.split(" ")[1].replace("(","").replace(")","")
        self.ipChosen = sel[0]
        return sel
    def getShareData(self, host):
        rawData = subprocess.run(f"smbclient -NL {host}", shell=True, capture_output=True).stdout.decode()
        #print(rawData)
        self.shares = list()
        for i in rawData.split("\n"): #IM SO STUPID I FORGOT THE SPLIT AND WAS STUCK ON THIS FOR LIKE 10 MINUTES
            if "Disk" not in i:
                #print("continue")
                continue
            j = i.strip()
            #print(j)
            thing = list()
            a = j.split(" ")
            #print(a)
            for k in a:
                #print("k: "+k)
                if k != "": thing.append(k)
            print(thing)
            self.shares.append((thing[0], thing[2:]))
        print(self.shares)
    def destroyy(self, *args): self.destroy()
    def mntform(self, idkwhatthisvariableis):
        dialog = DialogExample(self)
        response = dialog.run()

        if response == "Nope" or response == 78111112:
            print("sad boi")
        elif response == 42.0:
            print("Read Only")
        elif response == 69:
            print("Read Write")

        dialog.destroy()
    def about_box(self, widget):
        # { Licence data - feel free to skip
        licence_data = """
        This program was designed to assist users in finding and mounting samba shared folders on a network while being easy yet functional Copyright (C) <2007, 2021>  <David Braker, TheTechRobo>. This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. On a Debian GNU/Linux system you can find a copy of this license in `/usr/share/common-licenses/'.
        """
        # }
        dialog = Gtk.MessageDialog(
            transient_for=self,flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="About SMB Browser Revamped",
        )
        dialog.format_secondary_text(
            f"SMB Browser Revamped version 1.0. Created by TheTechRobo with some borrowed code from the original.\nNo, I don't like legalese either, but it keeps the lawyers away.\n{licence_data}" #fuck %s and .format
        )
        dialog.run()

        dialog.destroy()
    def _getServers(self, parent):
        sambaServerList = subprocess.run(["nmblookup __SAMBA__"], shell=True, capture_output=True).stdout.decode()
        print(sambaServerList)
        servers = []
        for line in sambaServerList.split("\n"):
            lne = line.split(" ")[0]
            if lne == "\n" or lne == "": continue
            print(lne)
            servers.append((lne, subprocess.run(["nbtscan -e %s" % lne], shell=True, capture_output=True).stdout.decode().replace("\n","").split("\t")[1]))
        print(servers)
        return servers


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
