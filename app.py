
import streamlit as st

# Pupil list
pupils = [f"Pupil {i}" for i in range(1, 21)]

# Project data
projects = {
    "Mirror Frame": {
        "frame": ["Corner Halving", "T Halving", "Mortice & Tenon"],
        "carcass": ["Dowel"],
        "machines": ["Mortice Machine", "Band Facer"],
        "tools": ["Power Drill"]
    },
    "Truck": {
        "frame": ["Stubbed Mortice & Tenon"],
        "carcass": ["Rebate", "Dowel"],
        "machines": ["Band Facer", "Wood Turning Lathe"],
        "tools": ["Power Drill", "Sander"]
    },
    "Corner Unit": {
        "frame": [],
        "carcass": ["Through Housing", "Dowel", "Rebate"],
        "machines": ["Band Facer"],
        "tools": ["Power Drill", "Sander"]
    },
    "Sling Puck": {
        "frame": ["Bridle Joint"],
        "carcass": ["Through Housing"],
        "machines": ["Band Facer"],
        "tools": ["Power Drill", "Sander"]
    },
    "AVU": {
        "frame": ["Corner Halving"],
        "carcass": ["Dowel"],
        "machines": ["Band Facer", "Wood Turning Lathe"],
        "tools": ["Power Drill", "Sander"]
    },
}

completion_options = [
    "Not Attempted",
    "Frame Only",
    "Carcass Only",
    "Both Joints (Not Assembled)",
    "Fully Completed"
]

# Select pupil
st.title("Woodworking Pupil Tracker")
selected_pupil = st.selectbox("Select Pupil", pupils)

# Project completion inputs
st.header("Project Completion")
project_status = {}
for project in projects:
    status = st.selectbox(f"{project} - Completion Level", completion_options, key=project)
    project_status[project] = status

# Calculate joint/tool usage
frame_joints = set()
carcass_joints = set()
machines_used = set()
tools_used = set()

for proj, status in project_status.items():
    data = projects[proj]
    if status in ["Frame Only", "Both Joints (Not Assembled)", "Fully Completed"]:
        frame_joints.update(data["frame"])
    if status in ["Carcass Only", "Both Joints (Not Assembled)", "Fully Completed"]:
        carcass_joints.update(data["carcass"])
    if status in ["Both Joints (Not Assembled)", "Fully Completed"]:
        machines_used.update(data["machines"])
        tools_used.update(data["tools"])

# Show summary
st.header("Summary")
st.write(f"**Unique Frame Joints:** {len(frame_joints)} - {frame_joints}")
st.write(f"**Unique Carcass Joints:** {len(carcass_joints)} - {carcass_joints}")
st.write(f"**Unique Machines Used:** {len(machines_used)} - {machines_used}")
st.write(f"**Unique Power Tools Used:** {len(tools_used)} - {tools_used}")

# Pass checks
st.success("✅ Frame Unit Passed" if len(frame_joints) >= 4 else "❌ Frame Unit Not Passed")
st.success("✅ Carcass Unit Passed" if len(carcass_joints) >= 3 else "❌ Carcass Unit Not Passed")
st.success("✅ Machines Unit Passed" if len(machines_used) >= 2 else "❌ Machines Unit Not Passed")
st.success("✅ Power Tools Unit Passed" if len(tools_used) >= 2 else "❌ Power Tools Unit Not Passed")
