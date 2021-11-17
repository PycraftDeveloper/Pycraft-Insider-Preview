if not __name__ == "__main__":
    print("Started <Pycraft_SkyBoxUtil>")
    class SkyBox:
        def __init__(self):
            pass


        def LoadSkyBox(self):
            try:
                if self.aa == True:
                    im1 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS) 
                    texture1 = im1.tobytes() 
                    im2 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512, 512)) 
                    texture2 = im2.tobytes() 
                    im3 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS)
                    texture3 = im3.tobytes()
                    im4 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS)
                    texture5 = im4.tobytes() 
                    im5 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS)
                    texture4 = im5.tobytes() 
                    im6 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512, 512), self.mod_PIL_Image_.ANTIALIAS)
                    texture6 = im6.tobytes() 
                if self.aa == False:
                    im1 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\front.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512)) 
                    texture1 = im1.tobytes() 
                    im2 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\left.jpg"))).rotate(180).resize((512, 512)) 
                    texture2 = im2.tobytes() 
                    im3 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\top.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512))
                    texture3 = im3.tobytes()
                    im4 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\back.jpg"))).rotate(180).transpose(self.mod_PIL_Image_.FLIP_LEFT_RIGHT).resize((512, 512))
                    texture5 = im4.tobytes() 
                    im5 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\right.jpg"))).rotate(180).resize((512, 512))
                    texture4 = im5.tobytes() 
                    im6 = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\skybox\\bottom.jpg"))).resize((512, 512))
                    texture6 = im6.tobytes() 
                
                self.mod_OpenGL_GL_.glGenTextures(1)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 1) 
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1) 
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP) 
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP) 
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR) 
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture1) 
                
                self.mod_OpenGL_GL_.glGenTextures(2)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 2)
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture2)
                
                self.mod_OpenGL_GL_.glGenTextures(3)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 3)
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture3)
                
                self.mod_OpenGL_GL_.glGenTextures(4)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 4)
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture4)
                
                self.mod_OpenGL_GL_.glGenTextures(5)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 5)
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture5)
                
                self.mod_OpenGL_GL_.glGenTextures(6)
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 6)
                self.mod_OpenGL_GL_.glPixelStorei(self.mod_OpenGL_GL_.GL_UNPACK_ALIGNMENT, 1)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_S, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_WRAP_T, self.mod_OpenGL_GL_.GL_CLAMP)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MAG_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexParameterf(self.mod_OpenGL_GL_.GL_TEXTURE_2D, self.mod_OpenGL_GL_.GL_TEXTURE_MIN_FILTER, self.mod_OpenGL_GL_.GL_LINEAR)
                self.mod_OpenGL_GL_.glTexImage2D(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0, self.mod_OpenGL_GL_.GL_RGB, 512, 512, 0, self.mod_OpenGL_GL_.GL_RGB, self.mod_OpenGL_GL_.GL_UNSIGNED_BYTE, texture6)
            except Exception as Message:
                return Message


        def DrawSkyBox(self):
            try:
                self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_TEXTURE_2D)
                self.mod_OpenGL_GL_.glColor3f(1, 1, 1) 
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 1) 
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS) 
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0) 
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, -10.0) 
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0) 
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glEnd() 

                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0) 
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 2)
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glEnd()

                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 3)
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glEnd()

                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 4)
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0)
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0)
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glEnd()

                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 5)
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0)
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, 10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glEnd()

                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
                
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 6)
                self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_QUADS)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 0)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 0)
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, -10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(1, 1)
                self.mod_OpenGL_GL_.glVertex3f(10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glTexCoord2f(0, 1)
                self.mod_OpenGL_GL_.glVertex3f(-10.0, -10.0-50000, self.Z+10.0)
                self.mod_OpenGL_GL_.glEnd()
                self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)

                self.mod_OpenGL_GL_.glTranslate(0, 1, 0)
            except Exception as Message:
                return Message
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()