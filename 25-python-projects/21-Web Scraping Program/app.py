# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from urllib.parse import urlparse
# import io

# st.set_page_config(page_title="Web Scraper", layout="centered", page_icon="🌐")

# st.title("🌐 Web Scraper App")
# st.markdown("Scrape content from any public website using HTML tag, class or ID.")

# # Input URL
# url = st.text_input("Enter a valid URL to scrape", "https://quotes.toscrape.com")

# # Input for scraping parameters
# scrape_type = st.selectbox("Choose scrape method", ["Tag", "Class", "ID"])
# element = st.text_input(f"Enter the {scrape_type.lower()} name (e.g., 'p', 'quote', 'main')", "")

# # Scrape button
# if st.button("Scrape"):
#     if not url or not element:
#         st.warning("Please provide both URL and element.")
#     else:
#         try:
#             # Validate URL
#             parsed_url = urlparse(url)
#             if not parsed_url.scheme:
#                 st.error("Invalid URL. Please include http:// or https://")
#             else:
#                 response = requests.get(url)
#                 response.raise_for_status()
#                 soup = BeautifulSoup(response.content, "html.parser")

#                 # Scrape logic
#                 if scrape_type == "Tag":
#                     results = soup.find_all(element)
#                 elif scrape_type == "Class":
#                     results = soup.find_all(class_=element)
#                 elif scrape_type == "ID":
#                     found = soup.find(id=element)
#                     results = [found] if found else []

#                 # Extract and display
#                 data = [r.get_text(strip=True) for r in results if r]
#                 if data:
#                     df = pd.DataFrame(data, columns=["Extracted Content"])
#                     st.success(f"Scraped {len(data)} items.")
#                     st.dataframe(df)

#                     # Download button
#                     csv = df.to_csv(index=False).encode('utf-8')
#                     st.download_button("Download CSV", csv, "scraped_data.csv", "text/csv")
#                 else:
#                     st.warning("No data found with the specified criteria.")

#         except requests.exceptions.RequestException as e:
#             st.error(f"Request Error: {e}")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")





# web_scraper_app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

st.set_page_config(page_title="Web Scraper", layout="centered", page_icon="🌐")

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("📂 Select a Page", ["🏠 Home", "🔍 Scraper"])

# --- Home Page ---
if page == "🏠 Home":
    st.title("🌐 Web Scraper App")
    st.subheader("📘 How to Use")
    st.markdown("""
    This app allows you to extract HTML content from any public website.

    ### 👉 Steps:
    1. Go to the **Scraper** tab from the sidebar.
    2. Enter a **valid URL** (e.g., `https://quotes.toscrape.com`)
    3. Choose a method to scrape:
       - **Tag** – HTML tag like `p`, `h1`, `span`, etc.
       - **Class** – HTML class name like `quote`, `text`, etc.
       - **ID** – Unique element ID like `main`, `content`
    4. Click **Scrape** to extract the data.
    5. View the results and download as CSV.

    ### 🔍 Test Example:
    - URL: `https://quotes.toscrape.com`
    - Method: Class
    - Element: `text`

    ⚠️ Works best with static websites (non-JavaScript).

    """)

# --- Scraper Page ---
elif page == "🔍 Scraper":
    st.title("🔍 Web Scraper")

    url = st.text_input("Enter a valid URL to scrape", "https://quotes.toscrape.com")
    scrape_type = st.selectbox("Choose scrape method", ["Tag", "Class", "ID"])
    element = st.text_input(f"Enter the {scrape_type.lower()} name", "")

    if st.button("Scrape"):
        if not url or not element:
            st.warning("Please provide both URL and element.")
        else:
            try:
                parsed_url = urlparse(url)
                if not parsed_url.scheme:
                    st.error("Invalid URL. Include http:// or https://")
                else:
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    response = requests.get(url, headers=headers)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.content, "html.parser")

                    if scrape_type == "Tag":
                        results = soup.find_all(element)
                    elif scrape_type == "Class":
                        results = soup.find_all(class_=element)
                    elif scrape_type == "ID":
                        found = soup.find(id=element)
                        results = [found] if found else []

                    data = [r.get_text(strip=True) for r in results if r]
                    if data:
                        df = pd.DataFrame(data, columns=["Extracted Content"])
                        st.success(f"✅ Scraped {len(data)} items.")
                        st.dataframe(df)

                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button("📥 Download CSV", csv, "scraped_data.csv", "text/csv")
                    else:
                        st.warning("No data found with the specified criteria.")

            except requests.exceptions.RequestException as e:
                st.error(f"Request Error: {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
