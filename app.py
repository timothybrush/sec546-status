import streamlit as st
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SEC546 Authoring Status", layout="wide")

CT = ZoneInfo("America/Chicago")
LAST_UPDATED = "August 9, 2026 at 12:30 CT"

st.title("SEC546: Securing Agentic AI (5-day)")
st.subheader("Authoring Status")
st.caption("Status report for Lara and Frank at SANS Institute")
st.markdown("**Course Author:** Viswanath Chirravuri")

viewed_on = datetime.now(CT).strftime("%B %d, %Y at %H:%M CT")
st.markdown(f"**Last updated:** {LAST_UPDATED} &nbsp;|&nbsp; **Viewed:** {viewed_on}")

st.info(
    "📌 **Note:** All sections (1, 2, 3, 4, 5) are updated to use the "
    "**gpt-oss-20b** and **AWS Nova 2 Lite** models."
)

DONE = "✅"
NOTDONE = "❌"
HALF = "🔶 50%"
NA = "N/A"

STATUS_COLUMNS = ["PowerPoint Slides", "Speaker Notes", "Lab Setup"]

sections = [
    {
        "label": "SECTION 1",
        "title": "Foundations of Agentic AI Security",
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
                f"{DONE} Lab 1.1: Hardening with NeMo Guardrails",
            ],
            [
                "1.2 Defending Against Prompt Injection",
                DONE,
                DONE,
                f"{DONE} Lab 1.2 Agent Goal Integrity Controls",
            ],
            [
                "1.3 Secure Agent Development Patterns",
                DONE,
                DONE,
                f"{DONE} Lab 1.3 Build Secure Agent Chain",
            ],
            [
                "1.4 Agent Identity, Permissions & Least Agency",
                DONE,
                DONE,
                f"{DONE} Lab 1.4 Privilege Scoping & Identity Controls",
            ],
        ],
    },
    {
        "label": "SECTION 2",
        "title": "Agent Operations, Hardening, and MCP Defense",
        "rows": [
            [
                "2.1 Securing Agent Memory & Context Stores",
                DONE,
                DONE,
                f"{DONE} Lab 2.1 Memory Integrity Controls",
            ],
            [
                "2.2 Detecting, Containing & Isolating Rogue Agents",
                DONE,
                DONE,
                f"{DONE} Lab 2.2 Safe Agent Termination",
            ],
            [
                "2.3 Observability, Governance & Continuous Defense",
                DONE,
                DONE,
                f"{DONE} Lab 2.3 Runtime Governance & Policy Enforcement",
            ],
            [
                "2.4 MCP Gateway Defense & Policy",
                DONE,
                DONE,
                f"{DONE} Lab 2.4 Deploying Defensive MCP Gateway",
            ],
        ],
    },
    {
        "label": "SECTION 3",
        "title": "Secure MCP, Desktop Agents, and Runtime Defense",
        "rows": [
            [
                "3.1 MCP Data Integrity & Context Security",
                DONE,
                DONE,
                f"{DONE} Lab 3.1 Detecting Context Poisoning & Tool Response Poisoning",
            ],
            [
                "3.2 Agent Tool Execution Sandboxing",
                DONE,
                DONE,
                f"{DONE} Lab 3.2 Tool Sandbox & Egress Controls",
            ],
            [
                "3.3 Securing Desktop Agents",
                DONE,
                DONE,
                f"{DONE} Lab 3.3 Securing OpenCode Agents",
            ],
            [
                "3.4 Agent Supply Chain & AIBOM Defense",
                DONE,
                DONE,
                f"{DONE} Lab 3.4 Dependency, Skill & Prompt Provenance",
            ],
        ],
    },
    {
        "label": "SECTION 4",
        "title": "Multi-Agent, Browser & Computer-Use Agent Security",
        "rows": [
            [
                "4.1 Multi-Agent A2A Protocol Defense",
                DONE,
                DONE,
                f"{DONE} Lab 4.1 A2A Trust Chain Controls",
            ],
            [
                "4.2 Securing Browser & Computer-Use Agents",
                DONE,
                DONE,
                f"{DONE} Lab 4.2 CUA Action Sandboxing",
            ],
            [
                "4.3 Delegated Agent Authorization Defense",
                DONE,
                DONE,
                f"{DONE} Lab 4.3 Token Exchange & Scoping Controls",
            ],
            [
                "4.4 Cross-Agent Data Leakage Defense",
                DONE,
                DONE,
                f"{DONE} Lab 4.4 Task Contamination Isolation Controls",
            ],
        ],
    },
    {
        "label": "SECTION 5",
        "title": "Cyber-Physical Agent Security & Emerging Frontiers",
        "rows": [
            [
                "5.1 Physical-World Agent Safety",
                NOTDONE,
                NOTDONE,
                f"{NOTDONE} Lab 5.1 Robotic & IoT Kill-Switch Controls",
            ],
            [
                "5.2 Emerging Agentic Security Topics",
                NOTDONE,
                NOTDONE,
                f"{NOTDONE} Lab 5.2 Confidential Agent Execution & Attestation",
            ],
            [
                "5.3 CTF: Agent Defense Capstone",
                NOTDONE,
                NOTDONE,
                f"{HALF} Lab 5.3 Live Defense Operations CTF",
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
