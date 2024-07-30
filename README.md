# FireTimeSpanPrediction


## Temperature API Collection and Final DataFrame Formation

The original data file named "map_data.csv" is read into the jupyter notebook. Open-Meteo, a weather API, is used to get hourly temperature data between the incident date and the extinguishment date based on the coordinate values for each row in the DataFrame. The mean of the temperature values for each row is calculated and added as a new column called "mean_temperature" in the original DataFrame. The column called 'Population(SUM)' in the data file named "map_data_population_final.csv" is added to the DataFrame as another column. The month is also extracted from the 'incident_dateonly_extinguished' column to form another column titled 'month_extinguished'. The excess columns are removed from this new DataFrame and saved to be used by the model for training and testing. The final features of this DataFrame are: 'incident_administrative_unit', 'incident_county', 'incident_acres_burned', 'incident_longitude', 'incident_latitude', 'incident_type', 'calfire_incident', 'mean_temperature', 'Population' and 'month_extinguished'. The target column for this DataFrame is 'incident_days', which is separated from the features data. All rows with "NaN" values in any of the columns are also removed since they will not be helpful for model training and evaluation.  

Once this has all been completed, the categorical columns in features dataset is encoded. This encoded dataset is split into training and testing sets. Standard Scaling is conducted on the encoded features dataset (both training and testing sets) to scale any large values that may skew the model's performance. 


## Model and Performance

The Gradient Boosting Regressor is the chosen model to learn on the preprocessed dataset. This model is fitted on the training data and then is used to predict the number of incident days based on the ten supplied features. Three Gradient Boosting Regressor Models with varying parameters are created to see which one results in the best overall R2 score. The first model contains: **200 trees**, a learning_rate of **0.1**, and maximum depth of **8**. The second model has: **220 trees**, a learning_rate of **0.1**, and maximum depth of **7**. The third model is created with: **200 trees**, a learning_rate of **0.1**, and maximum depth of **6**. In terms of highest to lowest R2 scores: Model 3 has **0.817**, Model 2 has **0.813**, and Model 1 has **0.802**. Since Model 3 provides the highest R2 score, this is the model that will be used for predicting the total number of incident days. 


## Flask Website for Reader's Usage 

Flask is used to build a website that users can interact with and input their own values for the features, to which the created model will take and return its prediction to them. The user must input all 10 values, which are both categorical and numerical. For the categorical values, the user must select an option in the drop-down menu. For the numerical values, the user can input any appropriate floating number or use the up-or-down buttons on the right side of the box to select a value. The only exception is the 'Month Extinguished' box, which requires a whole number between 1 and 12 (it represents each month in a year). After all the values are input, the user can press the red button called "Predict", to which the website will show the prediction that the model calculates.          


## Acknowledgements

Thank you to the [Open-Meteo API](https://open-meteo.com/) for supplying past temperature data that was used to create the dataset the model learned from.  

Thank you to [Nitesh Malviya](https://bootsnipp.com/snippets/WMlMa) for providing the code that was used as the website template for this project. 

