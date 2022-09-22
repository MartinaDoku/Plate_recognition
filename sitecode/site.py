from imaplib import _Authenticator
from ssl import Options
import streamlit  as st
from dat import datamanager
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import pandas as pd
st.set_page_config(layout="wide")
name="admin"
user="admin"
app=st.set_page_config
file_path=Path(__file__).parent/"Hashed_pw.pkl"
with file_path.open("rb") as file:
    psw=pickle.load(file)
credentials={"usernames":{
    user:{
        "email":" ",
        "name":name,
        "password":psw[0]
    }
}
}
authenticator=stauth.Authenticate( credentials,"name","123",1)
name,authentication_status,username=authenticator.login("Login","main")
if authentication_status == False:
    st.error("Password incorrect")
if authentication_status == None:
    st.warning("please enter username and password")
if authentication_status == True:
    database=datamanager()
    authenticator.logout("logout","sidebar")
   # st.session_state["ada"]="See saved Plates"
    options=st.sidebar.radio("Pages",["See saved Plates","Add Plate","Remove Plate","Change Password"],key="ada")
    if options== "See saved Plates":
            dt=pd.DataFrame(database.getplate(),columns=("Plate Number","Insertion Date","Expiring Date"))
            st.dataframe(dt,width=10000)

    if options == "Add Plate":
        with st.form("Add your Plate"):
            multiple_plates = st.checkbox("click this if you want to add multiple plates",False,"add_check")
            plate=st.text_input("",value="",max_chars=8)
            submitted = st.form_submit_button("Submit")
            if submitted:
                add=database.addplate(plate)
                if  not multiple_plates:
                    del st.session_state["ada"]
                    st.experimental_rerun()
    
    if options == "Remove Plate":
        with st.form("Add your Plate"):
            plates = st.multiselect("select the plates to remove :", database.getonlyplate())
            submitted = st.form_submit_button("Submit")
            if submitted:
                for plate in plates:
                    database.removeplate(plate)
                del st.session_state["ada"]
                st.experimental_rerun()