import os

def rename_files(folder, prefix="file"):
    for count, filename in enumerate(os.listdir(folder), start=1):
        ext = filename.split(".")[-1]
        new_name = f"{prefix}_{count}.{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print("✅ Files renamed successfully!")

# Example usage:
# rename_files("test_folder", prefix="outside")
