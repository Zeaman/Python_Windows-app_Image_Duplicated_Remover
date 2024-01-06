# Duplicated Image Remover Tool
## Description
This Python application provides a simple and user-friendly GUI for removing duplicated images in bulk. The tool is built using the Dhash algorithm.
Dhash, short for "difference hash," is a type of perceptual hashing algorithm used in image processing and computer vision. Perceptual hashing involves generating a unique hash value for an image based on its visual content. Dhash specifically focuses on capturing differences in pixel intensities between adjacent pixels in an image. The Dhash algorithm typically works by converting an image to grayscale, resizing it to a small fixed size, and then comparing the intensity difference between adjacent pixels. The resulting hash is a compact representation of the image's visual features, making it useful for tasks like image similarity comparison, duplicate detection, and near-duplicate image retrieval.

## Features
- Find the duplicated file(s) from the given dirctory.
- If found, remove the duplicate image-file.

## Usage
1. Download the repository or clone it to your local machine.
2. Run the executable file (`Duplicated_Remover_GUI.exe`) on Windows or execute the Python script directly (`Duplicated_Remover_GUI.py` on other platforms).
3. The GUI will prompt you to provide the source folder od the images stored.
4. It will automatically hand the task after the source specified by the user
5. For double-check; click the "Submit" button to find and delete duplicated image file(s).
6. A success message will be displayed once all files are successfully processed.

## Screenshots
### Icon of the APP:
![Application Screenshot](https://github.com/Zeaman/Python_Windows-app_Image_Duplicated_Remover/blob/main/iconTwo.jpg)
### GUI:
![Application Screenshot](https://github.com/Zeaman/Python_Windows-app_Image_Duplicated_Remover/blob/main/screenshoot1.PNG)
### Success:
![Application Screenshot](https://github.com/Zeaman/Python_Windows-app_Image_Duplicated_Remover/blob/main/screenshoot2.PNG)


## Dependencies
- Python 3.10
- Tkinter

## Contributions
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
