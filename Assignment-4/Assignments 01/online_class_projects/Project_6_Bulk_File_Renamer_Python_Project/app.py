import streamlit as st
import os
import glob
import shutil

# Set up dark mode
st.set_page_config(page_title="Bulk File Renamer", page_icon="📂", layout="centered")
dark_mode = """
    <style>
        body { background-color: #0e1117; color: white; }
        .stButton>button { background-color: #4CAF50; color: white; }
        .stTextInput>div>div>input { background-color: #262730; color: white; }
    </style>
"""
st.markdown(dark_mode, unsafe_allow_html=True)

# Function to preview renamed files
def preview_renaming(directory, prefix, replace_text, new_text, extension_filter, numbering):
    if not os.path.exists(directory):
        return "Directory does not exist!", []

    files = sorted(glob.glob(os.path.join(directory, f"*{extension_filter}")))
    if not files:
        return "No matching files found!", []

    preview_files = []
    for index, file_path in enumerate(files, start=1):
        dir_name, old_filename = os.path.split(file_path)
        new_filename = old_filename

        # Apply prefix
        if prefix:
            new_filename = f"{prefix}_{new_filename}"

        # Replace text
        if replace_text and new_text:
            new_filename = new_filename.replace(replace_text, new_text)

        # Add numbering
        if numbering:
            name, ext = os.path.splitext(new_filename)
            new_filename = f"{name}_{index}{ext}"

        preview_files.append(new_filename)

    return None, preview_files

# Function to rename files
def bulk_rename_files(directory, preview_files, extension_filter):
    if not os.path.exists(directory):
        return "Directory does not exist!"

    files = sorted(glob.glob(os.path.join(directory, f"*{extension_filter}")))
    if not files:
        return "No matching files found!"

    undo_folder = os.path.join(directory, "undo_backup")
    os.makedirs(undo_folder, exist_ok=True)

    for index, file_path in enumerate(files):
        dir_name, old_filename = os.path.split(file_path)
        new_filename = preview_files[index]

        # Backup original files
        shutil.copy(file_path, os.path.join(undo_folder, old_filename))

        new_file_path = os.path.join(dir_name, new_filename)
        os.rename(file_path, new_file_path)

    return "Files renamed successfully!"

# Function to undo renaming
def undo_rename(directory):
    undo_folder = os.path.join(directory, "undo_backup")
    if not os.path.exists(undo_folder):
        return "No backup found!"

    for file in os.listdir(undo_folder):
        original_path = os.path.join(directory, file)
        backup_path = os.path.join(undo_folder, file)
        shutil.move(backup_path, original_path)

    os.rmdir(undo_folder)  # Remove the backup folder after restoring
    return "Undo completed! Files restored."

# Streamlit UI
st.title("📂 Bulk File Renamer")
st.sidebar.header("Settings")

directory = st.text_input("Enter directory path:")
prefix = st.text_input("Enter prefix (optional):")
replace_text = st.text_input("Text to replace (optional):")
new_text = st.text_input("New text (optional):")
extension_filter = st.text_input("File extension filter (e.g., .txt, .jpg, * for all):", value="*")
numbering = st.checkbox("Add numbering (e.g., file_1.txt, file_2.txt)")

if st.button("Preview Rename"):
    if directory:
        error, preview_files = preview_renaming(directory, prefix, replace_text, new_text, extension_filter, numbering)
        if error:
            st.error(error)
        else:
            st.write("🔍 **Preview of renamed files:**")
            for old, new in zip(sorted(os.listdir(directory)), preview_files):
                st.text(f"{old} → {new}")
            st.session_state.preview_files = preview_files  # Store preview in session state
    else:
        st.warning("Please enter a valid directory.")

if st.button("Rename Files"):
    if directory and "preview_files" in st.session_state:
        result = bulk_rename_files(directory, st.session_state.preview_files, extension_filter)
        st.success(result)
    else:
        st.warning("Please preview before renaming.")

if st.button("Undo Rename"):
    if directory:
        result = undo_rename(directory)
        st.success(result)
    else:
        st.warning("Please enter a valid directory.")
