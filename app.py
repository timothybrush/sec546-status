import streamlit as st
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SEC546 Authoring Status", layout="wide")

CT = ZoneInfo("America/Chicago")
LAST_UPDATED = "March 9, 2026 at 22:33 CT"

st.title("SEC546: Securing Agentic AI")
st.subheader("Authoring Status")
st.caption("Status report for Lara and Frank at SANS Institute")

viewed_on = datetime.now(CT).strftime("%B %d, %Y at %H:%M CT")
st.markdown(f"**Last updated:** {LAST_UPDATED} &nbsp;|&nbsp; **Viewed:** {viewed_on}")

DONE = "✅"
NOTDONE = "❌"
HALF = "🔶 50%"
NA = "N/A"

rows = [
    [
        "1.0 — Introduction to Agentic AI Risk Landscape",
        DONE,
        DONE,
        f"{DONE} Lab 1.0 Initial Setup",
    ],
    [
        "1.1 — Enforcing Input and Output Boundaries",
        DONE,
        NOTDONE,
        f"{HALF} Lab 1.1: Hardening with Guardrails AI",
    ],
    [
        "1.2 — Defending Against Prompt Injection",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 1.2 Goal Integrity Controls",
    ],
    [
        "1.3 — Least-Privilege & Blast Radius Controls",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 1.3 Permission Scoping Lab",
    ],
    [
        "1.4 — Resource Governance & Agent Throttling",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 1.4 Budget & Rate Enforcement",
    ],
    [
        "2.1 — Securing Persistent Agent Memory",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 2.1 Memory Integrity Controls",
    ],
    [
        "2.2 — Detecting & Stopping Runaway Agents",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 2.2 Safe Agent Termination",
    ],
    [
        "2.3 — Verifying Agent Identity & Trust",
        NOTDONE,
        NOTDONE,
        f"{HALF} Lab 2.3 Multi-Agent Trust Enforcement",
    ],
    ["2.4 — Emerging Threats & Future Defenses", NOTDONE, NOTDONE, f"{HALF} Lab: CTF"],
]

df = pd.DataFrame(
    rows, columns=["Module", "PowerPoint Slides", "Speaker Notes", "Lab Setup"]
)


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


styled = (
    df.style.applymap(
        style_cell, subset=["PowerPoint Slides", "Speaker Notes", "Lab Setup"]
    )
    .set_properties(subset=["Module"], **{"text-align": "left", "font-weight": "500"})
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

st.dataframe(styled, use_container_width=True, hide_index=True)

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.success("✅  Completed")
col2.warning("🔶  In Progress (50%)")
col3.error("❌  Not Done")
col4.info("N/A  Not Applicable")
