import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the trained model and encoder
model = joblib.load('XGBoost.joblib')

# Load or create the OneHotEncoder with handle_unknown set to 'ignore'
encoder = joblib.load('ohe_encoder.pkl')
if isinstance(encoder, OneHotEncoder):
    encoder.handle_unknown = 'ignore'

# Define a function to determine the age group
def determine_age_group(age):
    if 20 <= age < 30:
        return '20-29'
    elif 30 <= age < 40:
        return '30-39'
    elif 40 <= age < 50:
        return '40-49'
    elif 50 <= age < 60:
        return '50-59'
    elif 60 <= age < 70:
        return '60-69'
    elif 70 <= age < 80:
        return '70-79'
    elif 80 <= age < 90:
        return '80-89'
    else:
        return 'Unknown'

# Define unique values for categorical fields
unique_values = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'DayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Make': ['Accura', 'BMW', 'Chevrolet', 'Dodge', 'Ferrari', 'Ford', 'Honda', 'Jaguar', 'Lexus', 'Mazda', 'Mecedes', 'Mercury', 'Nisson', 'Pontiac', 'Porche', 'Saab', 'Saturn', 'Toyota', 'VW'],
    'AccidentArea': ['Rural', 'Urban'],
    'DayOfWeekClaimed': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'MonthClaimed': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sex': ['Male', 'Female'],
    'MaritalStatus': ['Single', 'Married', 'Divorced', 'Widow'],
    'Fault': ['Policy Holder', 'Third Party'],
    'PolicyType': ['Sedan – All Perils', 'Sedan – Collision', 'Sedan - Liability', 'Sport – All Perils', 'Sport – Collision', 'Sport – Liability', 'Utility – All Perils', 'Utility – Collision'],
    'VehicleCategory': ['Sedan', 'Sport', 'Utility'],
    'VehiclePrice': ['20k-29k', '30k-39k', '40k-59k', '60k-69k', 'less than 20k', 'more than 69k'],
    'Days_Policy_Accident': ['1 to 7', '15 to 30', '8 to 15', 'none', 'more than 30'],
    'Days_Policy_Claim': ['15 to 30', '8 to 15', 'more than 30', 'none'],
    'PastNumberOfClaims': ['1', '2 to 4', 'more than 4', 'none'],
    'AgeOfVehicle': ['new', '2 years', '3', '4', '5', '6', '7', 'more than 7'],
    'AgeOfPolicyHolder': ['16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40', '41 to 50', '51 to 65', 'over 65'],
    'PoliceReportFiled': ['Yes', 'No'],
    'WitnessPresent': ['Yes', 'No'],
    'AgentType': ['External', 'Internal'],
    'NumberOfSuppliments': ['1 to 2', '3 to 5', 'none', 'more than 5'],
    'AddressChange_Claim': ['1 year', '2 to 3 years', '4 to 8 years', 'no change', 'under 6 months'],
    'NumberOfCars': ['1 Vehicle', '2 Vehicles', '3 to 4', '5 to 8', 'more than 8'],
    'BasePolicy': ['All Perils', 'Collision', 'Liability'],
    'AgeGroup': ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', 'Unknown']
}

# Define your Streamlit app
def app(st):

    # Add input fields for categorical columns
    categorical_inputs = {
        'Month': st.selectbox('Select Month', unique_values['Month']),
        'DayOfWeek': st.selectbox('Select Day of Week', unique_values['DayOfWeek']),
        'Make': st.selectbox('Select Vehicle Make', unique_values['Make']),
        'AccidentArea': st.selectbox('Select Accident Area', unique_values['AccidentArea']),
        'DayOfWeekClaimed': st.selectbox('Select Day of Week Claimed', unique_values['DayOfWeekClaimed']),
        'MonthClaimed': st.selectbox('Select Month Claimed', unique_values['MonthClaimed']),
        'Sex': st.selectbox('Select Sex', unique_values['Sex']),
        'MaritalStatus': st.selectbox('Select Marital Status', unique_values['MaritalStatus']),
        'Fault': st.selectbox('Select Fault', unique_values['Fault']),
        'PolicyType': st.selectbox('Select Policy Type', unique_values['PolicyType']),
        'VehicleCategory': st.selectbox('Select Vehicle Category', unique_values['VehicleCategory']),
        'VehiclePrice': st.selectbox('Select Vehicle Price', unique_values['VehiclePrice']),
        'Days_Policy_Accident': st.selectbox('Select Days Policy Accident', unique_values['Days_Policy_Accident']),
        'Days_Policy_Claim': st.selectbox('Select Days Policy Claim', unique_values['Days_Policy_Claim']),
        'PastNumberOfClaims': st.selectbox('Select Past Number of Claims', unique_values['PastNumberOfClaims']),
        'AgeOfVehicle': st.selectbox('Select Age of Vehicle', unique_values['AgeOfVehicle']),
        'AgeOfPolicyHolder': st.selectbox('Select Age of Policy Holder', unique_values['AgeOfPolicyHolder']),
        'PoliceReportFiled': st.selectbox('Select Police Report Filed', unique_values['PoliceReportFiled']),
        'WitnessPresent': st.selectbox('Select Witness Present', unique_values['WitnessPresent']),
        'AgentType': st.selectbox('Select Agent Type', unique_values['AgentType']),
        'NumberOfSuppliments': st.selectbox('Select Number of Suppliments', unique_values['NumberOfSuppliments']),
        'AddressChange_Claim': st.selectbox('Select Address Change Claim', unique_values['AddressChange_Claim']),
        'NumberOfCars': st.selectbox('Select Number of Cars', unique_values['NumberOfCars']),
        'BasePolicy': st.selectbox('Select Base Policy', unique_values['BasePolicy'])
    }

    # Add input fields for numerical columns
    age = st.number_input('Enter Age', min_value=16, max_value=120, value=30)
    age_group = determine_age_group(age)
    
    numerical_inputs = {
        'WeekOfMonth': st.number_input('Enter Week of Month', min_value=1, max_value=5, value=1),
        'WeekOfMonthClaimed': st.number_input('Enter Week of Month Claimed', min_value=1, max_value=5, value=1),
        'Age': age,  # Use age input directly
        'PolicyNumber': st.number_input('Enter Policy Number', min_value=0, max_value=999999, value=12345),
        'RepNumber': st.number_input('Enter Rep Number', min_value=1, max_value=16, value=1),
        'Deductible': st.number_input('Enter Deductible', min_value=0, max_value=10000, value=500),
        'DriverRating': st.number_input('Enter Driver Rating', min_value=1, max_value=4, value=3),
        'Year': st.number_input('Enter Year', min_value=1900, max_value=2100, value=2022)
    }

    # Combine all inputs into a DataFrame for encoding
    inputs_dict = {**categorical_inputs, **numerical_inputs, 'AgeGroup': age_group}
    inputs_df = pd.DataFrame([inputs_dict])

    try:
        # Ensure the data matches the expected column format for the encoder
        columns_to_encode = list(categorical_inputs.keys()) + ['AgeGroup']
        
        # Encode the inputs
        encoded_inputs = encoder.transform(inputs_df[columns_to_encode])
        
        # Convert the encoded features back to DataFrame
        encoded_inputs_df = pd.DataFrame(encoded_inputs, columns=encoder.get_feature_names_out(columns_to_encode))
        
        # Combine encoded categorical features with numerical features
        inputs_df_numerical = inputs_df[list(numerical_inputs.keys())].reset_index(drop=True)
        inputs_final = pd.concat([encoded_inputs_df, inputs_df_numerical], axis=1)
    except Exception as e:
        st.error(f"Error during preprocessing: {e}")
        return

    # When the user clicks predict
    if st.button("Predict"):
        try:
            prediction = model.predict(inputs_final)
            st.write(f"The prediction is: {'Fraud' if prediction[0] else 'Not Fraud'}")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    app(st)
