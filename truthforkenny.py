#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
    

def write_truth():
    print("Chloe loves you!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Bye!", 
                   fg="blue",
                   command=quit)
button.pack(side=tk.LEFT)
truth = tk.Button(frame,
                   text="Here's the truth...",
                   command=write_truth)
truth.pack(side=tk.LEFT)

root.mainloop()


# In[ ]:





# In[ ]:




