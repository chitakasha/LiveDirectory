import pandas as pd

def transform_data(df):
    """
    Transforms the input DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame to be transformed.

    Returns:
        DataFrame: The transformed DataFrame.
    """
    # Sample transformation: Create a new column that is the square of an existing column
    df['new_column'] = df['existing_column'] ** 2

    return df

if __name__ == "__main__":
    # Sample usage
    df = pd.read_csv("data/clean_data.csv")
    transformed_df = transform_data(df)
    transformed_df.to_csv("data/transformed_data.csv", index=False)

