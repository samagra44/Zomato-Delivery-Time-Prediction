# Zomato Delivery Time Prediction Application

## Project Overview

The Zomato Delivery Time Prediction Application is a machine learning-driven Flask web application designed to predict the estimated delivery time for food orders placed on the Zomato platform. This project has been built from scratch, encompassing all the essential files and folders required for a real-world data science project. The application uses a machine learning model to provide users with accurate delivery time estimates.

### Project Structure

The project directory structure consists of the following folders and files:

- **Artifact:** This folder contains any artifacts or model-related files generated during the project.

- **config:** The config folder stores configuration files or settings required for the application.

- **data:** The data folder contains datasets or any data files necessary for training and testing the machine learning model.

- **env:** This folder may contain environment-specific configurations or virtual environment files for the project.

- **logs:** Logs related to the application can be found here. These logs can help in debugging and monitoring the application.

- **Prediction:** This folder could contain any specific prediction-related files or scripts.

- **src:** The src folder is where the main source code for the application resides. It includes the logic for data preprocessing, machine learning model training, and Flask web app development.

- **templates:** This folder holds the HTML templates used for rendering the web interface of the application.

- **app.py:** The main application file where the Flask web app is defined and configured. This is the entry point of the application.

- **exception.py:** This folder may contain scripts or files related to handling exceptions or errors in the application.

- **logs.py:** A script or module responsible for logging actions and events in the application.

- **requirements.txt:** A list of Python dependencies and packages required to run the application.

- **setup.py:** A setup script for configuring and installing the application and its dependencies.

### Application Workflow

1. **Data Collection:** The data required for the prediction model is stored in the 'data' folder. This dataset likely contains features such as order details, restaurant information, and historical delivery times.

2. **Data Preprocessing:** Data preprocessing tasks, such as cleaning, feature engineering, and data transformation, are performed in the 'src' folder. These processed data are used to train the machine learning model.

3. **Machine Learning Model:** The machine learning model, built using libraries like scikit-learn or TensorFlow, is trained using the preprocessed data. The model's goal is to predict delivery times based on various input features.

4. **Flask Web Application:** The Flask web application is defined in 'app.py'. It serves as the user interface for the prediction. Users can input order details, such as restaurant selection and order contents.

5. **Prediction:** Upon receiving user input, the Flask app uses the trained machine learning model to predict the estimated delivery time.

6. **User Interface:** The HTML templates in the 'templates' folder define the user interface, which displays the predicted delivery time to the user.

7. **Logging and Exception Handling:** The 'logs.py' and 'exception' folders contain code for logging application actions and handling errors gracefully.

### Running the Application

To run the Zomato Delivery Time Prediction Application:

1. Install the necessary Python dependencies listed in 'requirements.txt'.
2. Execute 'app.py' to start the Flask web server.
3. Access the application by navigating to `http://localhost:8888` in your web browser.

### 1. Create  New Environment
```
**conda create -p env puthon==3.9 -y**
```
### 2. Activate conda environment
### for CMD
```
**conda activate env/**
```
### for bash
```
**source activate env/**
```
### 3. Install requirements file
```
**pip install -r requirements.txt**
```
### 4. Running the Application
```
**python app.py**
```

### Additional Notes

- Make sure to set up the environment and data as required before running the application.
- This README provides an overview of the project structure and workflow. For more detailed instructions and documentation, refer to specific files or folders within the project.

### Acknowledgments

This project was developed by Samagra Shrivastava as a demonstration of machine learning and web application development skills. Feel free to explore the code and contribute to its improvement. If you have any questions or feedback, please don't hesitate to contact samagra6424@gmail.com.

**Happy predicting and happy coding!**
