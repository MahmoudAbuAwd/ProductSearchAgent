# streamlit_app.py (Optional UI)
import streamlit as st
from  app.agent import ProductResearchAgent
import json

def main():
    st.set_page_config(page_title="Product Research Agent", page_icon="🔍")
    
    st.title("🔍 Product Research Agent")
    st.write("Get comprehensive product research with AI-powered analysis")
    
    # Initialize agent
    if 'agent' not in st.session_state:
        st.session_state.agent = ProductResearchAgent()
    
    # Input section
    query = st.text_input(
        "What product would you like to research?",
        placeholder="e.g., Best laptop for programming under $1000"
    )
    
    if st.button("🔍 Research Product") and query:
        with st.spinner("Researching product... This may take a moment."):
            try:
                results = st.session_state.agent.research_product(query)
                
                # Display results
                st.success("Research completed!")
                
                # Tabs for organized display
                tab1, tab2, tab3, tab4 = st.tabs(["📊 Analysis", "💡 Recommendations", "📋 Comparison", "🔍 Raw Data"])
                
                with tab1:
                    st.subheader("Analysis")
                    st.write(results["analysis"])
                
                with tab2:
                    st.subheader("Recommendations")
                    st.write(results["recommendations"])
                
                with tab3:
                    st.subheader("Comparison Chart")
                    st.markdown(results["comparison_chart"])
                
                with tab4:
                    st.subheader("Raw Research Data")
                    st.json(results["raw_data"])
                
                # Download button
                st.download_button(
                    label="📥 Download Results",
                    data=json.dumps(results, indent=2),
                    file_name=f"product_research_{query.replace(' ', '_')}.json",
                    mime="application/json"
                )
                
            except Exception as e:
                st.error(f"Error during research: {str(e)}")

if __name__ == "__main__":
    main()