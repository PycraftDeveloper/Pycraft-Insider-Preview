if not __name__ == "__main__":
    print("Started <Pycraft_GetWorldVertex>")
    class GetMapVertices:
        def __init__(self):
            pass


        def MapModel(self):
            self.mod_OpenGL_GL_.glPushMatrix()
            #self.mod_OpenGL_GL_.glGenBuffers(1, "Store here")
            self.mod_OpenGL_GL_.glScalef(*self.Map_scale) 
            self.mod_OpenGL_GL_.glTranslatef(*self.Map_trans)
            for mesh in self.Map.mesh_list: 
                #self.mod_OpenGL_GL_.glBegin(self.mod_OpenGL_GL_.GL_TRIANGLES)
                for i in range(0, len(self.Map_IterableVertices)):
                    print("Iterating")
                    map_vertices = self.mod_Numpy__.array(self.Map_IterableVertices)
                    data = self.mod_OpenGL_Arrays_.vbo.VBO(self.mod_OpenGLContext_Array_(list(self.mod_OpenGLContext_Box_.yieldVertices( (2,2,2) )), 'f') )
                    self.mod_OpenGL_GL_.glGenBuffers(2, "VertexBufferObject")

                    self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, data)
                    self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, len(data), data, self.mod_OpenGL_GL_.GL_STATIC_DRAW)

                    #self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, data[1]);
                    #self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, len(indices), indices, self.mod_OpenGL_GL_.GL_STATIC_DRAW)
                    
                    #self.mod_OpenGL_GL_.glVertex3f(*self.Map_IterableVertices[i], sep = ',')
                #self.mod_OpenGL_GL_.glEnd()
            self.mod_OpenGL_GL_.glPopMatrix()
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()