if not __name__ == "__main__":
    print("Started <Pycraft_MapTextureUtil>")
    class MapTexture:
        def __init__(self):
            pass

        def LoadMapTexture(self):
            try:
                if self.aa == True:
                    file = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS) 
                    texture = file.tobytes() 
                if self.aa == False:
                    file = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\Map\\GrassTexture.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512))
                    texture = file.tobytes() 
                self.mod_OpenGL_GL_.glGenTextures(7) 
                self.mod_OpenGL_GL_.glActiveTexture(self.mod_OpenGL_GL_.GL_TEXTURE0)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 7) 
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1) 
                self.mod_OpenGL_GL_.glTexParameteri(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_MIRRORED_REPEAT) 
                self.mod_OpenGL_GL_.glTexParameteri(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_MIRRORED_REPEAT) 
                self.mod_OpenGL_GL_.glTexParameteri(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_R, self.mod_OpenGL_GL_.GL_MIRRORED_REPEAT)
                self.mod_OpenGL_GL_.glTexParameteri(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR) 
                self.mod_OpenGL_GL_.glTexParameteri(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                color = [0.0, 1.0, 0.0]
                self.mod_OpenGL_GL_.glTexParameterfv(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_BORDER_COLOR, color)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture)
                self.mod_OpenGL_GL_.glGenerateMipmap(self.mod_OpenGL_GL_.GL_TEXTURE_2D)
            except Exception as Message:
                return Message

        def DrawMapTexture(self):
            self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_TEXTURE_2D)
            self.mod_OpenGL_GL_.glColor3f(1, 1, 1)
            self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 7) 
            self.mod_OpenGL_GL_.glActiveTexture(self.mod_OpenGL_GL_.GL_TEXTURE0)
            #self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()