import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# -------------------- Fungsi Encoding --------------------
def encoding(dataset):
    # Target
    target = 'Attrition'

    # Fitur kategorikal & numerikal
    categorical_features = ['OverTime', 'JobRole', 'MaritalStatus', 'BusinessTravel', 'Department']
    numerical_features = ['TotalWorkingYears', 'Age', 'JobLevel', 'StockOptionLevel', 'MonthlyIncome',
                          'YearsInCurrentRole', 'YearsWithCurrManager', 'JobInvolvement', 'YearsAtCompany',
                          'YearsSinceLastPromotion']

    # Bagi fitur dan target
    X = dataset.drop(columns=[target])
    y = dataset[target]

    # Pipeline preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(drop='first'), categorical_features)
        ]
    )

    # Transformasi
    X_processed = preprocessor.fit_transform(X)
    ohe_columns = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
    feature_names = numerical_features + ohe_columns.tolist()

    # DataFrame hasil encoding
    X_encoded = pd.DataFrame(X_processed, columns=feature_names)
    df_encoded = pd.concat([X_encoded, y.reset_index(drop=True)], axis=1)

    # Info tambahan
    print(f"Jumlah fitur numerik: {len(numerical_features)}")
    print(f"Jumlah kolom hasil OneHotEncoder: {len(ohe_columns)}")
    print("Encoding & scaling selesai! Berikut dimensi dataframe baru:")
    print(df_encoded.shape)

    return X_encoded, df_encoded, y

# -------------------- Fungsi Prediksi --------------------
def predict(model, X_encoded, y, dataset):
    # Tentukan kembali target (untuk drop column)
    target = 'Attrition'

    # Fitur yang digunakan model (sesuai pelatihan)
    selected_features = ['TotalWorkingYears', 'Age', 'StockOptionLevel', 'MonthlyIncome',
                         'YearsInCurrentRole', 'YearsWithCurrManager', 'JobInvolvement',
                         'YearsAtCompany', 'OverTime_Yes', 'MaritalStatus_Single']

    # Filter fitur
    X_selected = X_encoded[selected_features]

    # Prediksi dan probabilitas
    y_pred_rfc = model.predict(X_selected)
    risk_probability = model.predict_proba(X_selected)[:, 1]

    # Hasil ke DataFrame
    result_df = dataset.drop(columns=[target]).copy()
    result_df["Attrition (Actual)"] = y.values
    result_df["PredictedAttrition"] = y_pred_rfc
    result_df["Risk (Probability)"] = risk_probability

    # Akurasi
    accuracy = (y.values == y_pred_rfc).mean()

    return result_df, accuracy

# -------------------- Main Program --------------------
if __name__ == "__main__":
    # Load data prediksi
    predict_df = pd.read_csv('data_predict.csv')  # Ganti path jika perlu

    # Proses encoding
    X_encoded, _, y = encoding(predict_df)

    # Load model
    model = joblib.load('model.pkl')

    # Lakukan prediksi
    result_df, accuracy = predict(model, X_encoded, y, predict_df)

    # Simpan hasil
    result_df.to_csv('hasil_prediksi_hr.csv', index=False)
    print("\nHasil prediksi disimpan sebagai 'hasil_prediksi_hr.csv'")
    print(f"Akurasi model pada data ini: {accuracy:.4f}")
