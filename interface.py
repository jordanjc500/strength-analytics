import tkinter as tk
import workoutcalcs

def calc1rm():
    weight = float(entryWeight.get())
    reps = int(entryReps.get())

    result = workoutcalcs.epley(weight, reps)
    estimation.config(text=f"Estimated 1RM: {result:.1f}")  
    
    if weight > 1000:
        warning.config(text=f"Are you sure you just lifted {weight}?")
        warning.pack(after=estimation)
    else:
        warning.pack_forget()
    

root = tk.Tk()
root.title("Strength Analytics")
root.geometry("400x300")

desc = tk.Label(root, text="Enter weight and reps to calculate a one rep max", bg="lightgray")
desc.pack()

#frame for input fields
inputFrame = tk.Frame(root)
inputFrame.pack(pady=10)

tk.Label(inputFrame, text="Weight:").grid(row=0, column=0)
entryWeight = tk.Entry(inputFrame)
entryWeight.grid(row=0, column=1)

tk.Label(inputFrame, text="Reps:").grid(row=1, column=0)
entryReps = tk.Entry(inputFrame)
entryReps.grid(row=1, column=1)


calcButton = tk.Button(root, text="Calculate", command=calc1rm)
calcButton.pack()

estimation = tk.Label(root, text="Estimated 1RM: -")
estimation.pack()

warning = tk.Label(root, text=f"Are you sure you just lifted --?", fg="red")

root.mainloop()
