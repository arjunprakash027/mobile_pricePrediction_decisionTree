import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('mobile_phone_price.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def show_predict_page():
    st.title('mobile price prediction')
    st.write("""### Give us your preferance""")


    bluetooth = (
        1,
        0,
    )

    dual_sim = (
        1,
        0,
    )

    fourg = (
        1,
        0,
    )

    threeg = (
        1,
        0,
    )

    touchscreen = (
        1,
        0,
    )

    wifi = (
        1,
        0,
    )

    battery_powers = st.slider("battery capacity",0,2000,300)
    bluetooths = st.selectbox("bluetooth",bluetooth)
    dual_sims = st.selectbox("dual sim",dual_sim)
    internal_mems = st.slider("internal storage",0,64,4)
    rams = st.slider("ram",0,4000,0)
    fourgs = st.selectbox("4g",fourg)
    threegs = st.selectbox("3g",threeg)
    touchscreens = st.selectbox("touchscreen",touchscreen)
    wifis = st.selectbox("wifi",wifi)
    fc = st.slider('front cam mp',0,20,0)
    pc = st.slider('back cam mp',0,20,0)

    predx = [battery_powers,bluetooths,dual_sims,fc,fourgs,internal_mems,pc,rams,threegs,touchscreens,wifis]
    predxnp = np.array(predx)
    predxnp = predxnp.reshape(1,-1)
    print(predxnp)

    "yes" == 1
    "no" == 0

    ok = st.button("calculate price")

    if ok:
        price = data.predict(predxnp)
        if price[0] == 0.0:
            st.subheader(f"This falls under the category of 500rs to 2500rs")
        elif price[0] == 1.0:
            st.subheader(f"This falls under the category 2500rs to 5000rs")
        else:
            st.subheader(f"This falls under the category 5000rs to 10000rs")


