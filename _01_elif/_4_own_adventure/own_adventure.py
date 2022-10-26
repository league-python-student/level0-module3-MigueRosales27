from tkinter import simpledialog, messagebox,  Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()


# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

    question = simpledialog.askstring(None,"Once there was a boy named Bert and he liked to play _____ (soccer or football?")

    if(question=="soccer"):
        question=simpledialog.askstring(None,"He played in his school team and became the best goalie at school. He; won or lost the championsih? ")
    if(question=="football"):
        question=simpledialog.askinteger(None,"He played in the final game and _________ (1.) lost the game or 2.) scored the winning touchdown?")

    if(question== 1):
        messagebox.showinfo(None, "He was bullied at school for the whole week :( ")
    if(question== 2):
        messagebox.showinfo(None, "He became his school hero!")
    if(question=="won"):
        messagebox.showinfo(None, "He became his school hero!")
    if(question=="lost"):
        messagebox.showinfo(None, "He was bullied at school for the whole week :( ")
    pass


