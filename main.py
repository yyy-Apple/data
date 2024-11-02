import streamlit as st
import json

def load_from_jsonl(file_name: str):
    def load_json_line(line: str, i: int, file_name: str):
        try:
            return json.loads(line)
        except:
            raise ValueError(f"Error in line {i+1}\n{line} of {file_name}")

    with open(file_name, "r", encoding="UTF-8") as f:
        data = [load_json_line(line, i, file_name) for i, line in enumerate(f)]
    return data


def main():

    st.title("JSONL File Visualizer")
    file_path = "round2_filtered_data_full.jsonl"
    if file_path:
        try:
            data = load_from_jsonl(file_path)
            max_index = len(data) - 1

            index = st.slider(
                "Select the index of the line:", min_value=0, max_value=max_index
            )

            selected_data = data[index]

            text = selected_data.get("text", "")
            question = selected_data.get("question", "")
            answer = selected_data.get("final_answer", "")
            try:
                retrieved_text_idx = text.index("### Text\nRetrieved from")
            except:
                retrieved_text_idx = 0
          
            st.title(f"Question at {index}:")
            st.markdown(question, unsafe_allow_html=True)
            st.divider()

            st.title(f"Answer at {index}:")
            st.markdown(answer, unsafe_allow_html=True)
            st.divider()
            
            st.title(f"Original text {index}:")
            st.markdown(text[retrieved_text_idx:], unsafe_allow_html=True)
            st.divider()

        except FileNotFoundError: 
            st.error("File not found. Please check the file path.")
        except json.JSONDecodeError:
            st.error("Invalid JSON format. Please check the file contents.")


if __name__ == "__main__":
    main()
