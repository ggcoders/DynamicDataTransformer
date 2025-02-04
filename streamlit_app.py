import streamlit as st
import pandas as pd

def get_df(file) -> pd.DataFrame | None:
    '''
    get_df(file) is going to return a dataframe if possible. \n
    The file extension will be retrieved by itself and if it's included in the pandas library it will be opened. \n
    All of this will be possible thanks to the extension retrieving and the eval() function.
    '''
    # if the file exists, proceed to get the extension
    f_ext = file.name.split(".")[-1]

    # retrieve dataframe with the desired extension
    try:
        data = eval(f"pd.read_{f_ext}(f)")

    # error handling if the extension is not correct formatting
    except: 
        st.error(f"Incompatible extension -> {f_ext}")
        st.code("'Extensions supported' = [ CSV, XLSX, TXT, JSON, HTML, LaTeX, XML, SQL ]")
        st.error("If the extension is in the list, please make sure that the file is formatted correctly")
        
        return None
    
    return data


if "__name__" == "__name__":
    st.markdown("# Dynamic Data Transformer (:rainbow[DDT])")
    f = st.file_uploader(label="Input your file below")

    if f:
        extension = f.type.split("/")[-1]
    
        df = get_df(f)

        # printing analytics in the terminal for usage control 
        print(
            "---> file uploaded!\n\t"
            f"name: '{f.name}'\n\t"
            f"size: {(f.size / 1_000_000):.3f} Mb\n\t"
            f"extension: {extension}\n\t"
            f"df status: {'Successful upload' if df is not None else 'Unsuccesful upload'}\n\t"
            f"df.shape: {df.shape if df is not None else '-'}"
            )

