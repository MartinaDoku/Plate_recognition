import pickle
from pathlib import Path
import streamlit_authenticator as stauth
passwords=["123"]
psw=stauth.Hasher(passwords).generate()

file_path=Path(__file__).parent/"Hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(psw,file)