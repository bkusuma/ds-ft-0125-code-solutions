def load_data():
    import pandas as pd

    file_path = "../../house-prices-advanced-regression-techniques/input/test.csv"
    houses = pd.read_csv(file_path)

    return houses


def porch_func(X):
    import pandas as pd
    from sklearn import set_config

    set_config(transform_output="pandas")

    porches = pd.DataFrame(X.sum(axis=1), columns=["porch_cols"])
    return porches


def preprocess(df):
    import pandas as pd
    from sklearn import set_config

    set_config(transform_output="pandas")
    ids = df.pop("Id")

    df.drop(columns=["MiscFeature", "MSSubClass"], inplace=True)

    import joblib

    preprocessor = joblib.load("fitted_preprocessor.joblib")
    df_proc = preprocessor.transform(df)

    df_proc = pd.concat([ids, df_proc], axis=1)
    return df_proc


def model(df_proc):
    import pandas as pd
    import numpy as np
    from sklearn import set_config

    set_config(transform_output="pandas")

    ids = df_proc.pop("Id")

    import joblib

    model = joblib.load("model.joblib")
    preds = model.predict(df_proc)
    preds = np.exp(preds)
    output = pd.DataFrame({"Id": ids, "SalePrice": preds})
    return output
