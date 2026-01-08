import streamlit as st
import json
import os

DATA_FILE = "todo_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("ToDo Manager")

new_task = st.text_input("タスクを追加")

if st.button("追加"):
    if new_task.strip():
        st.session_state.tasks.append(new_task)
        save_tasks(st.session_state.tasks)
        st.rerun()

st.divider()

st.subheader("未完了タスク")

if not st.session_state.tasks:
    st.write("タスクはありません ")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([5, 1])
        col1.write(f"・{task}")
        if col2.button("完了", key=f"done_{i}"):
            st.session_state.tasks.pop(i)
            save_tasks(st.session_state.tasks)
            st.rerun()
