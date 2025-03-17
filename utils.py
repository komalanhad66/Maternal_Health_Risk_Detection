import config
import json
import pickle
import numpy as np

class risklevel:
    def __init__(self, Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate):
        self.Age = Age
        self.SystolicBP = SystolicBP
        self.DiastolicBP = DiastolicBP
        self.BS = BS
        self.BodyTemp = BodyTemp
        self.HeartRate = HeartRate

    def load_model(self):
        try:
            with open(config.pkl_model_path, "rb") as f:
                self.model = pickle.load(f)
            with open(config.json_file_path, "rb") as f:
                self.json_data = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Model or JSON file not found: {e}")

    def get_Risk_Level_status(self):
        try:
            self.load_model()
            input_array = np.array(
                [self.Age, self.SystolicBP, self.DiastolicBP, self.BS, self.BodyTemp, self.HeartRate],
                dtype=int,
            )
            pred_status = self.model.predict([input_array])  # Ensure input is 2D
            return pred_status[0]  # Assuming the output is a list/array
        except Exception as e:
            raise Exception(f"Error during prediction: {e}")


if __name__ == "__main__":
    Age = 25
    SystolicBP = 130
    DiastolicBP = 80
    BS = 15
    BodyTemp = 98
    HeartRate = 86

    risk_obj = risklevel(Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate)
    
    try:
        final_pred = risk_obj.get_Risk_Level_status()
        print("Predicted Maternal Health Risk Level is:", final_pred)
    except Exception as e:
        print("Error:", e)
