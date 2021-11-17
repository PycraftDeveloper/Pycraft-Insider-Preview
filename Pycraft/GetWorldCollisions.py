if not __name__ == "__main__":
    print("Started <Pycraft_GetWorldCollisions>")
    class GetMapCollisions:
        def __init__(self):
            pass

        def GetCollisions(self):
            try:
                #self.map_vertices = [0,0,0,0,0]
                for i in range(len(self.map_vertices)):
                    #print(int(self.map_vertices[i])*self.G3Dscale, int(self.X))
                    if int(self.map_vertices[i])*self.G3Dscale == int(self.X):
                        try:
                            if int(self.map_vertices[i+2])*self.G3Dscale == int(self.Z):
                                arr = [True, self.map_vertices[i+1]]
                                self.Collisions = arr
                            else:
                                #print(int(self.map_vertices[i+2])*self.G3Dscale, int(self.Z))
                                arr = ["Partial Detection Found",0]
                                self.Collisions = arr
                        except:
                            pass
                    else:
                        arr = [False, 0]
                        self.Collisions = arr
            except Exception as error:
                print(error)
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()