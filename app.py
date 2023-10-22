import streamlit as st

st.title("☃️ KESKO")

st.subheader("Welcome to test app")

st.subheader("Drag and Drop Files")
raw_text_file = st.file_uploader("Upload File",type=['txt'],
    accept_multiple_files=False)
if raw_text_file is not None:
	file_details = {"Filename":raw_text_file.name,"FileType":raw_text_file.type,"FileSize":raw_text_file.size}
	#st.write(file_details)
	# Check File Type
	if raw_text_file.type == "text/plain":
		try:
			raw_text = str(raw_text_file.read(),"utf-8")
			st.info("Text from TXT file")
			st.write(raw_text)
		except:
			st.error("TXT File Fetching Problem...")
				