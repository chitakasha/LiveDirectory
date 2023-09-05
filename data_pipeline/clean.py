import pandas as pd

def clean_data(df):
    """
    Cleans the input DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame to be cleaned.

    Returns:
        DataFrame: The cleaned DataFrame.
    """
    # Remove any null values
    df.dropna(inplace=True)

    # Convert all strings to lowercase
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # Remove any special characters
    df = df.replace(r"[^\w\s]", "", regex=True)

    return df

if __name__ == "__main__":
    # Sample usage
    df = pd.read_csv("data/raw_data.csv")
    clean_df = clean_data(df)
    clean_df.to_csv("data/clean_data.csv", index=False)

