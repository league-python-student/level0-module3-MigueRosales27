from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    pass
    user_answer = simpledialog.askstring(None, "Are you happy?")


    if(user_answer== "Yes" , "yes"):
        messagebox.showinfo(None, "Keep doing what you are doing!")
    if(user_answer=="no", "No"):
        messagebox.showinfo(None, "Do you want to be happy?")

