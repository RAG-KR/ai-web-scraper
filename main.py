import streamlit as st
from scrape import scrape_website , split_dom_content , clean_body_content ,extract_body_content
from parse import parse_with_ollama


st.title('ai web scraper')
url = st.text_input("Enter a website url")

if st.button('scrape site'):
    st.write('scraping the website')
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander('veiw DOM Contet'):
        st.text_area('DOM Content' , cleaned_content , height = 300)

if 'dom_content' in st.session_state:
    parse_description = st.text_area('describe what you want to parse')
    if st.button('parse content'):
        if parse_description:
            st.write('parsing the content')
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks , parse_description)
            st.write(result)

 
