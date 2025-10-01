
import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    result = patients[patients["conditions"].str.contains(
        pat=r"(^|\s)DIAB1.*")]
    return result


data = {
    "patient_id": [1, 2, 3, 4, 5],
    "patient_name": ["Daniel", "Alice", "Bob", "George", "Alain"],
    "conditions": ["YFEV COUGH", "", "DIAB100 MYOP", "ACNE DIAB100", "DIAB201"]
}
patients = pd.DataFrame(data)


if __name__ == "__main__":
    result = find_patients(patients)
    print(result)
