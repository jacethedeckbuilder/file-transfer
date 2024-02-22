#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
import glob


# In[6]:


def move_from_gdrive(path,filetype):
    #
    files = [f for f in os.listdir(Gdrive+path) if filetype in f.lower()]
    #loops through the files so that they can be moved
    for file in files:
        #gets the file path
        new_Dpath = Ddrive+path+file
        
        #get the new destination path path
        new_Gpath = Gdrive+path+file
        
        #this gets the last folder in the path   
        folder_path="/".join(new_Dpath.split('/')[0:-1])
    
        #this checks if the folder exists in the desinated folder          
        #if it doesn't exist than it creates the folder path thus keeping the structure the same
        if not os.path.isdir(folder_path): os.makedirs (folder_path)
            
        #prints the original path and the the new path. 
        print("received:"+(new_Gpath))
        print("sent: "+(new_Dpath))
        print("*"*25))
        
        #this try statement is there to let the computer run if it gets an access denied or file can't be moved error
        #so that the program can run until all of the others can be moved
        try:
            #moves the file from to the destination folder
            shutil.move(new_Gpath, new_Dpath) 
        except:
            #if there is an error it prints where the error took place
            print("there was an error trying to move :"+str(file))
            #then continues through the rest of the files
            continue
        finally:
            print()
            


# In[7]:


def delete_empty_folders(root):
    #creates a set named delete
    deleted = set()
    
    #loops through the paths
    for current_dir, subdirs, files in os.walk(root, topdown=False):
        
        #this tells whether or not there are any subfolders automaticly set to false 
        still_has_subdirs = False
        
        #loops through the sub directories 
        for subdir in subdirs:
            #checks for subdirectories that haven't been set to deleted
            if os.path.join(current_dir, subdir) not in deleted:
                #there is a subdirs so it is set too true
                still_has_subdirs = True
                break
        #checks to see if there are any files and, checks to see if there are other directories 
        if not any(files) and not still_has_subdirs:
            #deletes the folder
            os.rmdir(current_dir)
            
            #adds the current directory to the set deleted
            deleted.add(current_dir)
            
    #returns all of the files that have been deleted. 
    return deleted



# In[8]:


def new_move_function():
    #
    extensions = set()
    directory_list = list()
    
    # so that the orignal file can be scrapped
    directory_list.append("") 
    #walks though the folder
    for dirpath, dirnames, filenames in os.walk(Gdrive):
        #
        for name in dirnames:
            #adds the directory name to the folder. 
            directory_list.append(os.path.join(dirpath, name))
        #
        for file in filenames:
            #adds the extention to the list of paths 
            extensions.add(os.path.splitext(file)[1])

    #
    for dirs in directory_list:
        #
        for fileext in extensions:
            #checks to see if the file is a google file and skips it
            if(fileext!=".gsheet" and fileext!=".gdoc" and fileext!=".gsite"):
                #moves the file on the path
                move_from_gdrive(dirs[len(Ddrive):]+'/',fileext)
            else:
                #lets the user know that there was a google file that can't be tranfered
                print("can't move "+Gdrive+dirs[len(Ddrive):]+'/'+" google file")
                print()
    #clean up the empty folders
    delete_empty_folders(Gdrive)


# In[21]:


#
def set_origin_folder():
    #
    orign_path=input("enter the folder you wish the files to be moved from: ")
    
    #checks to see if the path exists
    if(os.path.exists(orign_path)):
        #if it does make sure the folder isn't empty 
        if(len(os.listdir(orign_path))!=0):
            #continue
            print("the orgin folder has been set as: "+orign_path)
        else:
            #if the folder is empty let the user enter a new folder
            print("the folder you selected is empty please choose a new folder")
            #then restart until the user starts again returns the correct input
            orign_path=set_origin_folder()
    else:
        #if the path doesn't exist let the user know and let them enter a new folder 
        print("this path doesn't exist please try again")
        #then restart until the user starts again returns the correct input
        orign_path=set_origin_folder()
    #returns the path
    return orign_path

#    
def set_destination_folder():
    #
    destination_path= input("enter the folder you wish the files to be directed too: ")
    #checks to see if the path exists
    if(os.path.exists(destination_path)):
        #if it let the user know
        print("the destination folder has been set as: "+destination_path)
    else:
        #if the path doesn't exist then create a folder in that path
        os.mkdir(destination_path)
        print("the folder was created")
    
    #returns the path
    return destination_path


# In[22]:


#sets the choosen path
Gdrive=set_origin_folder()
Ddrive=set_destination_folder()

#checks to make sure that the paths entered aren't the same
if(Gdrive!=Ddrive):
    #then let the user know that the file tranfer has started
    print("the moving process has started")
    print('_'*75)
    #starts the move proccess
    new_move_function()
else:
    #lets the user know they have entered the same path
    print()
    print("the path you selected is the same please try again")
    #lets the user enter a new file path
    Gdrive=set_origin_folder()
    Ddrive=set_destination_folder()
print("proccess is done")


# In[ ]:




