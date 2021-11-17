if not __name__ == "__main__":
    print("Started <Pycraft_ModelMathsUtil>")
    class ComputeMapPoints:
        def __init__(self):
            pass

        def LoadingMapData(self, vertex, counterFORvertex):
            counterFORvertex += 1
            self.min_v = [min(self.Map_box[0][i], vertex[i]) for i in range(3)]
            self.max_v = [max(self.Map_box[1][i], vertex[i]) for i in range(3)]
            self.Map_box = (self.min_v, self.max_v)
            return counterFORvertex
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()