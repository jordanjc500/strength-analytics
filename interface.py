import tkinter as tk
import workoutcalcs

def calc1rm():
    try:
        weight = float(entryWeight.get())
        reps = int(entryReps.get())
        highThreshold = 1000

        if weight <= 0 or reps <= 0:
            raise ValueError("Weight and reps must both be positive numerical values. Reps must be an integer.")

        result = workoutcalcs.epley(weight, reps)
        estimation.config(text=f"Estimated 1RM: {result:.1f}")

        invWarning.pack_forget()

        if weight >= 1000:
            weightWarning.config(text=f"Are you sure you just lifted {weight}?", fg="orange")
            weightWarning.pack(after=estimation)
        else:
            weightWarning.pack_forget()

        if reps > 10:
            repsWarning.pack(after=weightWarning if weight >= 1000 else estimation)
        else:
            repsWarning.pack_forget()
        
    except ValueError:
        
        repsWarning.pack_forget()
        weightWarning.pack_forget()
        estimation.config(text=f"Estimated 1RM: --")
        invWarning.pack(after=estimation)
        
    

root = tk.Tk()
root.title("Strength Analytics")
root.geometry("800x600")

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

#frame for unit selection
'''unit = tk.StringVar(value="lbs")
unitFrame = tk.Frame(root)
unitFrame.pack()
unitText = tk.Label(unitFrame, text="Units:").grid(row=0, column=2)
 
tk.Radiobutton(
    inputFrame,
    text="lbs",
    variable=unit,
    value="lbs"
).grid(row=0, column=2)

tk.Radiobutton(
    inputFrame,
    text="kg",
    variable=unit,
    value="kg"
).grid(row=0, column=2)'''

calcButton = tk.Button(root, text="Calculate", command=calc1rm)
calcButton.pack()

estimation = tk.Label(root, text="Estimated 1RM: -")
estimation.pack()

weightWarning = tk.Label(root, text=f"Are you sure you just lifted --?", fg="darkorange")
repsWarning = tk.Label(root, text="Rep count is over 10, results are expected to be less accurate", fg="gold")
invWarning = tk.Label(root, text="Weight and reps must both be positive numerical values. Reps must be an integer.", fg="red")

root.mainloop()
