import streamlit as st
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SEC546 Authoring Status", layout="wide")

CT = ZoneInfo("America/Chicago")
LAST_UPDATED = "April 29, 2026 at 12:00 CT"

st.title("SEC546: Securing Agentic AI")
st.subheader("Authoring Status")
st.caption("Status report for Lara and Frank at SANS Institute")
st.markdown("**Course Author:** Viswanath Chirravuri")

viewed_on = datetime.now(CT).strftime("%B %d, %Y at %H:%M CT")
st.markdown(f"**Last updated:** {LAST_UPDATED} &nbsp;|&nbsp; **Viewed:** {viewed_on}")

DONE = "✅"
NOTDONE = "❌"
HALF = "🔶 50%"
NA = "N/A"

STATUS_COLUMNS = ["PowerPoint Slides", "Speaker Notes", "Lab Setup"]

sections = [
    {
        "label": "SECTION 1",
        "title": "Foundations of Agentic Security & Boundary Defenses",
        "rows": [
            [
                "1.0 Introduction to Agentic AI Risk Landscape & Threat Model",
                DONE,
                DONE,
                f"{DONE} Lab 1.0 Initial Setup",
            ],
            [
                "1.1 Enforcing Input and Output Boundaries",
                DONE,
                DONE,
                f"{DONE} Lab 1.1: Hardening with Guardrails AI",
            ],
            [
                "1.2 Defending Against Prompt Injection",
                DONE,
                DONE,
                f"{DONE} Lab 1.2 Agent Goal Integrity Controls",
            ],
            [
                "1.3 Secure Agent Development Patterns",
                NOTDONE,
                NOTDONE,
                f"{DONE} Lab 1.3 Build Secure Agent Chain",
            ],
            [
                "1.4 Agent Identity, Permissions & Least Agency",
                NOTDONE,
                NOTDONE,
                f"{DONE} Lab 1.4 Privilege Scoping & Identity Controls",
            ],
        ],
    },
    {
        "label": "SECTION 2",
        "title": "Advanced Defenses: Hardening, Operations, and Multi-Agent Ecosystems",
        "rows": [
            [
                "2.1 Securing Agent Memory & Context Stores",
                NOTDONE,
                NOTDONE,
                f"{DONE} Lab 2.1 Memory Integrity Controls",
            ],
            [
                "2.2 Detecting, Containing & Isolating Rogue Agents",
                NOTDONE,
                NOTDONE,
                f"{DONE} Lab 2.2 Safe Agent Termination",
            ],
            [
                "2.3 Observability, Governance & Continuous Defense",
                NOTDONE,
                NOTDONE,
                f"{DONE} Lab 2.3 Runtime Governance & Policy Enforcement",
            ],
            [
                "2.4 Emerging Threats & Future Defenses",
                NOTDONE,
                NOTDONE,
                "",
            ],
        ],
    },
]


def style_cell(val):
    if isinstance(val, str):
        if val.startswith(DONE):
            return "background-color: #d4edda; color: #155724; text-align: center;"
        if val == NA:
            return "background-color: #f0f0f0; color: #6c757d; text-align: center;"
        if val.startswith("🔶"):
            return "background-color: #fff3cd; color: #856404; text-align: center;"
        if val.startswith(NOTDONE):
            return "background-color: #fde8e8; color: #721c24; text-align: center;"
    return ""


def build_styled_dataframe(rows):
    df = pd.DataFrame(
        rows, columns=["Module", "PowerPoint Slides", "Speaker Notes", "Lab Setup"]
    )
    return (
        df.style.map(style_cell, subset=STATUS_COLUMNS)
        .set_properties(
            subset=["Module"], **{"text-align": "left", "font-weight": "500"}
        )
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "#2c3e50"),
                        ("color", "white"),
                        ("font-weight", "bold"),
                        ("text-align", "center"),
                        ("padding", "10px 12px"),
                    ],
                },
                {"selector": "td", "props": [("padding", "8px 12px")]},
                {
                    "selector": "tr:nth-child(even)",
                    "props": [("background-color", "#f9f9f9")],
                },
            ]
        )
    )


for section in sections:
    st.markdown(f"### {section['label']}")
    st.subheader(section["title"])
    st.markdown("**Modules & Labs**")
    st.dataframe(
        build_styled_dataframe(section["rows"]),
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.success("✅  Completed")
col2.warning("🔶  In Progress (50%)")
col3.error("❌  Not Done")
col4.info("N/A  Not Applicable")
