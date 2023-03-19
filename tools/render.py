import os
from subprocess import call


# call(["ls", "-l"]

class Renderer:
    def __init__(self):
        pass

    def render(self):
        os.chdir("..")
        print(os.getcwd())
        #######################
        # get list of all folders in this directory
        ######################
        my_directories = [f.path for f in os.scandir(os.getcwd()) if f.is_dir()]
        pdf_direc = []
        for directory in my_directories:
            if 'pdf' in [x.name for x in os.scandir(directory)]:
                pdf_direc.append(directory)

        print(pdf_direc)
        ####################
        # Go through those directories and find all the .md files and then create the pdf
        ####################
        for directory in pdf_direc:
            print(directory)
            os.chdir(directory)
            md_files = [my_file.name for my_file in os.scandir(directory) if my_file.name[-3:] == ".md"]
            print(md_files)
            ################
            # pandoc those files
            ################
            for file in md_files:
                self.process_file(directory, file)

    def process_file(self, direc: str, filename:str):
        os.chdir(direc)
        file1 = open(filename, "r")
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        commands = [line.strip()[10:].strip() for line in Lines if line.strip()[:10] == "[comment]:"]
        print(commands)
        # TODO: Make the landscape command
        if 'render' in commands:
            call(["pandoc", "-s", direc + "/" + filename, "-o", direc + "/pdf/" + filename[:-3] + '.pdf'])


if __name__ == '__main__':
    # Renderer.render()
    r = Renderer()
    #r.process_file("/Users/mbardoe/Documents/GitHub/CS570-ClassNotes/Homework_Handouts", 'HW_1.md')
    r.render()