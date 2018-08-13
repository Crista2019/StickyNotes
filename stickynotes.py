import tkinter
from tkinter import messagebox, simpledialog, Listbox, Menu, Tk, Label, Scrollbar, filedialog, Frame, Text, OptionMenu, StringVar, Toplevel, Entry, Button
import smtplib
from email.mime.text import MIMEText
import binascii

class StickyNotes(Frame):
    ftypes = [('Plain text file', '.txt'),
            ('All files', '*')]

    fileName = "default name"

    def __init__(self, parent, text):
        Frame.__init__(self, parent)
        self.parent = parent
        self.text = text
        self.initUI()

    def initUI(self):
        self.parent.title('Sticky Notes')
        Label(self.parent, text='Use the directory to navigate notes').pack(pady=20,padx=50)

        menubar = Menu(self.parent)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.newNote)
        filemenu.add_command(label="Save", command=self.saveNote)
        filemenu.add_command(label="Open", command=self.openPastNote)
        # filemenu.add_command(label="Send", command=self.sendMail)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exitApp)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.help)
        helpmenu.add_command(label="About...", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        examplesmenu = Menu(menubar, tearoff=0)
        examplesmenu.add_command(label="Dino", command=self.dinosaur)
        examplesmenu.add_command(label="Hello World", command=self.helloworld)
        examplesmenu.add_command(label="It's-a me!", command=self.mario)
        menubar.add_cascade(label="Examples", menu=examplesmenu)

        toolsmenu = Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Convert to Binary", command=self.binaryCon)
        toolsmenu.add_command(label="Convert to ASCII", command=self.asciiCon)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        self.parent.config(menu=menubar)

    def exitApp(self):
       if messagebox.askokcancel("Exit","The application will be closed"):
           self.parent.quit()

    def saveNote(self):
        if messagebox.askyesno("Save","Do you want to save the current note?"):
            try:
                self.parent.filename =  filedialog.asksaveasfilename(initialdir = "/Desktop", initialfile=self.fileName, title = "Select file", filetypes=self.ftypes, defaultextension='.txt')
                f = open(self.parent.filename, 'w')
                f.write(self.text.get('1.0', 'end'))
                f.close()
                tkinter.messagebox.showinfo('Save Alert', 'File Saved')
            except:
                pass

    def openPastNote(self):
        if messagebox.askyesno("Open Past Note","Would you like to open a previous note?"):
            self.deleteSpace()
            filename = tkinter.filedialog.askopenfilename(filetypes = self.ftypes)
            f = open(filename, 'r')
            f2 = f.read()
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', f2)
            f.close()
            self.parent.title('Past Note: %s)' % filename)

    def newNote(self):
        if messagebox.askyesno("Write New Note","Would you like to write a new note?"):
            self.deleteSpace()

            def localRenameWindow():
                self.parent.title('New Note: %s' % name.get())
                self.fileName = name.get()

            win = Toplevel()
            win.geometry("275x75")
            win.wm_title("Note Options")

            Label(win, text="Name of Note").grid(row=0)
            name = Entry(win)
            name.grid(row=0, column=1)

            submitBtn = Button(win, text='Save', command=localRenameWindow)
            submitBtn.grid(row=2, column=1)

    def sendMail(self):
        msg = MIMEText(self.text.get('1.0', 'end'))
        subject = simpledialog.askstring("Subject Line", "What is the subject?", parent=self.parent)
        sender = simpledialog.askstring("You", "What is the sender's email?", parent=self.parent)
        recipient = simpledialog.askstring("Recipient", "What is the recipient's email?", parent=self.parent)
        msg['Subject'] = '%s' % subject
        msg['From'] = sender
        msg['To'] = recipient
        s = smtplib.SMTP('localhost', 1025)
        try:
            s.sendmail(sender, [recipient], msg.as_string())
        except SMTPException:
            print("Error: unable to send email")
        finally:
            s.quit()

    def about(self):
        self.deleteSpace()
        self.text.insert('1.0', "This is a simple GUI deisgned to make digital post-it notes.\nFor additional information for operating this program, see HELP INDEX. \n\nMade by: Crista Falk 2018")
        self.renameWindow("About")

    def help(self):
        self.deleteSpace()
        self.text.insert("1.0", "Help: \n\n      1. The menu directory above will provide options related to making notes. \n      2. To write a new note, select NEW. \n      3. To save a current note to your computer, select SAVE. \n      4. To open a previous note, select OPEN. \n      5. For example notes and adorable ASCII doodles, check out EXAMPLES. \n      6. To leave the application, select EXIT or press the [x] at the top right of the window. \n")
        self.renameWindow("Help")

    def deleteSpace(self):
        self.text.delete('1.0', 'end')

    def dinosaur(self):
        self.text.delete('1.0', 'end')
        self.text.insert("1.0",
        "                      __ \n")
        self.text.insert("end",
        "                     /  _) \n")
        self.text.insert("end",
        "         _.----._/  /   \n")
        self.text.insert("end",
        "        /             /     \n")
        self.text.insert("end",
        "   _/  (    | (    |      \n")
        self.text.insert("end",
        "  /_.-'|__|--|__|      ")
        self.renameWindow("Dino Ascii")

    def helloworld(self):
        self.text.delete('1.0', 'end')
        self.text.insert("1.0","0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100")
        self.renameWindow("Hello World")

    def mario(self):
        self.text.delete('1.0', 'end')
        self.text.insert("1.0","\n")
        self.text.insert("end","── ── ── ── ── ── ── ██ ██ ██ ██ ── ██ ██ ██ ──\n")
        self.text.insert("end","── ── ── ── ── ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ \n")
        self.text.insert("end","── ── ── ── ██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ \n")
        self.text.insert("end","── ── ── ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ░░ ░░ ██ \n")
        self.text.insert("end","── ── ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ░░ ██ \n")
        self.text.insert("end","── ── ██ ▓▓ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██ ── \n")
        self.text.insert("end","── ██ ██ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██\n")
        self.text.insert("end","── ██ ░░ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ \n")
        self.text.insert("end","██ ░░ ░░ ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ \n")
        self.text.insert("end","██ ░░ ░░ ░░ ██ ░░ ░░ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ \n")
        self.text.insert("end","── ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ░░ ░░ ██ ██ ██ ── \n")
        self.text.insert("end","── ── ██ ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ██ ▓▓ ██ ── \n")
        self.text.insert("end","── ── ── ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ▓▓ ██ ── \n")
        self.text.insert("end","── ── ── ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ▓▓ ██ ── \n")
        self.text.insert("end","── ░░ ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ▓▓ ██ ── ── \n")
        self.text.insert("end","── ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ██ ── ── ── \n")
        self.text.insert("end","██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██ ── ── ── \n")
        self.text.insert("end","██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██ ── ── ── \n")
        self.text.insert("end","██ ██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ██ ██ ██ ──\n")
        self.text.insert("end","── ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ── \n")
        self.text.insert("end","── ── ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ██ \n")
        self.text.insert("end","── ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n")
        self.text.insert("end","██ ██ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n")
        self.text.insert("end","██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ \n")
        self.text.insert("end","██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ── ── ── ██ ▓▓ ▓▓ ██ ██ \n")
        self.text.insert("end","██ ▓▓ ▓▓ ██ ██ ── ── ── ── ── ── ── ██ ██ ██ ── \n")
        self.text.insert("end","── ██ ██ ── ── ── ── ── ── ── ── ── ── ── ── ──")

        self.renameWindow("Mario")

    def renameWindow(self, name):
        self.parent.title('Sticky Notes: %s' % name)
        self.fileName = name

    def binaryCon(self):
        if len(self.text.get('1.0', 'end')) > 1:
            binary = bin(int.from_bytes(self.text.get('1.0', 'end').encode(), 'big'))
            self.deleteSpace()
            self.text.insert("1.0", binary)
        else:
            messagebox.showinfo("Alert", "Text input is empty.")

    def asciiCon(self):
        if len(self.text.get('1.0', 'end')) > 1:
            try:
                n = int(self.text.get('1.0', 'end'), 2)
                ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
                self.deleteSpace()
                self.text.insert("1.0", ascii)
            except:
                messagebox.showinfo("Alert", "Text is already in ASCII format.")
        else:
            messagebox.showinfo("Alert", "Text input is empty.")

def main():
    root = Tk()
    root.geometry("600x400")
    root.option_add('*font', '{Helvetica} 11')
    text = Text(master=root, bg = '#f9f3a9', wrap = 'word', undo = True)
    text.focus_set()
    program = StickyNotes(root, text)
    text.pack(fill = 'both', expand = 1)
    root.mainloop()

if __name__ == '__main__':
    main()
