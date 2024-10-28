import streamlit as st
import numpy as np
import joblib
import pandas as pd

model_path = "artifacts/model_trainer/model.joblib"
model = joblib.load(model_path)

expected_features = model.feature_names_in_

# Title and input form
st.title("Disease Prognosis Prediction")
st.write("Please enter the symptoms below to predict the disease prognosis.")

input_data = {}
for symptom in expected_features:
    input_data[symptom] = st.number_input(symptom, min_value=0, max_value=1, step=1, value=0)

input_df = pd.DataFrame([input_data])

missing_columns = set(expected_features) - set(input_df.columns)
for col in missing_columns:
    input_df[col] = 0  # Set default value for missing columns

input_df = input_df[expected_features]

if st.button("Predict"):
    try:
        prediction = model.predict(input_df)
        st.write("The predicted prognosis is:", prediction[0])
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")


# import streamlit as st
# import joblib
# import numpy as np

# # Load the model
# model_path = "artifacts/model_trainer/model.joblib"  # Adjust the path if needed
# try:
#     model = joblib.load(model_path)
#     if not hasattr(model, "predict"):
#         st.error("The loaded model does not have a predict method.")
# except Exception as e:
#     st.error(f"Failed to load the model. Error: {e}")

# # Title and description
# st.title("Disease Prognosis Prediction")
# st.write("Enter the symptoms and click Predict to get the prognosis.")

# # Input fields for symptoms
# symptoms = [
#     "abdominal_pain", "abnormal_menstruation", "acidity", "acute_liver_failure", "altered_sensorium", 
#     "anxiety", "back_pain", "belly_pain", "blackheads", "bladder_discomfort", "blister", "blood_in_sputum", 
#     "bloody_stool", "blurred_and_distorted_vision", "breathlessness", "brittle_nails", "bruising", 
#     "burning_micturition", "chest_pain", "chills", "cold_hands_and_feets", "coma", "congestion", 
#     "constipation", "continuous_feel_of_urine", "continuous_sneezing", "cough", "cramps", "dark_urine", 
#     "dehydration", "depression", "diarrhoea", "dischromic_patches", "distention_of_abdomen", "dizziness", 
#     "drying_and_tingling_lips", "enlarged_thyroid", "excessive_hunger", "extra_marital_contacts", 
#     "family_history", "fast_heart_rate", "fatigue", "fluid_overload", "foul_smell_of_urine", "headache", 
#     "high_fever", "hip_joint_pain", "history_of_alcohol_consumption", "increased_appetite", "indigestion", 
#     "inflammatory_nails", "internal_itching", "irregular_sugar_level", "irritability", "irritation_in_anus", 
#     "itching", "joint_pain", "knee_pain", "lack_of_concentration", "lethargy", "loss_of_appetite", 
#     "loss_of_balance", "loss_of_smell", "malaise", "mild_fever", "mood_swings", "movement_stiffness", 
#     "mucoid_sputum", "muscle_pain", "muscle_wasting", "muscle_weakness", "nausea", "neck_pain", 
#     "nodal_skin_eruptions", "obesity", "pain_behind_the_eyes", "pain_during_bowel_movements", 
#     "pain_in_anal_region", "painful_walking", "palpitations", "passage_of_gases", "patches_in_throat", 
#     "phlegm", "polyuria", "prominent_veins_on_calf", "puffy_face_and_eyes", "pus_filled_pimples", 
#     "receiving_blood_transfusion", "receiving_unsterile_injections", "red_sore_around_nose", 
#     "red_spots_over_body", "redness_of_eyes", "restlessness", "runny_nose", "rusty_sputum", "scurring", 
#     "shivering", "silver_like_dusting", "sinus_pressure", "skin_peeling", "skin_rash", "slurred_speech", 
#     "small_dents_in_nails", "spinning_movements", "spotting_urination", "stiff_neck", "stomach_bleeding", 
#     "stomach_pain", "sunken_eyes", "sweating", "swelled_lymph_nodes", "swelling_joints", 
#     "swelling_of_stomach", "swollen_blood_vessels", "swollen_extremeties", "swollen_legs", 
#     "throat_irritation", "toxic_look_typhos", "ulcers_on_tongue", "unsteadiness", "visual_disturbances", 
#     "vomiting", "watering_from_eyes", "weakness_in_limbs", "weakness_of_one_body_side", "weight_gain", 
#     "weight_loss", "yellow_crust_ooze", "yellow_urine", "yellowing_of_eyes", "yellowish_skin"
# ]

# # Collect symptom inputs from the user
# input_data = []
# for symptom in symptoms:
#     value = st.number_input(f"{symptom.replace('_', ' ').title()}", min_value=0, max_value=1, step=1, value=0)
#     input_data.append(value)

# # Convert input data to numpy array and reshape
# input_data = np.array(input_data).reshape(1, -1)

# # Prediction button
# if st.button("Predict"):
#     try:
#         # Ensure model has a predict method
#         if hasattr(model, "predict"):
#             prediction = model.predict(input_data)
#             st.success(f"The predicted prognosis is: {prediction[0]}")
#         else:
#             st.error("Model does not support predictions.")
#     except Exception as e:
#         st.error(f"An error occurred during prediction: {e}")
