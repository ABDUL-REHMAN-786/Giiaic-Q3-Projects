import streamlit as st
import os
import shutil
from pathlib import Path

# Function to rename files
def rename_files(folder_path, prefix, suffix, replace_old, replace_new):
    renamed_files = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_name = filename
            
            # Apply prefix and suffix
            if prefix:
                new_name = prefix + new_name
            if suffix:
                new_name = new_name + suffix
            
            # Replace old text with new text in filenames
            if replace_old and replace_new:
                new_name = new_name.replace(replace_old, replace_new)

            # Rename the file
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)
            os.rename(old_file_path, new_file_path)
            renamed_files.append((filename, new_name))
    
    return renamed_files

# Streamlit UI setup
st.title("Bulk File Renamer")

st.write("Upload a folder containing the files you want to rename.")

# File upload
uploaded_folder = st.file_uploader("Upload a Folder", type=None, accept_multiple_files=True)

if uploaded_folder:
    temp_dir = Path("temp_folder")
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Unzip files if a ZIP folder is uploaded
    for uploaded_file in uploaded_folder:
        with open(temp_dir / uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
    
    st.write(f"Files have been uploaded to {temp_dir}.")
    
    # Input for renaming rules
    prefix = st.text_input("Prefix (optional)")
    suffix = st.text_input("Suffix (optional)")
    replace_old = st.text_input("Text to replace (optional)")
    replace_new = st.text_input("Replace with (optional)")
    
    if st.button("Rename Files"):
        # Rename the files according to the rules
        renamed_files = rename_files(temp_dir, prefix, suffix, replace_old, replace_new)
        
        # Display the renamed files
        st.write("Renamed Files:")
        for old_name, new_name in renamed_files:
            st.write(f"{old_name} -> {new_name}")
        
        # Provide download option for the renamed files
        zip_file_name = "renamed_files.zip"
        shutil.make_archive(zip_file_name.replace(".zip", ""), 'zip', temp_dir)
        st.download_button(
            label="Download Renamed Files",
            data=open(zip_file_name, "rb").read(),
            file_name=zip_file_name
        )
    
    # Clean up
    shutil.rmtree(temp_dir)
