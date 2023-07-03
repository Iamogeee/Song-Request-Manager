import tkinter as tk

playlist = []

prompt = '''Welcome to DJ Ogenna's Song Request Manager!
Enter the song title to make a song request.
To exit, enter Quit.
'''

def add_song():
    songtitle = entry.get()
  
    if songtitle in playlist:
        status_label.config(text="This song has already been requested.")
        index_label.config(text=f"The song is number {playlist.index(songtitle) + 1} on the list.")
    else:
        playlist.append(songtitle)
        status_label.config(text=f"The song '{songtitle}' has been added to the list.")
        index_label.config(text=f"It is song number {playlist.index(songtitle) + 1}.")

def quit_app():
    status_label.config(text="Thank you for your requests. Enjoy the show!")
    index_label.config(text="")
    add_button.config(state=tk.DISABLED)
    quit_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("DJ Ogenna's Song Request Manager")



prompt_label = tk.Label(root, text=prompt)
prompt_label.pack()

entry_label = tk.Label(root, text="Enter a song title:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Song", command=add_song)
add_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

index_label = tk.Label(root, text="")
index_label.pack()

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack()

root.mainloop()