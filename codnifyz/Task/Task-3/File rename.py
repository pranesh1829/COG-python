import os

def rename_files(directory_path, prefix):
    try:
      
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

      
        os.chdir(directory_path)

        # List all files in the directory
        files = [file for file in os.listdir() if os.path.isfile(file)]

      
        for i, file in enumerate(files, start=1):
            file_extension = os.path.splitext(file)[1]
            new_name = f"{prefix}_{i:03d}{file_extension}"
            os.rename(file, new_name)

        print("Files successfully renamed!")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    directory_path = r"D:\abc.txt"
    prefix = "document"

    rename_files(directory_path, prefix)
