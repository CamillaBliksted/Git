#Exercise 1: Calculate BMI from patient measurements
import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "heightm": [1.72, 1.65, 1.81, 1.58, 1.75], 
    "weight_kg": [68, 72, 85, 54, 91],
})
patients['BMI'] = patients.weight_kg / (patients.heightm)**2
print(patients)
