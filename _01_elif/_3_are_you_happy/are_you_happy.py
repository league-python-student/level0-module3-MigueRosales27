from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    pass
    user_answer = simpledialog.askstring(None, "Are you happy?")


    if(user_answer== "yes"):
        messagebox.showinfo(None, "Keep doing what you are doing!")
        sys.exit
    if(user_answer=="no"):
        user_answer=simpledialog.askstring(None, "Do you want to be happy?")

    if(user_answer=="no"):
        messagebox.showinfo(None,"Keep doing what you are doing!")

    if(user_answer=="yes"):
        messagebox.showinfo(None,"You need to change something.")

