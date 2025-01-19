import streamlit as st

from web_function import predict

def app(aids_df, x, y):

    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        time = st.text_input('Input Nilai time')
        trt = st.text_input('Input Nilai trt')
        age = st.text_input('Input Nilai age')
        wtkg = st.text_input('Input Nilai wtkg')
        hemo = st.text_input('Input Nilai hemo')
        homo = st.text_input('Input Nilai homo')
        drugs = st.text_input('Input Nilai drugs')

    with col2:
        karnof = st.text_input('Input Nilai karnof')
        oprior = st.text_input('Input Nilai oprior')
        z30 = st.text_input('Input Nilai z30')
        preanti = st.text_input('Input Nilai preanti')
        race = st.text_input('Input Nilai race')
        gender = st.text_input('Input Nilai gender')
        str2 = st.text_input('Input Nilai str2')

    with col3:
        strat = st.text_input('Input Nilai strat')
        symptom = st.text_input('Input Nilai symptom')
        treat = st.text_input('Input Nilai treat')
        offtrt = st.text_input('Input Nilai offtrt')
        cd40 = st.text_input('Input Nilai cd40')
        cd420 = st.text_input('Input Nilai cd420')
        cd80 = st.text_input('Input Nilai cd80')
        cd820 = st.text_input('Input Nilai cd820')

    features =[time,trt,age,wtkg,hemo,homo,drugs,karnof,oprior,z30,preanti,race,gender,str2,strat,symptom,treat,offtrt,cd40,cd420,cd80,cd820]

    # tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses..")

        if (prediction == 1):
            st.warning("Orang tersebut rentan Terindikasi")
        else:
            st.success("Orang tersebut relatif Aman")

        st.write("Model yang digunakan memiliki tingkat Akurasi ", (score*100),"%")
