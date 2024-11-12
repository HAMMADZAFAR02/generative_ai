import os

import json



class FileHandler:

    #for inventory.json
    def read_file(self, filename):
        """Reads JSON content from a file and returns it as a dictionary."""
        
        """ raise exception if file not exist"""
        
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return {}

        try:
            with open(filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error decoding JSON: File is empty or not properly formatted.")
            return {}
        except IOError:
            print("An error occurred while trying to read the file.")
            return {}

    def write_file(self, filename, details):
      """Writes dictionary content as JSON into a file."""
      try:
           with open(filename, "w+" if not os.path.exists(filename) else "w") as f: # if not exist automatically make file
            f.flush()  # Ensure immediate write
            os.fsync(f.fileno())  # Force disk write
            json.dump(details, f)

      except TypeError:
          print("Invalid data type. Please provide a dictionary.")

      except Exception as e:
          print(f"An error occurred: {str(e)}")



    #for reading from users.txt
    def read_lines(self, filename):
        """Reads line-by-line user data from a file and returns it as a list of strings."""
       
        try:
        # Open the file in "a+" mode: read and append if exists, # if not exist automatically make file
         with open(filename, "a+") as f:
            f.seek(0)  # Move the pointer to the beginning of the file to read it
            return f.readlines()
        except Exception as e:
         print(f"Error reading {filename}: {e}")
        return []

    #used for writing in users.txt
    def write_line(self, filename, line):
        """Appends a line to a text file."""
        try:
         with open(filename, "a+" if not os.path.exists(filename) else "a") as f: #create automatically if not exist
            f.write(line + "\n")
        except Exception as e:
            print(f"an error occured {str(e)}")
