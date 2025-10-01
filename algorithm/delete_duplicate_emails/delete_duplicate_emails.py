import pandas as pd


data = {
    "id": [1, 2, 3, 4, 5],
    "email": ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
}


data = {
    "id": [1, 2, 3],
    "email": ["john@example.com", "bob@example.com", "john@example.com"]
}


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset=["email"], keep="first", inplace=True)


if __name__ == "__main__":
    df = pd.DataFrame(data)
    delete_duplicate_emails(df)
    print(df)
