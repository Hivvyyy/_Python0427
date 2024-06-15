import streamlit as st

st.title('這是一個測試')
st.header("Header")
st.subheader("subHeader")
st.caption("caption")
st.divider()
st.markdown("## Hello! **_World_**")
st.markdown("### 步驟1")
st.markdown("### 步驟2")
st.code('''
#Field_validator


from pydantic import BaseModel,Field,field_validator

#自動驗證
class Record(BaseModel):
    公司名稱:str = Field(alias='Name_Ins')
    登記編號:str = Field(alias='No')
    地址:str = Field(alias='Address')
    統編:str = Field(alias='tax_ID_number')
    緯度:float = Field(alias='wgs84aX')
    經度:float = Field(alias='wgs84aY')


#before
    #手動驗證（若資料內有空值or亂碼）
    @field_validator('緯度','經度',mode='before')
    @classmethod
    def abc(cls, value):
        if value == '':
            return 0.0
        else:
            return value

class Result(BaseModel):
    records:list[Record]
        ''')

st.write("## Hello! **_World_**")
"### 步驟1"
