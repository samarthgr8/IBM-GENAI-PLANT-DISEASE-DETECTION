import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("plant_model.h5")


# -----------------------------------------
# CLASSES
# -----------------------------------------

classes = [

'Pepper__bell___Bacterial_spot',
'Pepper__bell___healthy',
'Potato___Early_blight',
'Potato___Late_blight',
'Potato___healthy',
'Tomato_Bacterial_spot',
'Tomato_Early_blight',
'Tomato_Late_blight',
'Tomato_Leaf_Mold',
'Tomato_Septoria_leaf_spot',
'Tomato_Spider_mites_Two_spotted_spider_mite',
'Tomato__Target_Spot',
'Tomato__Tomato_YellowLeaf__Curl_Virus',
'Tomato__Tomato_mosaic_virus',
'Tomato_healthy'

]


# -----------------------------------------
# SOLUTIONS
# -----------------------------------------

solutions = {

"Tomato_Early_blight":
"Apply fungicide and remove infected leaves immediately.",

"Tomato_Late_blight":
"Avoid overwatering and use copper fungicides.",

"Tomato_Leaf_Mold":
"Improve air circulation and avoid excessive humidity.",

"Tomato_healthy":
"Your plant is healthy. Keep monitoring regularly.",

"Potato___Early_blight":
"Apply suitable fungicide and maintain proper spacing.",

"Potato___Late_blight":
"Remove infected leaves and use disease resistant varieties.",

"Potato___healthy":
"No treatment required. Maintain proper nutrition.",

"Pepper__bell___healthy":
"Your plant is healthy.",

"Pepper__bell___Bacterial_spot":
"Use copper-based sprays and avoid overhead watering."

}




st.markdown("""
<style>
/* Import a clean, modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* Main Background */
.stApp {
    background-color: #F4F9F4; 
    font-family: 'Inter', sans-serif;
}

/* Main Text */
html, body, [class*="css"] {
    color: #2D3748;
}

/* Headings */
h1, h2, h3 {
    color: #1A5319 !important;
    font-weight: 700;
}
h4 {
    color: #4A5568 !important;
    font-weight: 600;
}

/* =========================================
   PREMIUM MAIN ACTION BUTTONS
   ========================================= */

.stButton>button {
    background: linear-gradient(135deg, #2ECC71 0%, #16A34A 100%);
    color: white !important;
    border-radius: 25px; 
    border: none;
    height: 55px;
    width: 250px;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 15px rgba(22, 163, 74, 0.3);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
}

.stButton>button:hover {
    background: linear-gradient(135deg, #34D399 0%, #059669 100%);
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 8px 25px rgba(5, 150, 105, 0.4);
}

.stButton>button:active {
    transform: translateY(1px) scale(0.98);
    box-shadow: 0 2px 10px rgba(5, 150, 105, 0.3);
}

/* =========================================
   ENHANCED FILE UPLOADER (DROPZONE)
   ========================================= */

[data-testid="stFileUploader"] {
    background-color: #F8FBF8; 
    border: 5px dashed #4ADE80;
    border-radius: 20px; 
    padding: 30px 20px;
    box-shadow: inset 0 0 15px rgba(74, 222, 128, 0.05); 
    transition: all 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    border-color: #16A34A;
    background-color: #F0FDF4;
    box-shadow: inset 0 0 20px rgba(22, 163, 74, 0.1), 0 8px 16px rgba(0,0,0,0.05);
    transform: translateY(-2px);
}

/* Ensure general text inside uploader is dark and readable */
[data-testid="stFileUploader"] * {
    color: #2D3748;
}

/* =========================================
   "BROWSE FILES" BUTTON SPECIFIC STYLING
   ========================================= */

[data-testid="stFileUploader"] button {
    background-color: #E8F5E9 !important; /* Beautiful, light mint green */
    color: #1A5319 !important; /* Deep green text for readability */
    border: 1px solid #689469 !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
    box-shadow: none !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #C8E6C9 !important; /* Slightly deeper green on hover */
    border-color: #81C784 !important;
    color: #1A5319 !important;
}

/* =========================================
   ALERTS / NOTIFICATIONS
   ========================================= */

.stSuccess {
    background-color: #D1E7DD;
    color: #0F5132;
    border-left: 5px solid #198754;
    border-radius: 8px;
}
.stInfo {
    background-color: #CFF4FC;
    color: #055160;
    border-left: 5px solid #0DCAF0;
    border-radius: 8px;
}
.stError {
    background-color: #F8D7DA;
    color: #842029;
    border-left: 5px solid #DC3545;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------------
# TITLE
# -----------------------------------------

st.markdown(
"""
<h2 style='text-align:center;'>
🌿 Plant Disease Detection (Krishi Setu)
</h2>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<h4 style='text-align:center;'>
AI Powered Plant Health Monitoring System
</h4>
""",
unsafe_allow_html=True
)


st.divider()


# -----------------------------------------
# FILE UPLOAD
# -----------------------------------------

image = st.file_uploader(

"Upload Plant Leaf Image",

type=["jpg", "png", "jpeg"]

)



# -----------------------------------------
# PREDICTION
# -----------------------------------------

if image is not None:

    st.image(
        image,
        caption="Uploaded Image",
        width=350
    )

    img = Image.open(image)

    img = img.resize((128, 128))

    img_array = np.array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )


    if st.button("Predict Disease"):


        with st.spinner("Detecting Disease...."):

            prediction = model.predict(img_array)


        index = np.argmax(prediction)

        confidence = np.max(prediction) * 100

        disease = classes[index]


        # -----------------------------------------
        # LOW CONFIDENCE CHECK
        # -----------------------------------------

        if confidence < 70:

            st.error(
                "Unable to identify the disease confidently. Please upload a clearer plant leaf image."
            )


        else:

            st.success(
                f"Disease Detected : {disease}"
            )


            st.info(
                f"Confidence : {confidence:.2f}%"
            )


            # Progress Bar

            st.progress(float(confidence/100))



            if disease in solutions:

                st.write(
                    solutions[disease]
                )

            # else:
            #
            #     st.write("""
            #     • Consult agricultural experts.
            #
            #     • Use suitable fungicides.
            #
            #     • Regularly monitor the plant.
            #
            #     • Remove infected leaves if necessary.
            #     """)








            st.success(
                "Prediction Completed Successfully."
            )

