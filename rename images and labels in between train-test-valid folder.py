import os
def rename_files(image_folder, label_folder, prefix="04_"):
    image_ext = ".jpg"  # Change if needed (e.g., .png)
    label_ext = ".txt"  # Change if needed

    # Get sorted lists of image and label files
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(image_ext)])
    label_files = sorted([f for f in os.listdir(label_folder) if f.endswith(label_ext)])

    # Debug: Print detected files
    print(f"Processing:\nImages: {image_folder}\nLabels: {label_folder}")
    print("Detected Images:", image_files)
    print("Detected Labels:", label_files)

    # Ensure the number of images and labels match
    if len(image_files) != len(label_files):
        print("Error: Number of images and labels do not match!")
        return

    # Rename files sequentially
    for index, (img, lbl) in enumerate(zip(image_files, label_files), start=1):
        new_name = f"{prefix}{index:03d}"
        new_image_name = f"{new_name}{image_ext}"
        new_label_name = f"{new_name}{label_ext}"

        # Full paths for renaming
        old_img_path = os.path.join(image_folder, img)
        old_lbl_path = os.path.join(label_folder, lbl)
        new_img_path = os.path.join(image_folder, new_image_name)
        new_lbl_path = os.path.join(label_folder, new_label_name)

        # Rename files
        try:
            os.rename(old_img_path, new_img_path)
            os.rename(old_lbl_path, new_lbl_path)
            print(f"Renamed: {img} -> {new_image_name}, {lbl} -> {new_label_name}")
        except Exception as e:
            print(f"Error renaming {img} or {lbl}: {e}")

    print("Renaming complete!\n")

# Set the folder paths for images and labels
train_image_folder = r"C:\Users\USER\Downloads\Apllecounting2.v1i.yolov11\test\images"  # Change this to the actual image folder path
train_label_folder = r"C:\Users\USER\Downloads\Apllecounting2.v1i.yolov11\test\labels"  # Change this to the actual label folder path

rename_files(train_image_folder, train_label_folder)