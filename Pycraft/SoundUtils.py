if not __name__ == "__main__":
    print("Started <Pycraft_SoundUtils>")
    class PlaySound:
        def __init__(self):
            pass

        def PlayClickSound(self):
            channel1 = self.mod_Pygame__.mixer.Channel(0)
            clickMUSIC = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Click.ogg")))
            channel1.set_volume(self.soundVOL/100)
            channel1.play(clickMUSIC)
            self.mod_Pygame__.time.wait(40)

        def PlayFootstepsSound(self):
            channel2 = self.mod_Pygame__.mixer.Channel(1)
            Footsteps = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, (f"Resources\\G3_Resources\\GameSounds\\footsteps{self.mod_Random__.randint(0, 5)}.ogg")))
            channel2.set_volume(self.soundVOL/100)
            channel2.play(Footsteps)


        def PlayInvSound(self):
            channel3 = self.mod_Pygame__.mixer.Channel(2)
            InvGen = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\InventoryGeneral.ogg")))
            channel3.set_volume(self.musicVOL/100)
            channel3.play(InvGen)


        def PlayAmbientSound(self):
            channel4 = self.mod_Pygame__.mixer.Channel(3)
            LoadAmb = self.mod_Pygame__.mixer.Sound(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\GameSounds\\FieldAmb.ogg")))
            channel4.set_volume(self.soundVOL/100)
            channel4.play(LoadAmb)
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()