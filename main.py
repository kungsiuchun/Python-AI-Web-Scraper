import streamlit as st
from scrape import scrape_webpage, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("python-ai-web-scraper")
url = st.text_input("Enter the URL of the webpage to scrape:")

if st.button("Scrape"):
    st.write(f"Scraping the webpage at: {url}")
    # Here you would add the web scraping logic
    st.write("Web scraping in progress...")
    result = scrape_webpage(url)
    
    body_content = extract_body_content(result)
    clean_body_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_body_content

    with st.expander("Scraped DOM Content"):
        st.text_area("DOM Content", value=st.session_state.dom_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse from the DOM content:", height=100)

    if st.button("Parse DOM Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_output = parse_with_ollama(dom_chunks, parse_description)

            st.text_area("Parsed Output", value=parsed_output, height=300)
            st.write(parsed_output)

